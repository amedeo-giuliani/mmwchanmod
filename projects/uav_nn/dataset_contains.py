from mmwchanmod.datasets.download import get_dataset

ds_name = 'uav_lon_bos'

# Load the data
data = get_dataset(ds_name)
cfg = data['cfg']
train_data = data['train_data'] 
test_data = data['test_data']

print(data.keys())
print(train_data.keys()) # data set does not contains coordinates, but only distance ìs between tx and rx
print(train_data['nlos_ang'].shape) # 1 LOS path
print(train_data['nlos_ang'].shape) # 20 NLOS paths