# Predicting a new image using our CNN model
import numpy as np
#from keras.preprocessing import image
from keras.utils import load_img, img_to_array
import tensorflow as tf
import cv2
import os
from mtcnn_cv2 import MTCNN
from tensorflow.keras.preprocessing.image import load_img , img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import streamlit as st

model=tf.keras.models.load_model(r"dmg_car-weights-CNN.h5")
model_damage = tf.keras.models.load_model(r"damagemodel.h5")
model_location= tf.keras.models.load_model(r"locationmodel.h5")
model_serverity= tf.keras.models.load_model(r"serverity_model.h5")
#
def predict_image(img, model, threshold):
    # Load and preprocess the image
    img = load_img(img, target_size=model.input_shape[1:4])
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Make predictions using the model
    prediction = model.predict(img_array)
    return prediction


def predictimage(img, model, threshold):
    # Load and preprocess the image
    img = load_img(img, target_size=model.input_shape[1:4])
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Make predictions using the model
    prediction = model.predict(img_array)
    return prediction
    

    
def predictimage_1(img, model, threshold):
    # Load and preprocess the image
    img = load_img(img, target_size=model.input_shape[1:4])
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    # Make predictions using the model
    prediction = model.predict(img_array)
    return prediction
    

st.title('Car Damage Predictor')
st.write("---")
st.markdown('Upload an image of a car to see if it is damaged or not.')
st.sidebar.title('Settings')
threshold = st.sidebar.slider('Threshold', 0.0, 1.0, 0.5, 0.01)
def main():
  uploaded_file = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])
  if st.button('Predict'):
        progress_bar = st.progress(0)
        result=predict_image(uploaded_file, model, threshold)
        if(result[0][0]>=0.5):
            st.write("Validation complete - proceed to location and severity determination")
        else:
            st.write("Are you sure that your car is damaged? Please submit another picture of the damage.")
            st.write("Hint: Try zooming in/out, using a different angle or different lighting")
        
main()
