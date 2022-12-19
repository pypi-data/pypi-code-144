import asyncio
import json
import logging
from dataclasses import dataclass, field
from functools import reduce, lru_cache
from pathlib import Path
from typing import Any, Dict, List, Mapping, NewType, Optional, Union, TypeVar, Type
from urllib.parse import urlparse
from urllib.request import urlopen

import yaml
from alibabacloud_credentials.models import Config
from dataclasses_jsonschema import JsonSchemaMixin, ValidationError

from iacer.generate_params import ParamGenerator, IAC_OCTOPUS_NAME
from iacer.exceptions import IacerException
from iacer.plugin.base_plugin import CredentialClient
from iacer.plugin.oss import OssPlugin
from iacer.plugin.ros import StackPlugin

LOG = logging.getLogger(__name__)

GENERAL_CONFIG_FILE = Path(f'~/.{IAC_OCTOPUS_NAME}.yml').expanduser().resolve()
DEFAULT_PROJECT_ROOT = Path('./').resolve()
DEFAULT_TEMPLATE_PATH = DEFAULT_PROJECT_ROOT
DEFAULT_CONFIG_FILE = f'.{IAC_OCTOPUS_NAME}.yml'
DEFAULT_OUTPUT_DIRECTORY = f'{IAC_OCTOPUS_NAME}_outputs'
OVERRIDES = f'.{IAC_OCTOPUS_NAME}_overrides.yml'
DEFAULT_AUTH_FILE = Path(f'~/.aliyun/config.json').expanduser().resolve()

CONFIG_KEYS = (
    GENERAL, PROJECT, TESTS
) = (
    'general', 'project', 'tests'
)

METADATA_KEYS = (
    AUTH, REGIONS, PARAMETERS, TAGS, OSS_CONFIG, TEMPLATE_CONFIG, ROLE_NAME, NAME
) = (
    'auth', 'regions', 'parameters', 'tags', 'oss_config', 'template_config', 'role_name', 'name'
)

TEMPLATE_CONFIG_ITEMS = (
    TEMPLATE_BODY, TEMPLATE_URL, TEMPLATE_ID, TEMPLATE_VERSION, TEMPLATE_LOCATION
) = (
    'template_body', 'template_url', 'template_id', 'template_version', 'template_location'
)

OSS_CONFIG_ITEMS = (
    BUCKET_NAME, BUCKET_REGION
) = (
    'bucket_name', 'bucket_region'
)


METADATA: Mapping[str, Mapping[str, Any]] = {
    AUTH: {
        'Description': 'Aliyun authentication section.',
        'Examples': [{
            'name': 'default',
            'location': '~/.aliyun/config.json'
        }]
    },
    REGIONS: {
        'Description': 'List of aliyun regions.',
        'Examples': [['cn-hangzhou', 'cn-beijing']]
    },
    PARAMETERS: {
        'Description': 'Parameter key-values to pass to template.',
        'Examples': [{
            'MyParameterKey1': 'MyParameterValue1',
            'MyParameterKey2': 'MyParameterValue2'
        }]
    },
    OSS_CONFIG: {
        'Description': 'Oss bucket configuration, include BucketName, BucketRegion and etc.',
        'Examples': [{
            'bucket_name': 'ExampleName',
            'bucket_region': 'cn-hangzhou'
        }]
    },
    TEMPLATE_CONFIG: {
        'Description': 'Oss bucket configuration, include BucketName, BucketRegion and etc.',
        'Examples': [{
            'template_body': '{"ROSTemplateFormatVersion": "2015-09-01"}',
            'template_url': 'oss://ros-template/demo',
            'template_id': '5ecd1e10-b0e9-4389-a565-e4c15efc****',
            'template_version': 'v1',
            'template_location': 'ros-template/'
        }]
    },
    TAGS: {
        'Description': 'TAGS to apply to template.',
        'Examples': [{
            'env': 'Product',
            'app': 'MyApp'
        }],
    },
    ROLE_NAME: {
        'Description': 'Role name to use while running test.',
        'Examples': ['my-test-role']
    }
}

# types
ParameterKey = NewType('ParameterKey', str)
ParameterValue = Union[str, int, bool, List[Union[int, str]]]
TagKey = NewType('TagKey', str)
TagValue = NewType('TagValue', str)
Region = NewType('Region', str)
OssConfigKey = NewType('OssConfigKey', str)
OssConfigValue = NewType('OssConfigValue', str)


