from tensorflow import keras
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np

# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normalizacija i prilagodba dimenzija
x_train_s = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test_s = x_test.reshape(-1, 28, 28, 1) / 255.0

# One-hot encoding oznaka
y_train_s = to_categorical(y_train, num_classes=10)
y_test_s = to_categorical(y_test, num_classes=10)

model = models.Sequential()

# Ulazni sloj + Conv blok 1
model.add(layers.Conv2D(32, (3, 3),
                        activation='relu',
                        padding='same',
                        input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))

# Conv blok 2
model.add(layers.Conv2D(64, (3, 3),
                        activation='relu',
                        padding='same'))
model.add(layers.MaxPooling2D((2, 2)))

# Conv blok 3
model.add(layers.Conv2D(128, (3, 3),
                        activation='relu',
                        padding='same'))

# Potpuno povezani dio
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dropout(0.5))

# Izlazni sloj
model.add(layers.Dense(10, activation='softmax'))

# Prikaz arhitekture mreže
model.summary()

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# TensorBoard callback
tensorboard_cb = callbacks.TensorBoard(
    log_dir='logs',
    histogram_freq=1
)

# Spremanje najboljeg modela
checkpoint_cb = callbacks.ModelCheckpoint(
    filepath='best_model.keras',
    monitor='val_accuracy',
    save_best_only=True,
    mode='max',
    verbose=1
)
history = model.fit(
    x_train_s,
    y_train_s,
    epochs=10,
    batch_size=128,
    validation_split=0.1,   # 10% za validaciju
    callbacks=[tensorboard_cb, checkpoint_cb]
)

best_model = keras.models.load_model('best_model.keras')


# Predikcije
y_train_pred = np.argmax(best_model.predict(x_train_s), axis=1)
y_test_pred = np.argmax(best_model.predict(x_test_s), axis=1)

# Točnost
train_acc = accuracy_score(y_train, y_train_pred)
test_acc = accuracy_score(y_test, y_test_pred)

print(f"\nTočnost na skupu za učenje: {train_acc:.4f}")
print(f"Točnost na testnom skupu: {test_acc:.4f}")

cm_train = confusion_matrix(y_train, y_train_pred)
cm_test = confusion_matrix(y_test, y_test_pred)

print("\nMatrica zabune - TRAIN:")
print(cm_train)

print("\nMatrica zabune - TEST:")
print(cm_test)