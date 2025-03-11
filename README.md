This is a basic guide of some things that we have learned from testing CellPose.
1. First we need to train on chunks
    * To create these chunks we run img-chunker.py, we noticed that the nuclei model performs best if the chunks are inverted
    * we then load a selection of these chunks and manually label cells
    * The model is then trained on these
  
   **There is a bug in CellPose for models using the a finetuned nuclei model. I describe it here and how to fix it https://github.com/MouseLand/cellpose/issues/900**
      In short to fix the above bug just change the default diam_mean in the __init__ function of CPNet to 17.0
3. Next we deploy the trained model on the full images
   * for the moment the full images are crashing my machine, so we will need to run on a larger machine
   * For now we can somewhat downsample the images using img-chunker-big.py
   * To deploy the trained model on one image running the following command

    ```bash
    python -m cellpose --image_path /run/media/harryc/4TB_external_NTFS/linux-backup/Github/img-cropper/ext-d000009_PVMouse_81265_Samp1__s023_quadrants/chunk_15470_18564.tif --no_resample --pretrained_model nuclei --save_png  --verbose --save_tif --diameter 0
    ```
    If we want to run on a directory simply replace the image_path argument with --dir and point it towards a full directory
