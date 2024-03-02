import os
from setuptools import setup, find_packages


install_requires = [
    "aiohttp==3.9.3",
    "aiosignal==1.3.1",
    "asgiref==3.7.2",
    "async-timeout==4.0.3",
    "attrs==23.2.0",
    "crypto_cpp_py==1.4.4",
    "ecdsa==0.18.0",
    "frozenlist==1.4.1",
    "idna==3.6",
    "lark==1.1.9",
    "marshmallow==3.20.2",
    "marshmallow-dataclass==8.6.0",
    "marshmallow-oneofschema==3.1.1",
    "mpmath==1.3.0",
    "multidict==6.0.5",
    "mypy-extensions==1.0.0",
    "packaging==23.2",
    "poseidon_py==0.1.4",
    "pycryptodome==3.20.0",
    "python-decouple==3.8",
    "six==1.16.0",
    "starknet-py==0.19.0",
    "sympy==1.11.1",
    "toml==0.10.2",
    "typing-inspect==0.9.0",
    "typing_extensions==4.9.0",
    "yarl==1.9.4"
]

tests_require = []

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="starknet-simple-deploy",
    version="0.1.4",
    description="Starknet Simple Deploy",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Web3Technologies LLC",
    author_email="zach@web3technologies.io",
    install_requires=install_requires,
    include_package_data=True,
    packages=find_packages("src"),
    test_suite="tests",
    tests_require=tests_require,
    extras_require={
        "test": tests_require,
    },
    package_dir={"":"src"},
    project_urls={
        "Source Code": "https://github.com/web3technologies/starknet_simple_deploy",
        "Issue Tracker": "https://github.com/web3technologies/starknet_simple_deploy/issues",
    }
)