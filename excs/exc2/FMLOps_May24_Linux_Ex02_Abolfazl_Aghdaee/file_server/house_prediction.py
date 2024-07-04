import joblib
import numpy as np 
model = joblib.load('house_price_model.pkl')
def predict_house_price():
    try:
        input_ = float(input('please enter your house size: '))
        result = model.predict(np.array([[input_]]))
        print(f'your house price is: {result}')


    except ValueError:
        print('please enter a valid number')
        predict_house_price()


predict_house_price()



