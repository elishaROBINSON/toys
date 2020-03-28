import argparse
import os
import sys
import hashlib 
 
parser = argparse.ArgumentParser(description="""
        delete duplicate files present in 
        the given directory also removes any empty directories
        this operation is extremly dangerous do not run in root
        and please do not run it for any application
        """)
parser.add_argument('--folder', 
                   help='folder of duplicate files to be deleted')
folder_path = parser.parse_args().folder

if not os.path.isdir(folder_path):
    print("please enter a valid folder path")
    sys.exit()

hash_list = []
for root, dirs, files in os.walk(folder_path):
    for name in files:
        file_path = os.path.join(root, name)
        file_hash = hashlib.md5(open(file_path,'rb').read()).digest()
        if file_hash in hash_list:
            os.remove(file_path)
        else:
            hash_list.append(file_hash)

for root, dirs, files in os.walk(folder_path):
    for folder in dirs:
        folder = os.path.join(root, folder)
        if not os.listdir(folder) :
            os.removedirs(folder)




