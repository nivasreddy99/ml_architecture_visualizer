 
# File: backend/app/services/simulator.py

import time

class Simulator:
    def __init__(self, neural_network, hardware_config):
        self.nn = neural_network
        self.hw = hardware_config
    
    def run_simulation(self, input_data, num_iterations):
        start_time = time.time()
        
        for _ in range(num_iterations):
            self.nn.forward(input_data)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        performance_score = self.hw.calculate_performance_score()
        adjusted_time = execution_time / performance_score
        
        return adjusted_time