import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# učitaj sliku
imageNew = mpimg.imread('example_grayscale.png')

# pretvori u vektor (n_uzoraka, 1)
X = imageNew.reshape((-1, 1))

kmeans = KMeans(n_clusters=20, n_init=10, random_state=0)
kmeans.fit(X)

values = kmeans.cluster_centers_.squeeze()
labels = kmeans.labels_

# rekonstrukcija slike
image_compressed = np.choose(labels, values)
image_compressed = image_compressed.reshape(imageNew.shape)

plt.figure()
plt.title("Original")
plt.imshow(imageNew, cmap='gray')
plt.axis('off')

plt.figure()
plt.title("Kvantizirana slika")
plt.imshow(image_compressed, cmap='gray')
plt.axis('off')

plt.show()