 
# File: backend/app/routes.py

from flask import jsonify, request
from app import app
from app.models.neural_network import NeuralNetwork
from app.models.hardware_config import HardwareConfig
from app.services.simulator import Simulator
import numpy as np

@app.route('/api/simulate', methods=['POST'])
def simulate():
    data = request.json
    nn = NeuralNetwork(data['input_size'], data['hidden_size'], data['output_size'])
    hw = HardwareConfig(data['cpu_cores'], data['ram_gb'], data['gpu_cores'])
    simulator = Simulator(nn, hw)
    
    input_data = np.random.rand(data['input_size'], 1)
    result = simulator.run_simulation(input_data, data['num_iterations'])
    
    return jsonify({
        'execution_time': result,
        'performance_score': hw.calculate_performance_score()
    })