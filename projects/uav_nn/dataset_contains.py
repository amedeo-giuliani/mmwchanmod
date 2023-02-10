from mmwchanmod.datasets.download import get_dataset
import matplotlib.pyplot as plt

ds_name = 'uav_boston'

# Load the data
data = get_dataset(ds_name)
cfg = data['cfg']
train_data = data['train_data'] 
test_data = data['test_data']

print(data.keys())
print(train_data.keys()) # data set does not contains coordinates, but only distances between tx and rx
print(train_data['nlos_pl'])
print(cfg)