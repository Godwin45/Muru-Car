import joblib 
import numpy as np
import pandas as pd
from pathlib import Path



class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/best_model.joblib'))

    
    def predict(self, data):
        prediction = self.model.predict(data)
        if prediction == 0:
            return "Great Condition"
        elif prediction == 1:
            return "Maintenance"
        else:
            return "Unknown"  # Handle other cases if needed
