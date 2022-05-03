import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {'No attack':0.99, 'Gaussian noise':0.79, 'Compression':0.94,
		'Cropping':0.59, 'Rotation':0.62, 'Sharpening':0.47,'Darkening':0.99, 'Scaling':0.99, 'Salt&Pepper noise':0.77}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 6))

# creating the bar plot
plt.bar(courses, values, color ='maroon',
		width = 0.4, edgecolor ='grey')

plt.xlabel('Geometric Attacks', fontweight ='bold', fontsize = 12)
plt.ylabel('NCC value(db)', fontweight ='bold', fontsize = 12)
plt.title("Kidney stone CT Scan image used as Cover image")
plt.show()
