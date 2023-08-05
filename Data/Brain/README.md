# Overview

The corresponding patient identifier in the Healthy MR Database for each patient is:
* Patient1 - Normal_001
* Patient2 - Normal_003 (environment used in paper figure)
* Patient3 - Normal_005
* Patient4 - Normal_027
* Patient5 - Normal_035

The blood vessel segmentations are created using the Magnetic Resonance Angiograpy (MRA) images while the rest of the segmentations are created using the T1-Flash images. We register the blood vessels to the coordinate space of the T1 image using the Elastix registration toolkit in 3D Slicer ([LINK](https://lassoan.github.io/SlicerSegmentationRecipes/VesselSegmentationBySubtraction/)).

The targets in these environments are the globi pallidi in the setting of deep brain stimulation (DBS).

