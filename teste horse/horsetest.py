from skimage.morphology import skeletonize, binary_erosion
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert
from skimage import data, img_as_float, io
# Read the image
image = io.imread('corp.jpeg', as_gray=True)

# Binarize the image
_, binary_image = 'corp.jpeg' (image, 0, 255, 'corp.jpeg'.THRESH_BINARY_INV + 'corp.jpeg'.THRESH_OTSU)

# Perform skeletonization
skeleton = skeletonize(binary_image)

# display results
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4), sharex=True, sharey=True)

ax = axes.ravel()

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].axis('off')
ax[0].set_title('original', fontsize=20)

ax[1].imshow(skeleton, cmap=plt.cm.gray)
ax[1].axis('off')
ax[1].set_title('skeleton', fontsize=20)

fig.tight_layout()
plt.show()