# Add the path
import os
import sys
path = os.path.abspath('../..')
if not path in sys.path:
    sys.path.append(path)
from mmwchanmod.datasets.download import list_models, load_model

# Models to download
mod_names = ['uav_lon_tok', 'uav_boston', 'uav_moscow', 'uav_beijing']

# Downloads the datasets from the server, if needed
for mod in mod_names:
    load_model(mod, return_mod=False)

# Print list
list_models(src='local')