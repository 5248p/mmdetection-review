import os
from PIL import Image # to read image
import glob
import json

jpg_containing_folder = []
json_container = []

def search_container(top_folder):
    temp = 0
    temp1 = 0
    try:
        file_name = sorted(os.listdir(top_folder))
        for i in file_name:
            full_name = os.path.join(top_folder, i)
            if os.path.isdir(full_name):
                search_container(full_name)
            else:
                jpg_seartch = os.path.splitext(full_name)[-1]
                if jpg_seartch == '.jpg':
                    jpg_containing_folder.insert(temp ,top_folder)
                    temp += 1
                    break
                elif jpg_seartch == '.json':
                    json_container.insert(temp1, full_name)
                    temp += 1
                                        
    except PermissionError:
        pass
#----------------------------------------------------------
def launch(json_containers, jpg_containing_folders):
    for i in json_containers:
        split_json = os.path.splitext(i)[0]
        split_json = os.path.split(split_json)[1]
        split_json = os.path.splitext(split_json)[0]

        for j in jpg_containing_folders:
            if split_json in j:
                root_images = j + '/*.jpg'
                json_path = i

                list_image = sorted(glob.glob(root_images))
                list_bbox = []
                with open(json_path, encoding='utf-8-sig') as f:
                    json_data = json.load(f)

                for i, j in enumerate(json_data['annotations']):
                    x = j['bounding_box']['x'] 
                    y = j['bounding_box']['y']
                    width = j['bounding_box']['width']
                    height = j['bounding_box']['height']
                    list_bbox.insert(i, [x, y, x+width, y+height])

                for i, j in zip(list_image, list_bbox):
                    try:
                        img = Image.open(i)
                        cropped_image = img.crop(j)
                        cropped_image.save(i, 'JPEG')
                        print(i)
                    except:
                        continue
#----------------------------------------------------------




#==========제일 바깥쪽 폴더=============
search_container('/home/pkn/data/')
#======================================
launch(json_container, jpg_containing_folder)

