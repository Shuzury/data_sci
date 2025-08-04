import matplotlib.image as mpimg
import matplotlib.pyplot as plt
img= mpimg.imread('matplotlib/max.jpg')  
print(img)  
plt.imshow(img)
plt.axis('off')  # Hide the axes
cropped_img = img[50:200, 100:300]  # crop: rows 50-200, cols 100-300
plt.imshow(cropped_img)
plt.axis('off')