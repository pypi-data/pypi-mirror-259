import warnings
warnings.simplefilter('ignore')
import numpy as np
import os
import matplotlib.pyplot as plt
import tensorflow as tf
print(f"tensorflow version: {tf.__version__}")
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input,Conv2DTranspose,BatchNormalization,ReLU,Conv2D,LeakyReLU
import time

import keras

from IPython import display
import skillsnetwork
print(f"skillsnetwork version: {skillsnetwork.__version__}")

import matplotlib.pyplot as plt
#%matplotlib inline

import os
from os import listdir
from pathlib import Path
import imghdr

from tqdm import tqdm


# This function will allow us to easily plot data taking in x values, y values, and a title
def plot_distribution(real_data, generated_data, discriminator=None, density=True):
    plt.hist(real_data.numpy(), 100, density=density, facecolor='g', alpha=0.75, label='real data')
    plt.hist(generated_data.numpy(), 100, density=density, facecolor='r', alpha=0.75, label='generated data q(z) ')

    if discriminator:
        max_ = np.max([int(real_data.numpy().max()), int(generated_data.numpy().max())])
        min_ = np.min([int(real_data.numpy().min()), int(generated_data.numpy().min())])
        x = np.linspace(min_, max_, 1000).reshape(-1, 1)
        plt.plot(x, tf.math.sigmoid(discriminator(x, training=False).numpy()), label='discriminator', color='k')
        plt.plot(x, 0.5 * np.ones(x.shape), label='0.5', color='b')
        plt.xlabel('x')

    plt.legend()
    plt.show()


def plot_array(X, title=""):
    plt.rcParams['figure.figsize'] = (20, 20)

    for i, x in enumerate(X[0:5]):
        x = x.numpy()
        max_ = x.max()
        min_ = x.min()
        xnew = np.uint(255 * (x - min_) / (max_ - min_))
        plt.subplot(1, 5, i + 1)
        plt.imshow(xnew)
        plt.axis("off")

    plt.show()

mean = [10]
cov = [[1]]
X = tf.random.normal((5000,1),mean=10,stddev=1.0)

print("mean:",np.mean(X))
print("standard deviation:",np.std(X))

Z = tf.random.normal((5000,1),mean=0,stddev=2)

print("mean:",np.mean(Z))
print("standard deviation:",np.std(Z))

plot_distribution(X,Z,discriminator=None,density=True)

Xhat=Z+10

print("mean:",np.mean(Xhat))
print("standard deviation:",np.std(Xhat))

plot_distribution(X,Xhat,discriminator=None,density=True)

def make_generator_model():
    generator = tf.keras.Sequential()
    generator.add(layers.Dense(1))
    return generator

generator=make_generator_model()

Xhat = generator(Z, training=False)
plot_distribution(real_data=X,generated_data=Xhat)

def make_discriminator_model():
    discriminator=tf.keras.Sequential()
    discriminator.add(layers.Dense(1))
    return discriminator

discriminator=make_discriminator_model()

plot_distribution(real_data=X,generated_data=Xhat,discriminator=discriminator)

py_x=tf.math.sigmoid(discriminator(X,training=False))
np.sum(py_x>0.5)

py_x=discriminator(Xhat)
np.sum(py_x>0.5)

def get_accuracy(X,Xhat):
    total=0
    py_x=tf.math.sigmoid(discriminator(X,training=False))
    total=np.mean(py_x)
    py_x=tf.math.sigmoid(discriminator(Xhat,training=False))
    total+=np.mean(py_x)
    return total/2

get_accuracy(X,Xhat)

# This method returns a helper function to compute crossentropy loss
cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)
def generator_loss(Xhat):
    return cross_entropy(tf.ones_like(Xhat), Xhat)

def discriminator_loss(X, Xhat):
    real_loss = cross_entropy(tf.ones_like(X), X)
    fake_loss = cross_entropy(tf.zeros_like(Xhat), Xhat)
    total_loss = 0.5*(real_loss + fake_loss)
    return total_loss

