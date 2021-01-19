
def predictMyPet(path):
    import tensorflow as tf
    from tensorflow import keras
    import numpy as np
    
    new_model = tf.keras.models.load_model('saved_model/my_model')
    img_path=path
    
    img = keras.preprocessing.image.load_img(
        img_path, target_size=(180,180)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    
    predictions =new_model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    
    class_names=['cats', 'dogs']
    ans  = "This image most likely belongs to {} with a {:.2f} percent confidence.".format(class_names[np.argmax(score)], 100 * np.max(score))
    return ans
