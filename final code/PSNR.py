import numpy as np
import matplotlib.pyplot as plt



barWidth = 0.25
fig = plt.subplots(figsize =(10, 6))
 
# set height of bar
Watermark1 = [60.47, 57.91, 59.69, 60.42, 57.86, 59.36]
Watermark2 = [56.39, 55.53, 55.46, 55.65, 54.48, 55.08]
 
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
plt.ylabel('PSNR value (db)', fontweight ='bold', fontsize = 12)
plt.xticks([r + barWidth for r in range(len(Watermark1))],
        ['Kidney Stone', 'Colon MRI', 'Head CT Scan', 'MRI Spine', 'X-RAY', 'Retinal Scan'])
 
plt.legend()
plt.show()