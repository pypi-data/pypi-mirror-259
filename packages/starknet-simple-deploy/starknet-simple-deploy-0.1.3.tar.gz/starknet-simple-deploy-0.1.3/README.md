# Starknet Simple Deploy

## Overview

Starknet Simple Deploy is a Python package designed to simplify the process of deploying StarkNet smart contracts. It provides a set of APIs that abstract away the complexities involved in the deployment process, making it more accessible for developers of all skill levels. It utilizes API's from https://github.com/software-mansion/starknet.py

## Features

- **Simplified Deployment**: Decalre and Deploy StarkNet smart contracts with minimal setup and configuration.
- **Configurable**: Supports custom deployment configurations through `DeployerConfig`.
- **Write Deployment Data**: Supports ability to write data to a json file throug `ContractDataWriter`. 
- **Async Support**: Fully asynchronous API for efficient contract deployment.
- **Error Handling**: Designed to gracefully handle deployment errors and provide clear feedback.

## Installation

To install Starknet Simple Deploy, run the following command in your terminal:

```
pip install starknet-simple-deploy
```
## Quick Start

Here's a quick example to get you started with deploying a StarkNet smart contract:

```

from starknet_simple_deploy import (
    DeclareContract,
    DeployContract, 
    DeployerConfig, 
    ContractDataWriter, 
    InitializeContractData,

)
from starknet_simple_deploy.utils import get_abi


deployer_config = DeployerConfig.get_config(deploy_env, chain).init_account()
initialized_contract = InitializeContractData(contract_name="MyContract")
casm_class_hash, compiled_contract, sierra_class_hash = initialized_contract.read_contract_file_data()
declared_contract = DeclareContract(
    deployer_config,
    casm_class_hash,
    compiled_contract,
    sierra_class_hash
)
declared_contract = await declared_contract.get_contract()
deployer = DeployContract(
    declared_contract,
    deployer_config,
    sierra_class_hash,
    constructor_args={
        "oracle_address": deployed_oracle_contract.address,
        "contract_class_hash": sierra_class_hash
    }
)
deployed_contract = await deployer.deploy()
ContractDataWriter.write_data(
    deploy_env=args.deploy_env, 
    abi=get_abi(declared_contract),
    chain_id=deployer_config.chain_id,
    contract_name="MyContract", 
    address = deployed_contract.address
)
```

<!-- ## Documentation

For more detailed documentation on Starknet Simple Deploy, including all configuration options and API methods, please refer to [Documentation Link]. -->

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License

Starknet Simple Deploy is released under the MIT License.

## Support

If you have any questions or encounter any issues, please open an issue on the GitHub repository, and we'll do our best to assist you.
