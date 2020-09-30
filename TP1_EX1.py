import os
import pandas as pd
import matplotlib.pyplot as plt

prefix = os.path.join('..', 'DATASETS')

pima_indians_dataset = os.path.join(prefix, 'pima-indians-diabetes.data')
iris_plant_dataset = os.path.join(prefix, 'iris_proc.data')
churn_modelling_dataset = os.path.join(prefix, 'Churn_Modelling.csv')
social_network_dataset = os.path.join(prefix, 'Social_Network_Ads.csv')

pima_indians_data = pd.read_csv(pima_indians_dataset)
iris_plant_data = pd.read_csv(iris_plant_dataset)
churn_modelling_data = pd.read_csv(churn_modelling_dataset)
social_network_data = pd.read_csv(social_network_dataset)


print(pima_indians_data, pima_indians_data.shape)
print(iris_plant_data, iris_plant_data.shape)
print(churn_modelling_data, churn_modelling_data.shape)
print(social_network_data, social_network_data.shape)

# pima_indians_data.plot().show()
