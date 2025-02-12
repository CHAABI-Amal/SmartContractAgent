#Cet agent utilise Slither pour détecter les failles du smart contract.
import subprocess

class SecurityAgent:
    def __init__(self, contract_path):
        self.contract_path = contract_path

    def analyze_contract(self):
        result = subprocess.run(["docker", "run", "-v", "$(pwd):/mnt/slither", "trailofbits/slither", "/mnt/slither/" + self.contract_path], capture_output=True, text=True)
        return result.stdout


agent_security = SecurityAgent("contracts/SmartContract.sol")
print(agent_security.analyze_contract())
