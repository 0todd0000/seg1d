[![DOI](https://joss.theoj.org/papers/10.21105/joss.02404/status.svg)](https://doi.org/10.21105/joss.02404)

# seg1d

Automated segmentation of one-dimensional (1D) data


## Overview

seg1d is an open-source Python package for the automated segmentation of one-dimensional data using one or more reference segments. The segmentation process allows users to apply various methods and parameters for the process through weighted features (i.e., additional data attributed to the same set) in a rolling correlation size-varying window of a reference(s) to a target. Correlations can be averaged across the references and a peak detection algorithm finds the most prominent segments. Non-overlapping segments are identified and a clustering algorithm groups the most similar segments within the target. The package was developed for movement sciences but should be useful to anyone interested in extracting correlated subsequences from a dataset. 

![seg1d](https://raw.githubusercontent.com/cadop/seg1d/master/docs/build/plot_directive/api_basic-1.png)

Example of the segmentation algorithm using a portion of a sine wave. The initial reference segment is found, along with any additional segments. 

### Documentation

Full documentation available online: https://cadop.github.io/seg1d/


### Alternatives

There are existing libraries that provide clustering and similarity measures for querying subseries data. 

  * [The UCR Suite](https://www.cs.ucr.edu/~eamonn/UCRsuite.html) (Ultrafast subsequence search under both Dynamic Time Warping (DTW) and Euclidean Distance (ED))

  * [tslearn](https://github.com/rtavenar/tslearn)(Machine learning tools for the analysis of time series)
  
  * [seglearn](https://dmbee.github.io/seglearn/)(Provides a flexible approach to multivariate time series and related contextual (meta) data for classification, regression, and forecasting problems)

The advantage of seg1d is a simpler API which makes getting started and using the code quicker for non-experts when interested in purely extracting timestamps (segments) from a dataset. The API was built with motion capture data in mind, making the addition of features (e.g., marker trajectories) and sets of features (e.g., multiple subjects) easy. The output of seg1d is also geared towards users that are interested in comparing the segments found, such as returning masked arrays of segments. 


## Quickstart 


### Minimum Dependencies

Currently tested on ``Python 3.8`` on Ubuntu 18.04 and Windows 10. (Should work on ``Python 3.6`` and above)

Required Packages:

``numpy>=1.15``, ``scipy>=1.0.0``, ``sklearn>=0.2``, ``numba>=0.40``

For documentation:

``sphinx>=2``, ``numpydoc>=0.9.2``

For examples:

``matplotlib>=3.2.0``

### Installation

```pip install seg1d```


### Example usage

The documentation contains examples using data of both generated data (e.g., sine wave) and real-world examples (i.e., motion capture data). 

To quickly get started, try importing the seg1d module and using the provided sample data. 

```python

import seg1d 

#retrieve the sample reference, target, and weight data
r,t,w = seg1d.sampleData()
# define scaling percentage and rolling step size
minW, maxW, step  = 70, 150, 1 
#call the segmentation algorithm
a = seg1d.segment_data(r,t,w,minW,maxW,step)
print(a)
# Should output an array equal to:
# array([[207.       , 240.       ,   0.9124224],
#        [342.       , 381.       ,   0.8801901],
#        [ 72.       , 112.       ,   0.8776795]])
# where each array is of form [start index, end index, correlation]

```

For more examples, please refer to the full documention. 

## Project Info

To cite: 
Schwartz et al., (2020). seg1d: A Python package for Automated segmentation of one-dimensional (1D) data. Journal of Open Source Software, 5(52), 2404, https://doi.org/10.21105/joss.02404

Bibtex
```
@article{Schwartz2020,
  doi = {10.21105/joss.02404},
  url = {https://doi.org/10.21105/joss.02404},
  year = {2020},
  publisher = {The Open Journal},
  volume = {5},
  number = {52},
  pages = {2404},
  author = {Mathew Schwartz and Todd C. Pataky and Cyril J. Donnelly},
  title = {seg1d: A Python package for Automated segmentation of one-dimensional (1D) data},
  journal = {Journal of Open Source Software}
}
```

This project was used for the following paper -  [Paper Link](https://commons.nmu.edu/isbs/vol38/iss1/231/) : 

Schwartz, Mathew; Pataky, Todd; Sui Geok Karen, CHUA; Wei Tech, ANG; and Donnelly, Cyril (2020) "AUTOMATED MULTI-FEATURE SEGMENTATION OF TREADMILL RUNNING," ISBS Proceedings Archive: Vol. 38 : Iss. 1 , Article 231.

### Community

Issues and feature requests should be submitted on [github](https://github.com/cadop/seg1d/issues). 

Please check the Community Guidelines for further details on contributing. 


### Credits

Code written and developed by Mathew Schwartz (New Jersey Institute of Technology).

Data used in sample provided by Precision Rehab, Rehabilitation Research Institute of Singapore.

Project was funded in part by the Agency for Science, Technology and Research (A\*STAR), Nanyang Technological University (NTU) and the National Health Group (NHG) (RRG3: 2019/19002).

### License

Please refer to the full [LICENSE](https://github.com/cadop/seg1d/blob/master/LICENSE.txt).
