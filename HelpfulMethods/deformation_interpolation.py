
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Interpolating Segmentations
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Tested in Slicer 5.0.3

import os
import sys
import time
import numpy as np
import ScreenCapture

class RespiratoryDeformation:
    def __init__(self, segmentation_file_path, transform_file_path):
        assert self.check_existence
        self.segmentation        = self.load_segmentation(segmentation_file_path)
        self.transform           = self.load_transform(transform_file_path)
        self.transform_mtx       = slicer.util.arrayFromGridTransform(self.transform)
        self.interpolation_value = None
    # 
    def check_existence():
        exists = True
        if not os.path.exists(segmentation_file_path):
            print("{} does not exist".format(segmentation_file_path))
            exists = False
        if not os.path.exists(transform_file_path):
            print("{} does not exist".format(transform_file_path))
            exists = False
        return exists
    # 
    def load_segmentation(self, segmentation_file_path):
        segmentation = slicer.util.loadSegmentation(segmentation_file_path)
        segmentation.CreateClosedSurfaceRepresentation()
        slicer.app.layoutManager().threeDWidget(0).threeDView().resetFocalPoint()
        return segmentation
    # 
    def load_transform(self, transform_file_path):
        return slicer.util.loadTransform(transform_file_path)
    # Note: hardening might slightly adjust the segmentation
    def harden_transform(self):
        slicer.vtkSlicerTransformLogic().hardenTransform(self.segmentation)
    # 
    def interpolate(self, interpolation_value):
        if interpolation_value > 1 or interpolation_value < 0:
            print("Interpolation value needs to be between 0 and 1")
            return
        # 
        if interpolation_value == 0:
            self.reset_interpolation()
        else:
            if self.interpolation_value is not None:
                self.reset_interpolation()
            self.interpolation_value = interpolation_value
            self.transform_mtx *= self.interpolation_value
            slicer.util.arrayFromGridTransformModified(self.transform)
            self.segmentation.SetAndObserveTransformNodeID(self.transform.GetID())
    # 
    def reset_interpolation(self):
        # reset the segmentation
        self.segmentation.SetAndObserveTransformNodeID(None)
        # 
        if self.interpolation_value is None:
            return
        # reset the transform
        self.transform_mtx = slicer.util.arrayFromGridTransform(self.transform)
        self.transform_mtx *= (1.0 / self.interpolation_value)
        slicer.util.arrayFromGridTransformModified(self.transform)
        self.interpolation_value = None
    # 
    def record_deformation(self, output_directory, outfile = "interp_{}.jpg", steps = 100):
        print("Generating deformation frames...")
        sys.stdout.flush()
        cap            = ScreenCapture.ScreenCaptureLogic()
        threeDViewNode = slicer.app.layoutManager().threeDWidget(0).threeDView().mrmlViewNode()
        threeDView     = cap.viewFromNode(threeDViewNode)
        #
        interpolation_values = np.linspace(0, 1, steps)
        cap.captureImageFromView(threeDView, "{}/{}".format(output_directory, outfile.format(0)))
        time.sleep(0.05)
        for i in range(1, steps):
            self.interpolate(interpolation_values[i])
            cap.captureImageFromView(threeDView, "{}/{}".format(output_directory, outfile.format(i+1)))
            time.sleep(0.05)
            self.reset_interpolation()
        print("Done")
        sys.stdout.flush()
        
    
# basedir: path to the data
def test(basedir):
    segmentation_file_path = "{}/EXACT09_Case1/BronchialTree_EXACT09_Case01_.nii.gz".format(basedir)
    transform_file_path    = "{}/EXACT09_Case1/Transform_EXACT09_Case01.h5".format(basedir)
    # 
    deform = RespiratoryDeformation(segmentation_file_path, transform_file_path)
    deform.interpolate(0.5)
    deform.reset_interpolation()
    # 
    outdir = "{}/InterpolationDemo".format(basedir)
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    deform.record_deformation(outdir)






