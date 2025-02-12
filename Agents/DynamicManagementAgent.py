import gym
import numpy as np
from web3 import Web3
import random

class DynamicManagementAgent:
    def __init__(self, contract_address):
        # Initialisation du contrat et de l'adresse
        self.contract_address = contract_address
        self.web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))  

    def get_contract_balance(self):
        # Récupérer le solde du contrat
        balance = self.web3.eth.get_balance(self.contract_address)
        # Assurez-vous que 'fromWei' est bien disponible et utilisé correctement
        balance_in_ether = self.web3.from_wei(balance, 'ether')  # Convertir en Ether
        return balance_in_ether

