import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {'No attack':0.1, 'Gaussian noise':4.5, 'Compression':2.4,
		'Cropping':8.1, 'Rotation':7.2, 'Sharpening':10,'Darkening':0.7, 'Scaling':0.2, 'Salt&Pepper noise':3.3}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 6))

# creating the bar plot
plt.bar(courses, values, color ='maroon',
		width = 0.4, edgecolor ='grey')

plt.xlabel('Geometric Attacks', fontweight ='bold', fontsize = 12)
plt.ylabel('BER value (%)', fontweight ='bold', fontsize = 12)
plt.title("Kidney stone CT Scan image used as Cover image")
plt.show()
