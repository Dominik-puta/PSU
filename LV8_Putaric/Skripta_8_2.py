import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.transform import resize
from skimage import color
from tensorflow.keras import models
import numpy as np

filename = 'test.png'

# Učitaj sliku
img_original = mpimg.imread(filename)

# Pretvori u grayscale
img = color.rgb2gray(img_original)

# Promjena dimenzije na 28x28
img = resize(img, (28, 28))

# Prikaz slike
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.axis('off')
plt.show()


# Priprema slike za mrežu
img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')

# Učitavanje istrenirane mreže
model = models.load_model('best_model.keras')

# Predikcija
prediction = model.predict(img)

# Klasa s najvećom vjerojatnošću
predicted_class = np.argmax(prediction)


# Ispis rezultata
print("Predikcija mreže:", predicted_class)

print("\nVjerojatnosti po klasama:")
for i, p in enumerate(prediction[0]):
    print(f"Znamenka {i}: {p:.4f}")