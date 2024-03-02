import json
from starknet_py.contract import DeclareResult


get_abi = lambda contract: contract._get_abi() if isinstance(contract, DeclareResult) else json.loads(contract.abi)