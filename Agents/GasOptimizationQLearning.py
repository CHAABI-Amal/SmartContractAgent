import numpy as np
import random
from web3 import Web3

class GasOptimizationQLearning:
    def __init__(self, contract_address, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
        self.contract_address = contract_address
        self.q_table = {}  # Q-Table vide
        self.alpha = alpha  # Taux d'apprentissage
        self.gamma = gamma  # Facteur de réduction
        self.epsilon = epsilon  # Probabilité d'explorer au lieu d'exploiter

    def get_gas_price(self):
        return self.web3.eth.gas_price

    def choose_action(self, state):
        """ Choisit la meilleure action (ou explore aléatoirement) """
        if random.uniform(0, 1) < self.epsilon:
            return random.choice([-50, -10, 0, 10, 50])  # Exploration aléatoire
        return max(self.q_table.get(state, {}), key=self.q_table.get(state, {}).get, default=0)

    def update_q_table(self, state, action, reward, next_state):
        """ Met à jour la Q-Table avec la nouvelle récompense """
        if state not in self.q_table:
            self.q_table[state] = {}

        if action not in self.q_table[state]:
            self.q_table[state][action] = 0

        best_future_reward = max(self.q_table.get(next_state, {}).values(), default=0)
        self.q_table[state][action] += self.alpha * (reward + self.gamma * best_future_reward - self.q_table[state][action])

    def optimize_gas(self):
        """ Entraîne l'agent Q-Learning """
        state = self.get_gas_price()  # Obtenir le prix du gaz actuel
        print(f"[DEBUG] État actuel (prix du gaz) : {state}")

        action = self.choose_action(state)  # Choisir une action (explorer ou exploiter)
        print(f"[DEBUG] Action choisie : {action}")

        next_state = state + action  # Simuler le nouvel état
        print(f"[DEBUG] Prochain état : {next_state}")

        reward = -abs(action)  # Plus l'ajustement est faible, mieux c'est
        print(f"[DEBUG] Récompense : {reward}")

        self.update_q_table(state, action, reward, next_state)  # Mettre à jour la Q-Table
        print(f"[DEBUG] Q-Table après mise à jour : {self.q_table}")

        print(f"[OPTIMIZATION] Prix optimal du gaz recommandé : {next_state} Gwei")
        return next_state

