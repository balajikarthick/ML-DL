import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    #print (glob.glob(path + '/*.xml'))
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot() 
        image_path = xml_file.rsplit('/', 1)[1]
        image_path = image_path.rstrip('.xml')
        root.find('filename').text = image_path + '.png'
        print(root.find('filename').text)
        tree.write(xml_file)

def main():
    for folder in ['train']:
        image_path = os.path.join(os.getcwd(), ('images/' + folder))
        #print (image_path)
        xml_to_csv(image_path)
        
main()
