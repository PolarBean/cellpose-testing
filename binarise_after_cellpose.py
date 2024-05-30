import cv2
import numpy as np
image_path = r"Y:\2021_Bjerke_DevMouse_projects\02_DERIVED_DATA\Test_sections_for_segmentation\calbindin_downscaled_04_autocropped\Original_downscaled_04_inverted/mouse137_P21_M_calb_s071_inverted_cp_masks.png"
image = cv2.imread(image_path, cv2.IMREAD_ANYDEPTH)
image = (image>0) * 255
image = np.array(image).astype(np.uint8)
out_path = image_path.split('.')[0] + "_binarised.png"
cv2.imwrite(out_path, image)
