import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# učitaj sliku
image = mpimg.imread('example.png')

# reshape u (broj_piksela, 3)
X = image.reshape((-1, 3))
klasteri = 10

kmeans = KMeans(n_clusters=klasteri, n_init=10, random_state=0)
kmeans.fit(X)

centers = kmeans.cluster_centers_
labels = kmeans.labels_

# zamjena svakog piksela njegovim centroidom
image_compressed = centers[labels]
# vrati originalni oblik
image_compressed = image_compressed.reshape(image.shape)
# ako je tip float (0–1), sve je ok; ako je 0–255:
image_compressed = np.clip(image_compressed, 0, 1)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(image)
plt.title("Original")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(image_compressed)
plt.title("Kvantizirana (K="+str(klasteri)+ ")")
plt.axis('off')

plt.show()