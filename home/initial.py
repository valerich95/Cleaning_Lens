import os
from .utils import *
from shutil import rmtree

def initial(model):
    if os.path.exists('img'):
        rmtree('img')
    if os.path.exists('reference'):
        rmtree('reference')
    #TODO add speech recognition algorithm
    # if not model.search_query:

    # save base image in reference directory
    # Todo save image if send byte
    if model.image_url:
        ref_img_data = image_to_json(model.image_url)
        json_to_image(directory='reference' , file_name='reference.jpg' , raw_data=ref_img_data)