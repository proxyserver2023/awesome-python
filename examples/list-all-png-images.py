import os, glob


dir_name = input('Enter the directory you want to searh for png images\n')

os.chdir(dir_name)

for file in glob.glob('*.png'):
    print(file)
