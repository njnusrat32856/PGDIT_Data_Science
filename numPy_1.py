import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

arr = np.array([10, 20, 30, 40, 50, 60])

# Create Boolean array
bool_idx = arr > 30

# Print Boolean array
print("Boolean Index:", bool_idx)

# Filter using Boolean indexing
filtered = arr[bool_idx]
print("Filtered Array:", filtered)

# Or do it in one step
print("Filtered in one step:", arr[arr > 30])


arr = np.array([10, 20, 30, 40, 50, 60])
bool_index = arr > 30
print(bool_index)


# Image convert:
image_path = 'images.jpg'

img = Image.open(image_path).convert('RGB')
img_np = np.array(img)

gray = np.dot(img_np[:, :, :3], [0.2989, 0.5870, 0.1140])
print(gray.shape, img_np.shape)
plt.figure(figsize=(10,4))

plt.subplot(1, 2, 1)
plt.title("Orginal Image")
plt.imshow(img_np)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Grayscale Image(NumPy)') 
plt.imshow(gray, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

