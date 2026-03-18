import numpy as np
import matplotlib.pyplot as plt
img = plt.imread("tiger.png")
img = img[:,:,1].copy()

if img.max() <= 1.0:
    img = (img * 255).astype(np.uint8)

#Posvijetli
img = np.clip(img +20,0,255)
#Rotiraj
img = np.rot90(img,k=3)
#Zrcali
img= np.flip(img)

#Smanji rezoluciju
faktor = 10
img = img[::faktor, ::faktor]

# e) druga četvrtina po širini (ostalo crno)
h, w = img.shape
quarter = np.zeros_like(img)
start = w // 4
end = w // 2
quarter[:, start:end] = img[:, start:end]

plt.figure()
plt.imshow(quarter, cmap="gray")
plt.show()

