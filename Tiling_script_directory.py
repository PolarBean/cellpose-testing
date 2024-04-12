import os
import sys
import numpy as np
import tifffile as tiff
import glob

#path_to_file = r"Y:\2021_Bjerke_DevMouse_projects\02_DERIVED_DATA\Test_sections_for_segmentation\calbindin_downscaled_04_autocropped\mouse192_P35_M_calb_s095.tif"
folder_dir = r"Y:\2021_Bjerke_DevMouse_projects\02_DERIVED_DATA\Test_sections_for_segmentation\calbindin_downscaled_04_autocropped"

# script for tiling all tif images in a directory from path to directory
list_files = []

for images in os.listdir(folder_dir):
    if (images.endswith("tif")):
        list_files.append(os.path.join(folder_dir, images))

for image in list_files:
    image_outdir = image.split(".")[0].split("/")[-1]
    if not os.path.exists(image_outdir):
        os.makedirs(image_outdir)
    
    # Read the image
    img = tiff.imread(image)
            # Get the shape of the image
    shape = img.shape
            #Get the chunk size
    chunk_size = 512
    img = np.invert(img)
            #crop the image and save each chunk
    for i in range(0, shape[0], chunk_size):
        for j in range(0, shape[1], chunk_size):
            chunk = img[i:i+chunk_size, j:j+chunk_size]
            tiff.imsave("{}/chunk_{}_{}.tif".format(image_outdir,i, j), chunk)
    print("Image " + image_outdir + " is tiled.")
print("Job finished")


        



    