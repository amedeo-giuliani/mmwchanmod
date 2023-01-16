import numpy as np
import matplotlib.pyplot as plt
import pickle
import os
import sys
import argparse

path = os.path.abspath('../..')
if not path in sys.path:
    sys.path.append(path)

print(sys.path)

"""
Parse arguments from command line
"""
parser = argparse.ArgumentParser(description='Trains the channel model')
parser.add_argument('--model_dir', action='store', default= '../../models/uav_boston', help='directory to store models')

args = parser.parse_args()
model_dir = args.model_dir

print('model dir =', model_dir)

loss_path = os.path.join(model_dir, 'path_train_hist.p')

with open(loss_path,'rb') as fp:
    train_loss = pickle.load(fp)

epochs = [e for e in range(len(train_loss['loss']))]

plt.figure()
plt.plot(epochs, train_loss['loss'], label='train loss')
plt.plot(epochs, train_loss['val_loss'], label='val loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()

# Write figure
plot_dir = '../../plots'
figure_name = 'train_val_loss_'+model_dir.split('_')[1]+'.png'

if not os.path.exists(plot_dir):
    os.mkdir(plot_dir)

plot_path = os.path.join(plot_dir, figure_name)
plt.savefig(plot_path, bbox_inches='tight')
print('figure saved to:', plot_path)
