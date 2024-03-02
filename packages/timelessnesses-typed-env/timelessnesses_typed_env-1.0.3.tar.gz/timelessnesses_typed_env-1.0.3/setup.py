# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['timelessnesses']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'timelessnesses-typed-env',
    'version': '1.0.3',
    'description': 'A python module that help you have a type safety on enviroment variable',
    'long_description': '# typed-env\n\nA python module that help you have a type safety on enviroment variable (on runtime)\n\n## Documentation\n\n```python\ntimelessnesses.TypedEnv\n```\n\nA parent class that will help you ensure type safetiness on your enviroment variable.  \nUsage:\n\n```python\nfrom timelessnesses import typed_env\nimport datetime\n\nclass MyDotEnv(typed_env.TypedEnv):\n    # define your enviroment variable name and it\'s type (default value is optional and typing.Optional is also supported)\n    AMONG_US: bool = True\n    DISCORD_TOKEN: str\n    DATETIME: datetime.datetime = datetime.datetime.now()\n    NICE_DICTIONARY: typing.Dict[str, int] = {"a": 1, "b": 2}\n    DAMN_LIST: typing.List[int] = [1, 2, 3]\n    BALLS_KIND: BallsEnum # oh no! TypedEnv doesn\'t support my custom class!\n    # don\'t worry you can implement your own converter!\n\na = MyDotEnv()\na.add_validator(BallsEnum, lambda x: BallsEnum(int(x)))\na.configure(typed_env.Method.dotenv, dotenv=".env") # you have options to either get only from dotenv or os.environ or both!\n"""\na.get_env(typed_env.Method.all, dotenv="path_to_.env") # this fetch all the variable from both dotenv and os.environ\na.get_env(typed_env.Method.env) # this fetch all the variable from os.environ\na.get_env(typed_env.Method.dotenv, dotenv="path_to_.env") # this fetch all the variable from dotenv\nNOTE: for dotenv/all method you have to supply dotenv argument\n"""\na.raise_error_on_unknown_env = False # if this set to true any excessive enviroment variable will raise an error (default is True)\na.load() # let it do the work!\n```\n\n`TypedEnv` supports normal types like `str` or `int` and also `typing.Dict` and `typing.List` etc. But it also supports custom type by adding a validator, you are also allowed to overwrite the default validator by using `TypedEnv.add_validator` method.  \nCheck out more examples at `tests` folder!\n',
    'author': 'timelessnesses',
    'author_email': 'mooping3roblox@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/timelessnesses/typed_env',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
