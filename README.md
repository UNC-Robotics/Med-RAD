# Medical Robotics Anatomical Dataset (Med-RAD)

## Overview

This repository contains anatomical environments as a resource for research into development and evaluation of medical robots.

## Contributing

This dataset is actively growing and we welcome any and all collaborations and contributions. Please [get in touch with us](mailto:med-rad-cs@cs.unc.edu) if you are interested in this work!

## Data

### Lungs :lungs:

#### Anatomical Models with Lung Nodules

There are five lungs environments from the Lung Image Database Consortium and Image Database Resource Initiative ([LIDC-IDRI][1]) (CC-BY 3.0) image collection from The Cancer Imaging Archive ([TCIA][2]). We segmented the bronchial tree, pleural boundary, and major vessels using an [automatic segmentation algorithm][3], and we segmented the nodules and lung fissures manually using [3D-Slicer][4]. 

[1]: <https://wiki.cancerimagingarchive.net/display/Public/LIDC-IDRI> "LIDC-IDRI"
[2]: <https://www.cancerimagingarchive.net/> "TCIA"
[3]: <https://github.com/UNC-Robotics/lung-segmentation> "LINK"
[4]: <https://www.slicer.org/> "3D-Slicer"

#### Anatomical Models with Respiratory Deformation

In addition, there are two lungs environments from the Extraction of Airways from CT 2009 ([EXACT'09][5]) study and one lungs environment from the [CT-vs-PET-Ventilating-Imaging][7] (CC-BY 4.0) study from TCIA. We segmented the bronchial tree, lung lobes, and blood vessels in 3D-Slicer. The three CT scans we selected are from study participants for whom there is both an expiratory and inspiratory CT scan. We used [Elastix][6] to perform a non-rigid registration between these respiratory states and include the resulting deformation field in the dataset to enable interpolation of respiratory deformation in the anatomy.

[5]: <http://image.diku.dk/exact/> "EXACT'09"
[6]: <https://github.com/lassoan/SlicerElastix>
[7]: <https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=125600096>

### Liver

There are five liver environments from the Hepatocellular Carcinoma Transarterial Chemoembolization Segmentation ([HCC-TACE-Seg][8]) (CC-BY 4.0) image collection from TCIA. Segmentations of the liver, cancer nodules, and blood vessels are provided as part of the data. We manually refined and expanded these segmentations using 3D-Slicer, as well as differentiated the vessels into the hepatic arteries, hepatic veins, and portal vein.

[8]: <https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=70230229> "HCC-TACE-Seg"

### Brain :brain:

There are five brain environments from the [Healthy MR Database][9]. We segmented the blood vessels manually using 3D-Slicer, and we used [FastSurfer][10] to segment the brain and all of the brain subregions.

[9]: <https://data.kitware.com/#collection/591086ee8d777f16d01e0724> "HMRD"
[10]: <https://www.sciencedirect.com/science/article/pii/S1053811920304985> "FS"

## Usage

Within each folder are segmentation files in .nii.gz format. These can easily be loaded in publicly-available software such as 3D Slicer and then converted or saved in other formats. [NiBabel](https://nipy.org/nibabel/) or [SimpleITK](https://pypi.org/project/SimpleITK/) are other convenient tools for working with these types of images. For each environment, there are text files with [RAS](https://www.slicer.org/wiki/Coordinate_systems) coordinates corresponding to the nodules and a set of 4x4 matrices for variable clinically-motivated start poses for the motion planning problem.

Inside `HelpfulMethods/` are a couple helpful functions for programmatically loading the data, converting betweeen RAS and IJK coordinates, and for visualizing the data.

We used Slicer version 5.0.3

## References

* Clark, Kenneth, et al. "The Cancer Imaging Archive (TCIA): maintaining and operating a public information repository." Journal of digital imaging 26.6 (2013): 1045-1057.

* Armato III, Samuel G., et al. "The lung image database consortium (LIDC) and image database resource initiative (IDRI): a completed reference database of lung nodules on CT scans." Medical physics 38.2 (2011): 915-931.

* Armato III, Samuel G., et al. Data From LIDC-IDRI [Data set]. (2015). The Cancer Imaging Archive.

* Morshid, Ali, et al. "A machine learning model to predict hepatocellular carcinoma response to transcatheter arterial chemoembolization." Radiology. Artificial intelligence 1.5 (2019).

* Bullitt E, Zeng D, Gerig G, Aylward S, Joshi S, Smith JK, Lin W, Ewend MG (2005) Vessel tortuosity and brain tumor malignancy: A blinded study. Academic Radiology 12:1232-1240.

* Henschel, Leonie, et al. "Fastsurfer-a fast and accurate deep learning based neuroimaging pipeline." NeuroImage 219 (2020): 117012.

* Eslick, Enid M., et al. "CT ventilation imaging derived from breath hold CT exhibits good regional accuracy with Galligas PET." Radiotherapy and Oncology 127.2 (2018): 267-273.

* Eslick, Enid M., et al. CT Ventilation as a functional imaging modality for lung cancer radiotherapy (CT-vs-PET-Ventilation-Imaging) (Version 1) [Data set]. (2022). The Cancer Imaging Archive.

## Acknowledgements

The authors acknowledge the National Cancer Institute and the Foundation for the National Institutes of Health, and their critical role in the creation of the free publicly available LIDC/IDRI Database used in this study.

The MR brain images from healthy volunteers used in this work were collected and made available by the CASILab at The University of North Carolina at Chapel Hill and were distributed by the MIDAS Data Server at Kitware, Inc.

We thank the organizers of the Extraction of Airways from CT 2009 (EXACT09) study for their efforts in establishing the original study and for giving us permission to share the segmentations we generated using EXACT09 images.

## Citation

If you found our work useful in your work, please consider citing our abstract(s):

```
@inproceedings{fried2023dataset,
  title={A Dataset of Anatomical Environments for Medical Robots: Modeling Respiratory Deformation},
  author={Fried, Inbar and Hoelscher, Janine and Akulian, A Jason and Alterovitz, Ron},
  booktitle={IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) Workshop on Data vs Model in Medical Robotics},
  journal={arXiv preprint arXiv:2310.04289},
  year={2023}
}
```

```
@inproceedings{fried2022clinical,
  title={A Clinical Dataset for the Evaluation of Motion Planners in Medical Applications},
  author={Fried, Inbar and Akulian, A Jason and Alterovitz, Ron},
  booktitle={IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) Workshop on Evaluating Motion Planning Performance},
  journal={arXiv preprint arXiv:2210.10834},
  year={2022}
}
```

The abstracts for the citations can be found [here (IROS2023)](https://arxiv.org/abs/2310.04289) and [here (IROS2022)](https://arxiv.org/abs/2210.10834) (an earlier version of this dataset).

## License

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License ([CC BY-NC-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/)).

Any use of this work must also abide by the [terms](https://wiki.cancerimagingarchive.net/display/Public/Data+Usage+Policies+and+Restrictions) set by the TCIA.