@dataclass
class Auth(JsonSchemaMixin, allow_additional_props=False):
    name: Optional[str] = field(default=None)
    location: Optional[str] = field(default=None)

    def __post_init__(self):
        self.credential = self._get_credential()

    def __hash__(self):
        return hash((self.name, self.location))

    @lru_cache
    def _get_credential(self) -> CredentialClient:
        file_path = Path(self.location).expanduser().resolve() if self.location else DEFAULT_AUTH_FILE
        if not file_path.is_file():
            return
        try:
            with open(file_path, 'r', encoding='utf-8') as file_handle:
                config = json.load(file_handle)
            default = config.get('current')
            name = self.name or default
            if not name:
                return
            specified_profile = None
            profiles = config.get('profiles')
            for profile in profiles:
                if profile.get('name') == name:
                    specified_profile = profile
                    break
        except Exception as e:
            LOG.debug(str(e), exc_info=True)
            return

        if not specified_profile:
            return
        if specified_profile.get('mode') == 'AK':
            specified_config = Config(
                type='access_key',
                access_key_id=specified_profile.get('access_key_id'),
                access_key_secret=specified_profile.get('access_key_secret')
            )
        elif specified_profile.get('mode') == 'StsToken':
            specified_config = Config(
                type='sts',
                access_key_id=specified_profile.get('access_key_id'),
                access_key_secret=specified_profile.get('access_key_secret'),
                security_token=specified_profile.get('sts_token')
            )
        elif specified_profile.get('mode') == 'RamRoleArn':
            specified_config = Config(
                type='ram_role_arn',
                access_key_id=specified_profile.get('access_key_id'),
                access_key_secret=specified_profile.get('access_key_secret'),
                security_token=specified_profile.get('sts_token'),
                role_arn=specified_profile.get('ram_role_arn'),
                role_session_name=specified_profile.get('ram_session_name'),
                policy=specified_profile.get('policy', ''),
                role_session_expiration=specified_profile.get('expired_seconds', 900)
            )
        elif specified_profile.get('mode') == 'EcsRamRole':
            specified_config = Config(
                type='ecs_ram_role',
                role_name=specified_profile.get('ram_role_name')
            )
        else:
            return
        return CredentialClient(config=specified_config)


@dataclass
class OssCallbackConfig(JsonSchemaMixin, allow_additional_props=False):
    callback_url: Optional[str] = field(default=None)
    callback_host: Optional[str] = field(default=None)
    callback_body: Optional[str] = field(default=None)
    callback_body_type: Optional[str] = field(default=None)
    callback_var_params: Optional[dict] = field(default=None)


@dataclass
class OssConfig(JsonSchemaMixin, allow_additional_props=False):
    bucket_name: Optional[str] = field(default=None)
    bucket_region: Optional[str] = field(default=None)
    object_prefix: Optional[str] = field(default=None)
    callback_params: Optional[OssCallbackConfig] = field(default_factory=OssCallbackConfig)

    def validate_bucket(self, plugin: OssPlugin):
        if not plugin.bucket_exist():
            raise IacerException(f'oss bucket {self.bucket_name} in {self.bucket_region} region is not exist')


@dataclass
class TemplateConfig(JsonSchemaMixin, allow_additional_props=False):
    template_body: Optional[str] = field(default=None)
    template_url: Optional[str] = field(default=None)
    template_id: Optional[str] = field(default=None)
    template_version: Optional[str] = field(default=None)
    template_location: Optional[str] = field(default=None)

    def __hash__(self):
        return hash((
            self.template_body, self.template_url,
            self.template_id, self.template_version,
            self.template_location))

    @classmethod
    def _get_template_location(cls, template: Union[str, Path] = None) -> Path:
        suffix = ('json', 'yaml', 'yml')
        template_path = Path(template).resolve() if template else DEFAULT_TEMPLATE_PATH
        if template_path.is_file():
            return template_path
        template_file = None
        for su in suffix:
            template_file = next(template_path.glob(f'*.template.{su}'), None)
            if template_file is not None:
                break
        return template_file

    @lru_cache
    def generate_template_args(self) -> dict:
        result = self.to_dict()
        if self.template_id or self.template_body:
            return result

        if self.template_url:
            template_url = self.template_url
            components = urlparse(template_url)
            if components.scheme in ('oss', 'http', 'https'):
                return result
            elif components.scheme == 'file':
                try:
                    tpl_body = urlopen(template_url).read()
                    result[TEMPLATE_BODY] = tpl_body.decode('utf-8')
                    result.pop(TEMPLATE_URL)
                    return result
                except Exception as ex:
                    raise IacerException(f'failed to retrieve {template_url}: {ex}')
            else:
                raise IacerException(f'template url  {template_url} is not legally.')

        tpl_path = result.pop(TEMPLATE_LOCATION, None)
        tpl_location = self._get_template_location(tpl_path)
        if tpl_location is None:
            raise IacerException(f'failed to retrieve {tpl_path}')
        file_path = Path(tpl_location).expanduser().resolve()
        if not file_path.is_file():
            return result
        try:
            with open(str(file_path), 'r', encoding='utf-8') as file_handle:
                tpl_body = yaml.safe_load(file_handle)
                result[TEMPLATE_BODY] = json.dumps(tpl_body)
        except Exception as e:
            LOG.debug(str(e), exc_info=True)
            raise IacerException(f'can not find a template: {str(e)}')
        return result


@dataclass
class GeneralConfig(JsonSchemaMixin):
    '''General configuration settings.'''

    auth: Auth = field(
        default_factory=Auth, metadata=METADATA[AUTH])
    regions: Optional[List[Region]] = field(
        default_factory=list, metadata=METADATA[REGIONS])
    parameters: Optional[Dict[ParameterKey, ParameterValue]] = field(
        default_factory=dict, metadata=METADATA[PARAMETERS])
    parameters_order: Optional[List[str]] = field(default_factory=list)
    tags: Optional[Dict[TagKey, TagValue]] = field(
        default_factory=dict, metadata=METADATA[TAGS])
    oss_config: Optional[OssConfig] = field(
        default_factory=OssConfig, metadata=METADATA[OSS_CONFIG])


