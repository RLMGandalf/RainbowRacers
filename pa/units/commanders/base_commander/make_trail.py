import json
import os
import collections
import copy

def load(path):    
    if os.path.exists(path):
        return json.load(open(path), object_pairs_hook=collections.OrderedDict)
    else: 
        return None

def save(obj, path):    
    json.dump(obj, open(path, 'w'))


base_trail = {"emitters": []}

left_line = {
      "spec": {
        "shader": "particle_transparent_lit",
        "shape": "string",
        "sizeX": [[0, 1], [1, 0.2]],
        "red": 20,
        "green": 20,
        "blue": 20,
        "cameraPush": 2,
        "baseTexture": "/pa/effects/textures/particles/flat.papa"
      },
      "offsetX": 1,
      "offsetY": 1,
      "useWorldSpace": True,
      "alpha": [[0.7, 1 ], [2.65, 0 ]],
      "sizeX": 0.1,
      "velocityZ": 1,
      "velocityY": 1,
      "velocity": 30,
      "velocityRange" : 30,
      "drag": 0.9,
      "gravity": -10,
      "lifetime": 3.0,
      "lifetimeRange": 0.25,
      "emissionRate": 600,
      "killOnDeactivate": False,
      "endDistance": 2000,
      "useArmyColor": 1
    }

right_line = copy.deepcopy(left_line)
right_line['offsetX'] = -left_line['offsetX']

base_trail['emitters'].append(left_line)
base_trail['emitters'].append(right_line)


print json.dumps(base_trail)
save(base_trail, 'rainbow_trail.json')
