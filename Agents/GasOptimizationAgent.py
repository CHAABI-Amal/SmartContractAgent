#Cet agent utilise l’IA pour prédire les frais de gaz optimaux. 📄 Fichier :
import gym  
import numpy as np  
from web3 import Web3  

class GasOptimizationAgent:  
    def __init__(self, contract_address):  
        self.web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))  # Remplace par l'URL de ton fournisseur
        self.contract = self.web3.eth.contract(address=contract_address)  

    def get_gas_price(self):  
        return self.web3.eth.gas_price  

    def optimize_gas(self):  
        gas_prices = [self.get_gas_price() for _ in range(10)]  
        return min(gas_prices)  

# Utilisation  
agent_gas = GasOptimizationAgent("0x2CaD54232302141E6775488ABaF99A99bae9C731")  
optimal_gas = agent_gas.optimize_gas()  
print(f"Gaz optimal : {optimal_gas}")  
