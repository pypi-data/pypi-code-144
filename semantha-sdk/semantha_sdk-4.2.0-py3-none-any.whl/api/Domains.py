from semantha_sdk.model.DomainConfiguration import DomainConfiguration
from semantha_sdk.model.DomainSettings import DomainSettings
from semantha_sdk.model.Domains import Domains as _DomainsDTO, Domain as _DomainDTO
from semantha_sdk.rest.RestClient import RestClient
from semantha_sdk.response.SemanthaPlatformResponse import SemanthaPlatformResponse
from semantha_sdk.api.Documents import Documents
from semantha_sdk.api.ReferenceDocuments import ReferenceDocuments
from semantha_sdk.api.References import References
from semantha_sdk.api.DocumentAnnotations import DocumentAnnotations
from semantha_sdk.api.DocumentComparisons import DocumentComparisons
from semantha_sdk.api import SemanthaAPIEndpoint


class Domain(SemanthaAPIEndpoint):
    """ Endpoint for a specific domain.

        References: documents, documentannotations, documentcomparisons, documentclasses,
            modelclasses, modelinstances, referencedocuments, references,
            settings, stopwords, similaritymatrix, tags and validation.
    """
    def __init__(self, session: RestClient, parent_endpoint: str, domain_name: str):
        super().__init__(session, parent_endpoint)
        self._domain_name = domain_name
        self.__documents = Documents(session, self._endpoint)
        self.__document_annotations = DocumentAnnotations(session, self._endpoint)
        self.__document_comparisons = DocumentComparisons(session, self._endpoint)
        self.__reference_documents = ReferenceDocuments(session, self._endpoint)
        self.__references = References(session, self._endpoint)

    @property
    def _endpoint(self):
        return self._parent_endpoint + f"/{self._domain_name}"

    @property
    def documents(self):
        return self.__documents

    @property
    def reference_documents(self) -> ReferenceDocuments:
        return self.__reference_documents

    @property
    def references(self) -> References:
        return self.__references

    def get_metadata(self) -> SemanthaPlatformResponse:
        return self._session.get(f"{self._endpoint}/metadata").execute()

    def get_rule(self) -> SemanthaPlatformResponse:
        return self._session.get(f"{self._endpoint}/rules").execute()

    def get_documentclasses(self) -> SemanthaPlatformResponse:
        return self._session.get(f"{self._endpoint}/documentclasses").execute()

    def get_subclasses(self, id: str) -> SemanthaPlatformResponse:
        return self._session.get(
            f"{self._endpoint}/documentclasses/{id.lower()}/documentclasses"
        ).execute()

    def get_class_with_subclasses(self, id: str) -> SemanthaPlatformResponse:
        return self._session.get(f"{self._endpoint}/documentclasses/{id.lower()}").execute()

    def get_class_documents(self, id: str) -> SemanthaPlatformResponse:
        return self._session.get(
            f"{self._endpoint}/documentclasses/{id.lower()}/referencedocuments"
        ).execute()

    def get_configuration(self) -> DomainConfiguration:
        return self._session.get(f"{self._endpoint}").execute().to(DomainConfiguration)

    def get_model_classes(self) -> SemanthaPlatformResponse:
        return self._session.get(f"{self._endpoint}/modelclasses").execute()

    def get_settings(self) -> DomainSettings:
        return self._session.get(f"{self._endpoint}/settings").execute().to(DomainSettings)

    def get_stopwords(self) -> SemanthaPlatformResponse:
        return self._session.get(f"{self._endpoint}/stopwords").execute()

    def get_tags(self) -> SemanthaPlatformResponse:
        return self._session.get(f"{self._endpoint}/tags").execute()

    def get_custom_entity_by_id(self, domain: str, entity: str):
        return self._session.get(f"/api/model/domains/{domain}/namedentities/{entity}").execute()

    def get_all_regexes(self, domain: str):
        return self._session.get(f"/api/model/domains/{domain}/regexes").execute()

    def get_regex(self, domain: str, id: str):
        return self._session.get(f"/api/model/domains/{domain}/regexes/{id}").execute()

    def get_all_synonyms(self, domain: str):
        return self._session.get(f"/api/model/domains/{domain}/synonyms").execute()


# TODO: Add docstrings, comments, type hints and error handling.
class Domains:
    """
        References:
            Specific domains by name
    """
    def __init__(self, session: RestClient, parent_endpoint: str):
        self._session = session
        self.__endpoint = parent_endpoint + "/domains"

    def get_all(self) -> list[_DomainDTO]:
        """ Get all available domains """
        return self._session.get(self.__endpoint).execute().to(_DomainsDTO).domains

    def get_one(self, domain_name: str) -> Domain:
        # Returns a Domain object for the given domainname, throws error if id doesn't exist
        return Domain(self._session, self.__endpoint, domain_name)
