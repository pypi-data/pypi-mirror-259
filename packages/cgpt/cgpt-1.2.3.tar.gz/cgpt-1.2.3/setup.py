# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cgpt',
 'cgpt.app',
 'cgpt.app.client',
 'cgpt.app.commands',
 'cgpt.app.server',
 'cgpt.app.utils']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1']

entry_points = \
{'console_scripts': ['cgpt = cgpt.__main__:cgpt']}

setup_kwargs = {
    'name': 'cgpt',
    'version': '1.2.3',
    'description': 'Cgpt',
    'long_description': '![PyPI](https://img.shields.io/pypi/v/cgpt)\n![python](https://img.shields.io/badge/Python-3.7-blue.svg)\n![commit activity](https://img.shields.io/github/commit-activity/m/ainayves/cgpt?color=blue)\n[![Build Status](https://img.shields.io/badge/Build%20status-Passing-green)](https://github.com/ainayves/cgpt/actions)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n<center><h1>🤖 MAKE AI POWERED SEARCH INSIDE YOUR CLI 💻</h1></center>\n</br>\n\n### ⭐ FEATURES\n\n- [AI conversation exactly the same as in openai website](#description)\n- [LAN support](#link-cgpt-inside-a-local-network)\n- [Docker support](#whale2-build-and-run-with-docker)\n\n</br>\n\n![cgpt1 1 28 (1)](https://user-images.githubusercontent.com/66997516/232239452-27e5c840-5699-44b8-bb28-da8d2dabc64f.gif)\n\n</br>\n\n### DESCRIPTIONS\n\n- `cgpt` is a Python package that allows you to use AI directly in your favorite Terminal.\n- `cgpt` is based on [CLICK](https://github.com/pallets/click) for creating beautiful command line interfaces in a composable way.\n\n### :question: REQUIREMENTS\n\n- python >=3.7\n- openai API KEY :\n  You need to register on openai to receive your own api key , here : [api_key](https://platform.openai.com/account/api-keys).\n\n### INSTALL FROM PYPI\n\nYou can install the latest version from pypi.\n\n```\npip install cgpt\n```\n\n### 🖥️ SETUP FOR DEVELOPPERS\n\n```\npip install -r requirements.txt\n```\n\n### 🔨 BUILD\n\n- For this part , it is better to use Linux.\n\nIf you are on Linux , launch:\n\n```\nsudo chmod +x build.sh\n```\n\nThen , :\n\n```\n./build.sh\n```\n\n### ⏯️ VERIFY INSTALLATION\n\n```\ncgpt-version\n```\n\n### 🚀 RUN\n\n```\ncgpt\n```\n\n### :link: CGPT INSIDE A LOCAL NETWORK\n\nYou can use cgpt inside a LAN.\n\n- You just need one Host (`connected to internet`) to be the server.\n- Other Hosts (`not connected to internet`) can ALWAYS use Chat GPT as `client`.\n\nNOTES :\n\n- For now , a server must be launched inside a `Linux` computer . If the server is inside `Windows` : the address is sometimes wrong (to be fixed in the next version).\n\n- Also , make sure that your `/etc/hosts` is configured correctly like :\n\n```\n127.0.0.1\tlocalhost\n127.0.1.1\tyour-hostanme\n```\n\n- A `client` can also use his own api_key in the next version.\n\n### :whale2: BUILD AND RUN WITH DOCKER\n\n- To make it easier , use the `docker-compose.yml` file :\n\n```\ndocker-compose run --rm app\n```\n\n### 💚 Feedback\n\nPlease feel free to leave feedback in issues/PRs.\n',
    'author': 'Aina Yves',
    'author_email': 'randrianaina.yves@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ainayves/cgpt',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
