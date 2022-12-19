# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_gpt3']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.1.5,<3.0.0',
 'nonebot-plugin-htmlrender>=0.2.0.1,<0.3.0.0',
 'nonebot2>=2.0.0rc2,<3.0.0',
 'openai>=0.25.0,<0.26.0',
 'pyyaml>=6.0,<7.0',
 'transformers>=4.25.1,<5.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-gpt3',
    'version': '1.0.7',
    'description': '',
    'long_description': '<div align="center">\n  <img src="https://s2.loli.net/2022/06/16/opBDE8Swad5rU3n.png" width="180" height="180" alt="NoneBotPluginLogo">\n  <br>\n  <p><img src="https://s2.loli.net/2022/06/16/xsVUGRrkbn1ljTD.png" width="240" alt="NoneBotPluginText"></p>\n</div>\n\n\n<div align="center">\n\n# Nnonebot-plugin-gpt3\n\n_✨ 基于openai GPT3官方API的对话插件 ✨_\n\n<p align="center">\n  <img src="https://img.shields.io/github/license/EtherLeaF/nonebot-plugin-colab-novelai" alt="license">\n  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python">\n  <img src="https://img.shields.io/badge/nonebot-2.0.0r4+-red.svg" alt="NoneBot">\n  <a href="https://pypi.python.org/pypi/nonebot-plugin-gpt3">\n      <img src="https://img.shields.io/pypi/dm/nonebot-plugin-gpt3" alt="pypi download">\n  </a>\n</p>\n\n\n</div>\n\n# 功能\n\n- [x] 上下文功能\n- [x] 会话导出\n- [x] 返回文字图片渲染\n- [x] 每个人单独会话\n- [x] 人格设置\n- [x] 连续会话\n\n# 如何使用？\n\n私聊中是直接发送消息，**群聊中是以回复的方式发送。**\n\n## 功能列表\n\n|          指令          |      需要@      |      描述       |\n| :--------------------: | :-------------: |:-------------:|\n|     刷新/重置对话      |       是        | 重置会话记录，开始新的对话 |\n|        重置人格        |       是        |    重置AI人格     |\n|        设置人格        |       是        |    设置AI人格     |\n|   导出会话/导出对话    |       是        |    导出历史会话     |\n|  **自定义的指令前缀**  | 自定义是否需要@ |    基本的聊天对话    |\n| **chat/聊天/开始聊天** |       是        |    开始连续对话     |\n| **stop/结束/结束聊天** |       否        |   结束连续聊天模式    |\n\n\n\n## 连续会话\n\n输入**chat/聊天/开始聊天**即可不加前缀，连续的对话，输入**结束/结束聊天**，即可结束聊天\n\n![image-20221217230058979](https://chrisyy-images.oss-cn-chengdu.aliyuncs.com/img/image-20221217230058979.png)\n\n## 人格设置\n\n预设了**AI助手/猫娘/nsfw猫娘**三种人格，可以通过人格设置切换。内置的设定可以从[这里看到](https://github.com/chrisyy2003/lingyin-bot/blob/main/plugins/gpt3/nonebot_plugin_gpt3/__init__.py#L16-L18)。\n\n![image-20221217231703614](https://chrisyy-images.oss-cn-chengdu.aliyuncs.com/img/image-20221217231703614.png)\n\n同样也可以手动指定人格\n\n![image-20221217232155100](https://chrisyy-images.oss-cn-chengdu.aliyuncs.com/img/image-20221217232155100.png)\n\n## 图片渲染\n\n图片渲染可以在配置文件中配置是否，需要渲染\n\n![image-20221217233729263](https://chrisyy-images.oss-cn-chengdu.aliyuncs.com/img/image-20221217233729263.png)\n\n# 安装\n\n1.  使用 nb-cli\n\n```\nnb plugin install nonebot_plugin_gpt3\n```\n\n2.   通过包管理器安装，可以通过nb，pip3，或者poetry等方式安装，以pip为例\n\n```\npip install nonebot_plugin_gpt3\n```\n\n随后在`bot.py`中加上如下代码，加载插件\n\n```\nnonebot.load_plugin(\'nonebot_plugin_gpt3\')\n```\n\n# 配置\n\n对于官方openai接口只需配置API Keys即可，所以请填写API在您配置的`chatgpt_token_path`下面，默认路径是`config/chatgpt_img_config.yml`\n\n文件内格式如下，有多个Key请按照如下格式配置。\n\n```\napi_keys:\n  - XXX\n  - YYY\n```\n\n之后是一些自定义配置，根据注释可以自行修改，如果需要配置请在`env.dev`下进行配置。\n\n```\nchatgpt_api_key_path = "config/chatgpt_api.yml" # api文件\nchatgpt_command_prefix = "chat"                 # 触发聊天的前缀\nchatgpt_need_at = False                         # 是否需要@\nchatgpt_image_render = False                    # 是否需要图片渲染\nchatgpt_image_limit = 100                       # 长度超过多少才会渲染成图片\n```\n\n',
    'author': 'chrisyy',
    'author_email': '1017975501@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