generator_optimizer = tf.keras.optimizers.Adam(5e-1,beta_1=0.5,beta_2=0.8)

discriminator_optimizer = tf.keras.optimizers.Adam(5e-1,beta_1=0.5, beta_2=0.8)

# parameters for training
epochs = 20
BATCH_SIZE = 5000
noise_dim = 1
epsilon = 100

# discrimator and gernerator
tf.random.set_seed(0)
discriminator = make_discriminator_model()
generator = make_generator_model()

tf.config.run_functions_eagerly(True)

gen_loss_epoch = []
disc_loss_epoch = []
plot_distribution(real_data=X, generated_data=Xhat, discriminator=discriminator)
print("epoch", 0)

for epoch in tqdm(range(epochs)):
    # data for the true distribution of your real data samples training ste
    x = tf.random.normal((BATCH_SIZE, 1), mean=10, stddev=1.0)
    # random samples it was found if you increase the standard deviation, you get better results
    z = tf.random.normal([BATCH_SIZE, noise_dim], mean=0, stddev=10)
    # needed to compute the gradients for a list of variables.
    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        # generated sample
        xhat = generator(z, training=True)
        # the output of the discriminator for real data
        real_output = discriminator(x, training=True)
        # the output of the discriminator  data
        fake_output = discriminator(xhat, training=True)
        # loss for each
        gen_loss = generator_loss(fake_output)
        disc_loss = discriminator_loss(real_output, fake_output)
    # Compute the gradients for gen_loss and generator
    gradients_of_generator = gen_tape.gradient(gen_loss, generator.trainable_variables)
    # Compute the gradients for gen_loss and discriminator
    gradients_of_discriminator = disc_tape.gradient(disc_loss, discriminator.trainable_variables)
    # Ask the optimizer to apply the processed gradients
    generator_optimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))
    discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))

    # Save and display the generator and discriminator if the performance increases
    if abs(0.5 - get_accuracy(x, xhat)) < epsilon:
        epsilon = abs(0.5 - get_accuracy(x, xhat))
        generator.save('generator')
        discriminator.save('discriminator')
        print(get_accuracy(x, xhat))
        plot_distribution(real_data=X, generated_data=xhat, discriminator=discriminator)
        print("epoch", epoch)

        generator = make_generator_model()
        generator = models.load_model('generator')
        xhat = generator(z)
        discriminator = models.load_model('discriminator')
        plot_distribution(real_data=X, generated_data=xhat, discriminator=discriminator)

        dataset_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML311-Coursera/labs/Module6/cartoon_20000.zip"
        await skillsnetwork.prepare(dataset_url, overwrite=True)

        img_height, img_width, batch_size = 70, 70, 150

        train_ds = tf.keras.utils.image_dataset_from_directory(directory='cartoon_20000',
                                                               image_size=(img_height, img_width),
                                                               batch_size=batch_size,
                                                               label_mode=None)

        normalization_layer = layers.experimental.preprocessing.Rescaling(scale=1. / 127.5, offset=-1)
        normalized_ds = train_ds.map(lambda x: normalization_layer(x))

        images = train_ds.take(1)

        X = [x for x in images]

        plot_array(X[0])


        def make_generator():
            model = Sequential()

            # input is latent vector of 100 dimensions
            model.add(Input(shape=(1, 1, 100), name='input_layer'))

            # Block 1 dimensionality of the output space  64 * 8
            model.add(Conv2DTranspose(64 * 8, kernel_size=4, strides=4, padding='same',
                                      kernel_initializer=tf.keras.initializers.RandomNormal(mean=0.0, stddev=0.02),
                                      use_bias=False, name='conv_transpose_1'))
            model.add(BatchNormalization(momentum=0.1, epsilon=0.8, center=1.0, scale=0.02, name='bn_1'))
            model.add(ReLU(name='relu_1'))

            # Block 2: input is 4 x 4 x (64 * 8)
            model.add(Conv2DTranspose(64 * 4, kernel_size=4, strides=2, padding='same',
                                      kernel_initializer=tf.keras.initializers.RandomNormal(mean=0.0, stddev=0.02),
                                      use_bias=False, name='conv_transpose_2'))
            model.add(BatchNormalization(momentum=0.1, epsilon=0.8, center=1.0, scale=0.02, name='bn_2'))
            model.add(ReLU(name='relu_2'))

            # Block 3: input is 8 x 8 x (64 * 4)
            model.add(Conv2DTranspose(64 * 2, kernel_size=4, strides=2, padding='same',
                                      kernel_initializer=tf.keras.initializers.RandomNormal(mean=0.0, stddev=0.02),
                                      use_bias=False, name='conv_transpose_3'))
            model.add(BatchNormalization(momentum=0.1, epsilon=0.8, center=1.0, scale=0.02, name='bn_3'))
            model.add(ReLU(name='relu_3'))

            # Block 4: input is 16 x 16 x (64 * 2)
            model.add(Conv2DTranspose(64 * 1, kernel_size=4, strides=2, padding='same',
                                      kernel_initializer=tf.keras.initializers.RandomNormal(mean=0.0, stddev=0.02),
                                      use_bias=False, name='conv_transpose_4'))
            model.add(BatchNormalization(momentum=0.1, epsilon=0.8, center=1.0, scale=0.02, name='bn_4'))
            model.add(ReLU(name='relu_4'))

            model.add(Conv2DTranspose(3, 4, 2, padding='same',
                                      kernel_initializer=tf.keras.initializers.RandomNormal(mean=0.0, stddev=0.02),
                                      use_bias=False,
                                      activation='tanh', name='conv_transpose_5'))

            return model


        gen = make_generator()
        gen.summary()


        def make_discriminator():
            model = Sequential()

            # Block 1: input is 64 x 64 x (3)
            model.add(Input(shape=(64, 64, 3), name='input_layer'))
            model.add(Conv2D(64, kernel_size=4, strides=2, padding='same',
                             kernel_initializer=tf.keras.initializers.RandomNormal(mean=0.0, stddev=0.02),
                             use_bias=False, name='conv_1'))
            model.add(LeakyReLU(0.2, name='leaky_relu_1'))

            # Block 2: input is 32 x 32 x (64)
            model.add(Conv2D(64 * 2, kernel_size=4, strides=2, padding='same',
                             kernel_initializer=tf.keras.initializers.RandomNormal(mean=0.0, stddev=0.02),
                             use_bias=False, name='conv_2'))
            model.add(BatchNormalization(momentum=0.1, epsilon=0.8, center=1.0, scale=0.02, name='bn_1'))
            model.add(LeakyReLU(0.2, name='leaky_relu_2'))

            # Block 3
            model.add(Conv2D(64 * 4, 4, 2, padding='same',
                             kernel_initializer=tf.keras.initializers.RandomNormal(mean=0.0, stddev=0.02),
                             use_bias=False, name='conv_3'))
            model.add(BatchNormalization(momentum=0.1, epsilon=0.8, center=1.0, scale=0.02, name='bn_2'))
            model.add(LeakyReLU(0.2, name='leaky_relu_3'))

            # Block 4
            model.add(Conv2D(64 * 8, 4, 2, padding='same',
                             kernel_initializer=tf.keras.initializers.RandomNormal(mean=0.0, stddev=0.02),
                             use_bias=False, name='conv_4'))
            model.add(BatchNormalization(momentum=0.1, epsilon=0.8, center=1.0, scale=0.02, name='bn_3'))
            model.add(LeakyReLU(0.2, name='leaky_relu_4'))

            # Block 5
            model.add(Conv2D(1, 4, 2, padding='same',
                             kernel_initializer=tf.keras.initializers.RandomNormal(mean=0.0, stddev=0.02),
                             use_bias=False,
                             activation='sigmoid', name='conv_5'))

            return model


        disc = make_discriminator()
        disc.summary()

        cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)


        def generator_loss(Xhat):
            return cross_entropy(tf.ones_like(Xhat), Xhat)


        def discriminator_loss(X, Xhat):
            real_loss = cross_entropy(tf.ones_like(X), X)
            fake_loss = cross_entropy(tf.zeros_like(Xhat), Xhat)
            total_loss = 0.5 * (real_loss + fake_loss)
            return total_loss


        learning_rate = 0.0002

        generator_optimizer = tf.keras.optimizers.Adam(lr=0.0002, beta_1=0.5, beta_2=0.999)

        discriminator_optimizer = tf.keras.optimizers.Adam(lr=0.0002, beta_1=0.5, beta_2=0.999)


        @tf.function
        def train_step(X):
            # random samples it was found if you increase the  stander deviation, you get better results
            z = tf.random.normal([BATCH_SIZE, 1, 1, latent_dim])
            # needed to compute the gradients for a list of variables.
            with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
                # generated sample
                xhat = generator(z, training=True)
                # the output of the discriminator for real data
                real_output = discriminator(X, training=True)
                # the output of the discriminator for fake data
                fake_output = discriminator(xhat, training=True)

                # loss for each
                gen_loss = generator_loss(fake_output)
                disc_loss = discriminator_loss(real_output, fake_output)
            # Compute the gradients for gen_loss and generator

            gradients_of_generator = gen_tape.gradient(gen_loss, generator.trainable_variables)
            # Compute the gradients for gen_loss and discriminator
            gradients_of_discriminator = disc_tape.gradient(disc_loss, discriminator.trainable_variables)
            # Ask the optimizer to apply the processed gradients
            generator_optimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))
            discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))

            generator = make_generator()
            BATCH_SIZE = 128

            latent_dim = 100
            noise = tf.random.normal([BATCH_SIZE, 1, 1, latent_dim])
            Xhat = generator(noise, training=False)
            plot_array(Xhat)

            epochs = 1

            discriminator = make_discriminator()

            generator = make_generator()

            for epoch in range(epochs):

                # data for the true distribution of your real data samples training ste
                start = time.time()
                i = 0
                for X in tqdm(normalized_ds, desc=f"epoch {epoch + 1}", total=len(normalized_ds)):

                    i += 1
                    if i % 1000:
                        print("epoch {}, iteration {}".format(epoch + 1, i))

                    train_step(X)

                noise = tf.random.normal([BATCH_SIZE, 1, 1, latent_dim])
                Xhat = generator(noise, training=False)
                X = [x for x in normalized_ds]
                print("orignal images")
                plot_array(X[0])
                print("generated images")
                plot_array(Xhat)
                print('Time for epoch {} is {} sec'.format(epoch + 1, time.time() - start))


generator_url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-GPXX0XCEEN/data/generator.tar"
await skillsnetwork.prepare(generator_url, overwrite=True)

from tensorflow.keras.models import load_model


full_generator=load_model("generator")

latent_dim=100

# input consists of noise vectors
noise = tf.random.normal([200, 1, 1, latent_dim])

# feed the noise vectors to the generator
Xhat=full_generator(noise,training=False)
plot_array(Xhat)

for c in [1,0.8,0.6,0.4]:
    Xhat=full_generator(c*tf.ones([1, 1, 1, latent_dim]),training=False) # latent_dim = 100 defined previously
    plot_array(Xhat)


z=np.ones( (1, 1, 1, latent_dim))
for n in range(10):

    z[0, 0, 0, 0:10*n]=-1

    Xhat=full_generator(z,training=False)
    print("elements from 0 to {} is set to -1".format(10*n))
    plot_array(Xhat)

    for n in range(10):
        z = np.random.normal(0, 1, (1, 1, 1, latent_dim))

        z[0, 0, 0, 0:35] = 1

        Xhat = full_generator(z, training=False)

        plot_array(Xhat)

