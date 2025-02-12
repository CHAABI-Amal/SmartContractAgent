from web3 import Web3

# Connexion au fournisseur Ethereum (Ganache ou Infura)
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))  # Remplace par l'URL de ton fournisseur

# Adresse du contrat (assure-toi qu'elle est correcte)
contract_address = '0x2CaD54232302141E6775488ABaF99A99bae9C731'

# Vérifier que l'adresse est valide
if web3.is_address(contract_address):  # Correction ici, 'is_address' au lieu de 'isAddress'
    print("Adresse valide")
else:
    print("Adresse invalide")

# ABI de ton contrat (remplace par l'ABI complète que tu as)
abi = [
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "ExecutedTransaction",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "balance",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "withdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# Crée une instance de ton contrat
contract = web3.eth.contract(address=contract_address, abi=abi)

# Appel de la fonction get_balance pour afficher le solde actuel du contrat
def get_balance():
    balance = contract.functions.balance().call()
    print(f"Le solde du contrat est : {web3.fromWei(balance, 'ether')} ETH")

# Fonction `deposit` pour envoyer de l'ETH au contrat
def deposit(amount_in_ether):
    tx = {
        'from': web3.eth.accounts[0],  # Remplace avec l'adresse de l'envoyeur
        'to': contract_address,
        'value': web3.to_wei(amount_in_ether, 'ether'),  # Remplacé 'toWei' par 'to_wei'
        'gas': 2000000
    }
    txn_hash = web3.eth.send_transaction(tx)  # Remplacé 'sendTransaction' par 'send_transaction'
    print(f"Transaction envoyée : {txn_hash.hex()}")

# Fonction `withdraw` pour retirer des fonds
def withdraw(amount_in_ether):
    tx = contract.functions.withdraw(web3.to_wei(amount_in_ether, 'ether')).build_transaction({  # Remplacé 'buildTransaction' par 'build_transaction'
        'from': web3.eth.accounts[0],  # Remplace avec l'adresse de l'envoyeur
        'gas': 2000000,
        'nonce': web3.eth.get_transaction_count(web3.eth.accounts[0]),  # Remplacé 'getTransactionCount' par 'get_transaction_count'
    })
    signed_txn = web3.eth.account.sign_transaction(tx, private_key='0x5cd9412d9e33baae0b61006ebcd083267e8fb4ded6b3c7973e2c49d75fe0898c')  # Remplace avec ta clé privée
    txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)  # Remplacé 'sendRawTransaction' par 'send_raw_transaction'
    print(f"Transaction envoyée : {txn_hash.hex()}")

# Exemple d'utilisation de `deposit` (pour déposer 1.5 ETH)
deposit(1.5)

# Exemple d'utilisation de `withdraw` (pour retirer 0.5 ETH)
withdraw(0.5)

# Appel de la fonction `get_balance` pour afficher le solde actuel
get_balance()
