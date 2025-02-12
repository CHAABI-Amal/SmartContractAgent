from web3 import Web3

class GasOptimizationAgent:
    def __init__(self, contract_address):
        self.web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))  # Remplace par ton fournisseur
        self.contract_address = contract_address

    def get_gas_price(self):
        return self.web3.eth.gas_price

    def optimize_gas(self):
        gas_prices = [self.get_gas_price() for _ in range(10)]
        return min(gas_prices)

    def get_contract_balance(self):
        balance = self.web3.eth.get_balance(self.contract_address)
        return self.web3.from_wei(balance, 'ether')

class GasOptimizationEnv:
    def __init__(self, contract_address):
        self.agent = GasOptimizationAgent(contract_address)  # Agent d'optimisation du gaz
        self.action_space = [0, 1, 2]  # Choix de stratégies

    def step(self, action):
        gas_price = self.agent.get_gas_price()
        
        if action == 0:
            optimized_gas = max(gas_price - 10, 1)
        elif action == 1:
            optimized_gas = gas_price
        elif action == 2:
            optimized_gas = gas_price + 10
        else:
            optimized_gas = gas_price
        
        contract_balance = self.agent.get_contract_balance()
        print(f"Solde du contrat : {contract_balance} Ether")

        reward = -abs(optimized_gas - gas_price)
        return optimized_gas, reward

    def reset(self):
        return self.agent.get_gas_price()

# Utilisation
contract_address = "0x2CaD54232302141E6775488ABaF99A99bae9C731"
env = GasOptimizationEnv(contract_address)
observation = env.reset()

for _ in range(1000):
    action = env.action_space[0]  # Exemple : toujours choisir la première stratégie
    observation, reward = env.step(action)
    print(f"Gaz Optimisé: {observation}, Récompense: {reward}")
