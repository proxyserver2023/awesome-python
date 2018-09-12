import os
import glob

path = os.path.dirname(os.path.abspath(__file__))
print(path)

os.chdir(os.path.join(path, "files"))
for file in glob.glob("*.json"):
    #print(file)
    file_name, extension = os.path.splitext(file)
    new_file_name = file_name[:-6] + extension # no logic 
    try:
        os.rename(file, new_file_name)
    except OSError as e:
        print(e)
    else:
        print("Renamed {} to {}".format(file, new_file_name))
    print(new_file_name, extension)