from mmwchanmod.datasets.download import get_dataset

ds_name = 'uav_boston'

# Load the data
data = get_dataset(ds_name)
cfg = data['cfg']
train_data = data['train_data'] 
test_data = data['test_data']

print(data.keys())
print(train_data.keys()) # data set does not contains coordinates, but only distances between tx and rx
print(train_data['dvec'])
print(train_data['los_ang'].shape) # 1 LOS path
print(train_data['nlos_ang'].shape) # 20 NLOS paths
print(train_data['nlos_dly'].shape)
print(train_data['nlos_pl'])
print(train_data['link_state'].shape)
print(cfg)