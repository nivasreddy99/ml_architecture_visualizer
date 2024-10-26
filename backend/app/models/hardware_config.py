 
# File: backend/app/models/hardware_config.py

class HardwareConfig:
    def __init__(self, cpu_cores, ram_gb, gpu_cores):
        self.cpu_cores = cpu_cores
        self.ram_gb = ram_gb
        self.gpu_cores = gpu_cores
    
    def calculate_performance_score(self):
        return (self.cpu_cores * 0.3 + self.ram_gb * 0.2 + self.gpu_cores * 0.5) / 100