# **Finding Lane Lines on the Road** 

## Writeup
---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report
---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

Current Pipeline:
    
1) Mask out everything excluding Lane Lines
2) Crop out the Region of Interest
3) Apply Canny Edge Detection
4) Compute the Hough Lines
5) Filter out and differentiate lines
6) Compute 2 main lines
7) Average main lines over previous frames
8) Overlay Lines and Lane over original input


(see Jupyter Notebook for more details on pipeline)

### 2. Identify potential shortcomings with your current pipeline

The current pipeline works great for detecting straight, or slightly curved lanes. It handled the challenge video extremely well, mainly due to the smoothing caused by the interframe averaging. However, this is not good for use in the real world. The program doesn't account for curvature, and the lane filtering method does not work well with sharp turns.


### 3. Suggest possible improvements to your pipeline

 We can try doing a sliding window algorithm to produce a curve for curved lanes, which would detect lanes much more accurately. Another improvement that could improve accuracy would be detection of vehicles and adjacent lanes, which would allow for the car to localize itself better.

