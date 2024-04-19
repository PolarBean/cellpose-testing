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
    image_filename= image.split(".")[0].split("\\")[-1]
    
    # Read the image
    img = tiff.imread(image)
            # Get the shape of the image
#    shape = img.shape
            #Get the chunk size
#    chunk_size = 512
    img = np.invert(img)
    tiff.imwrite((image_filename + "_inverted.tif"), img)

    print("Image " + image_filename + " is inverted.")
print("Job finished")


        



    