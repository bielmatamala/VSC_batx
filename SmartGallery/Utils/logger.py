import os 
from datetime import datetime

# Module per gestionar els logs de l'aplicació
class Logger:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # carpeta SmartGallery
        self.log_dir = os.path.join(base_dir, "logs")
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file = os.path.join(self.log_dir, "run_log.txt")
    
    def timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def log (self, action, filename = "", result = "", extra = ""):
        #guarda un regitre del que fa el porgrama en un fitxer de text
        line = f"[{self.timestamp()}] {action} | {filename} | {result} {extra}\n"
        with open(self.log_file, "a", encoding = "utf-8") as f:
            f.write(line)