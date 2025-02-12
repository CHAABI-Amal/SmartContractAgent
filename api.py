from flask import Flask, jsonify, render_template
from Agents.GasOptimizationQLearning import GasOptimizationQLearning
from Agents.SecurityAgent import SecurityAgent
from Agents.DynamicManagementAgent import DynamicManagementAgent

app = Flask(__name__)

# Initialisation des agents
gas_agent = GasOptimizationQLearning("0x2CaD54232302141E6775488ABaF99A99bae9C731")
security_agent = SecurityAgent("contracts/SmartContract.sol")
dynamic_agent = DynamicManagementAgent("0x2CaD54232302141E6775488ABaF99A99bae9C731")

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/optimize_gas', methods=['GET'])
def optimize_gas():
    optimal_gas_price = gas_agent.optimize_gas()
    print(f"[API] Prix optimal du gaz retourné par l'agent : {optimal_gas_price} Gwei")
    return jsonify({"optimal_gas_price": optimal_gas_price})

@app.route('/security_check', methods=['GET'])
def security_check():
    security_report = security_agent.analyze_contract()
    return jsonify({"security_report": security_report})

@app.route('/contract_balance', methods=['GET'])
def contract_balance():
    balance = dynamic_agent.get_contract_balance()
    return jsonify({"contract_balance": balance})

if __name__ == '__main__':
    print("[SERVEUR] API Flask en cours d'exécution sur le port 5001...")
    app.run(debug=True, port=5001)
