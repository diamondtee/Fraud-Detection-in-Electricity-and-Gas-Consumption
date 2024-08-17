import numpy as np
import joblib
from joblib import load


model = joblib.load('fraud_detection_model.joblib')


def prediction(District,client_catg	,region	,tarif_type,counter_number,	counter_code,
               	reading_remarque, counter_coefficient, consommation_level_1,	
               consommation_level_2, consommation_level_3, consommation_level_4, old_index, new_index, months_number, counter_type):
    
    prediction = model.predict(np.array([[District,	client_catg	,region	,tarif_type, counter_number, counter_code,
               	reading_remarque, counter_coefficient, consommation_level_1,	
               consommation_level_2, consommation_level_3, consommation_level_4, old_index, new_index, months_number, counter_type]]))
    return prediction