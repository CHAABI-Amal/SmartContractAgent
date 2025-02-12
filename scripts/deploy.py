from brownie import SmartContract, accounts

def deploy():
    account = accounts.load("mon_compte")  # Charge un compte Brownie
    print(account.balance())  # Affiche le solde du compte
    contract = SmartContract.deploy({"from": account, "gas": 6721975, "gas_price": 0})

    print(f"Contrat déployé à : {contract.address}")

deploy()
