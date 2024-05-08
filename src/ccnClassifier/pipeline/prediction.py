import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import  image
import tensorflow as tf
import os

class Predictionpipeline:
    def __init__(self,filename):
        self.filename=filename

    def predict(self):
        model=load_model(os.path.join("model","model.h5"))

        imagename=self.filename
        # test_image=image.load_img(imagename,target_size=(224,244))
        # test_image=image.img_to_array(test_image)
        # test_image=np.expand_dims(test_image,axis=0)
        # test_image = test_image.astype('float32') / 255.0 
        image = tf.io.read_file(imagename)
        # Decode the image to a tensor
        image = tf.image.decode_image(image, channels=3)
        # Resize the image to the target size
        image = tf.image.resize(image, (224,224))
        # Normalize the image to [0, 1] range
        image = tf.cast(image, tf.float32) / 255.0
        # Add batch dimension (expand_dims adds a new dimension at index 0)
        image = tf.expand_dims(image, axis=0)
        result=np.argmax(model.predict(image),axis=1)
        
        print(result)
        
        if result[0]==1:
            prediction="Tumor"
            return [{"image":prediction}]
        
        else:
            prediction="Normal" 
            return [{"image":prediction}] 

    

