from keras.preprocessing.image import ImageDataGenerator
from keras import layers, models
from keras.models import load_model
import tensorflow as tf

train_datagen = ImageDataGenerator(rescale=1./255,
                                   rotation_range=40,
                                   width_shift_range=0.2,
                                   height_shift_range=0.2,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

train_dir = 'train'

validation_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(200,200),
    batch_size=2,
    class_mode='categorical'
)

original_model = load_model('../rede_neural.h5')


model = models.Sequential()
model.add(layers.Conv2D(64, (3,3), activation='relu', input_shape=(200, 200, 3)))
model.add(layers.MaxPooling2D(2))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation = 'relu'))
model.add(layers.Dense(26, activation='softmax'))


model.layers[1].set_weights(original_model.layers[1].get_weights())


BASE_LEARNING_RATE = 0.0001
model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=BASE_LEARNING_RATE),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

model.summary()

history = model.fit_generator(
      train_generator,
      epochs=3,
      verbose=2)

model.save('recalib.h5')