@dataclass
class ProjectConfig(GeneralConfig):
    '''Project specific configuration section'''

    name: Optional[str] = field(default='iacer-default-project-name')
    role_name: Optional[str] = field(
        default_factory=str, metadata=METADATA[ROLE_NAME])
    template_config: TemplateConfig = field(
        default_factory=TemplateConfig, metadata=METADATA[TEMPLATE_CONFIG])


@dataclass
class TestConfig(ProjectConfig):
    '''Test specific configuration section.'''

    def __post_init__(self):
        self.test_name = None
        self.region = None


T = TypeVar('T', bound='BaseConfig')


@dataclass
class BaseConfig(JsonSchemaMixin):
    general: GeneralConfig = field(default_factory=GeneralConfig)
    project: ProjectConfig = field(default_factory=ProjectConfig)
    tests: Dict[str, TestConfig] = field(default_factory=dict)

    @classmethod
    def merge(cls, base: Dict, new: Dict) -> Dict:
        result = base.copy()
        for item, value in new.items():
            if item == PARAMETERS:
                value.update(result.get(item, {}))
                result[item] = value
                continue
            if item not in result or not isinstance(value, dict):
                result[item] = value
                continue
            result[item] = cls.merge(result[item], value)
        return result

    @classmethod
    def generate_from_file(cls, file_path: Path, fail_ok=True, validate=True) -> dict:
        config_dict = {}
        if not file_path.is_file() and fail_ok:
            return config_dict
        try:
            with open(str(file_path), 'r', encoding='utf-8') as file_handle:
                config_dict = yaml.safe_load(file_handle)
            if validate:
                try:
                    cls.from_dict(config_dict)
                except ValidationError as e:
                    LOG.warning(f'config from {file_path} is illegal.')
                    LOG.debug(str(e), exc_info=True)
                    if not fail_ok:
                        raise e
            return config_dict
        except Exception as e:
            LOG.warning(f'failed to load config from {file_path}')
            LOG.debug(str(e), exc_info=True)
            if not fail_ok:
                raise e
        return config_dict

    @classmethod
    def create(cls: Type[T],
               global_config_path: Path = GENERAL_CONFIG_FILE,
               project_config_file: Path = DEFAULT_CONFIG_FILE,
               overrides_file: Path = OVERRIDES,
               args: Optional[dict] = None,
               project_path: str = None) -> T:
        project_root = Path(project_path).expanduser().resolve() if project_path else DEFAULT_PROJECT_ROOT
        project_config_path = project_root / project_config_file
        overrides_path = project_root / overrides_file
        sources = [
            cls.generate_from_file(global_config_path),
            cls.generate_from_file(project_config_path, fail_ok=False),
            cls.generate_from_file(overrides_path),
            args
        ]
        config = reduce(cls.merge, sources)
        general_config = config.get(GENERAL, {})
        merged_project_config = cls.merge(general_config, config.get(PROJECT))
        merged_test_configs = {
            key: cls.merge(merged_project_config, value) for key, value in config.get(TESTS, {}).items()
        }
        return cls.from_dict({
            GENERAL: general_config,
            PROJECT: merged_project_config,
            TESTS: merged_test_configs
        })

    async def get_all_configs(self, test_names: str = None):
        results = []
        base = self.tests
        test_names = test_names.split(',') if test_names else []
        all_regions = await self._get_test_regions()
        param_tasks = []
        for name, config in base.items():
            if test_names and name not in test_names:
                continue
            regions = [region.lower() for region in config.regions]
            if 'all' in regions or not regions:
                regions = all_regions

            template_args = config.template_config.generate_template_args()
            config.template_config = TemplateConfig.from_dict(template_args)

            for region in regions:
                region_config = TestConfig.from_dict(config.to_dict())
                region_config.region = region
                region_config.test_name = name
                oss_config = region_config.oss_config
                bucket_name = oss_config.bucket_name
                if bucket_name:
                    plugin = OssPlugin(
                        region_id=region,
                        bucket_name=bucket_name,
                        credential=region_config.auth.credential
                    )
                    oss_config.validate_bucket(plugin)
                resolved_parameters_task = ParamGenerator.result(region_config)
                param_tasks.append(asyncio.create_task(resolved_parameters_task))
                results.append(region_config)
        resolved_parameters = await asyncio.gather(*param_tasks)
        for config, params in zip(results, resolved_parameters):
            assert config.test_name == params.name
            assert config.region == params.region
            config.parameters = params.parameters
        return results

    def get_oss_config(self):
        oss_config = self.project.oss_config
        return oss_config.bucket_name, oss_config.bucket_region

    async def _get_test_regions(self):
        plugin = StackPlugin('cn-hangzhou', self.general.auth.credential)
        return await plugin.get_regions()
