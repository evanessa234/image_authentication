import numpy as np
import matplotlib.pyplot as plt


barWidth = 0.25
fig = plt.subplots(figsize =(10, 6))
 
# set height of bar
Watermark1 = [0.9992, 0.9991, 0.9994, 0.9995, 0.9991, 0.9992]
Watermark2 = [0.9978, 0.9974, 0.9984, 0.9983, 0.9979, 0.9977]
 
# Set position of bar on X axis
br1 = np.arange(len(Watermark1))
br2 = [x + barWidth for x in br1]

 
# Make the plot
plt.bar(br1, Watermark1, color ='maroon', width = barWidth,
        edgecolor ='grey', label ='Watermark1')
plt.bar(br2, Watermark2, color ='black', width = barWidth,
        edgecolor ='grey', label ='Watermark2')

# Adding Xticks
plt.xlabel('Medical images', fontweight ='bold', fontsize = 12)
plt.ylabel('SSIM value (db)', fontweight ='bold', fontsize = 12)
plt.xticks([r + barWidth for r in range(len(Watermark1))],
        ['Kidney Stone', 'Colon MRI', 'Head CT Scan', 'MRI Spine', 'X-RAY', 'Retinal Scan'])
 
plt.legend()
plt.show()