import os, glob
path = 'C:\\Users\\Joshua\\Desktop\\pyscripts\\flash_cards\\results'
for filename in glob.glob(os.path.join(path, '*.json')):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
      for i in range(3):
         print(f.read())
         

