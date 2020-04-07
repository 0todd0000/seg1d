import seg1d
import numpy as np
import matplotlib.pylab as plt

# Then we generate some data

x = np.linspace(-np.pi*2, np.pi*2, 2000) #create an array of data
targ = np.sin(x)  # target data from a sin function 
t_s,t_e = 200,400 # define a sub-series

# To assign the data to the Segmenter, first we create an instance of it and then
# use the ``setTarget()`` and ``addReference()`` methods.

S = seg1d.Segmenter()  # instance of the segmenter
S.minW, S.maxW, S.step = 98, 105, 1  # scaling parameters
S.setTarget(targ) # set target and reference data
S.addReference(targ[t_s:t_e])
segments = S.segment() # run segmentation algorithm
np.around(segments, decimals=7)
# array([[2.000000e+02, 4.000000e+02, 1.000000e+00],
# [1.200000e+03, 1.398000e+03, 9.999999e-01]])

# Using matplotlib we can visualize the results

plt.figure(figsize=(10,3)) #doctest: +SKIP
#plot the full sine wave
plt.plot(x, targ,linewidth=8,alpha=0.2,label='Target') #doctest: +SKIP
#plot the original reference segment
plt.plot(x[t_s:t_e], targ[t_s:t_e],linewidth=6,alpha=0.7,label='Reference') #doctest: +SKIP
# >>>
#plot all segments found
for s,e,c in segments:
    plt.plot(x[s:e], targ[s:e],dashes=[1,1],linewidth=4,alpha=0.8,label='Segment') #doctest: +SKIP
plt.legend() #doctest: +SKIP
plt.show() #doctest: +SKIP