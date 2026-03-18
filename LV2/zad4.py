import numpy as np
import matplotlib.pyplot as plt

def sahovnica(velicina, broj_h, broj_w):
    # crni i bijeli kvadrat
    crni = np.zeros((velicina, velicina))
    bijeli = np.ones((velicina, velicina)) * 255

    redovi = []

    for i in range(broj_h):
        blokovi = []
        for j in range(broj_w):
            if (i + j) % 2 == 0:
                blokovi.append(bijeli)
            else:
                blokovi.append(crni)
        
        # spajanje po širini (horizontalno)
        red = np.hstack(blokovi)
        redovi.append(red)
    
    # spajanje po visini (vertikalno)
    img = np.vstack(redovi)
    
    return img


# primjer korištenja
img = sahovnica(50, 6, 8)

plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.axis('off')
plt.show()