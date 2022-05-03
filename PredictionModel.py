from joblib import load
import random

class Model:

    def __init__(self):
        # self.model = load("assets/modelo.pkl")
        pass

    def make_predictions(self, data):
        # result = self.model.predict(data)
        random.seed()
        result = random.randint(0,100);
        return result
