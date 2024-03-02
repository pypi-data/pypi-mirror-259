import json
import re
from pathlib import Path


class ContractDataWriter:

    @staticmethod
    def write_data(base_output_path, deploy_env, abi, chain_id, contract_name, address=""):
        match = re.search(r'\.(.*)', str(chain_id))
        data_path_output_path = Path(f"{base_output_path}/{deploy_env}/{match.group(1)}")
        data_path_output_path.mkdir(parents=True, exist_ok=True)
        file_data = {
            "address": hex(address) if address else "null",
            "chain_id": repr(chain_id),
            "abi": abi
        }
        with open(data_path_output_path / f"{contract_name}_output.json", "w") as file:
            json.dump(file_data, file, indent=4)