import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os


st.set_page_config(page_title='AI Image Detector' , layout='centered')

print("✅ File exists:", os.path.exists("finetuned_ai_detector_v2.keras"))
print("📦 File size:", os.path.getsize("finetuned_ai_detector_v2.keras"), "bytes")

def load_model():
  model=tf.keras.models.load_model("finetuned_ai_detector_v2.keras")
  return model

model=load_model()


st.title("AI Image Detector")
st.write("Upload a face image and the model will predict whether it's Real or AI-generated.")

uploaded_file=st.file_uploader("upload an image",type=['jpeg','jpg','png'])

if uploaded_file is not none:
  image=Image.open(uploaded_file).convert('RGB')
  st.image(image , caption="Uploaded Image" , set_coloumn_width=True)

  image=image.resize(160,160)
  image_array= tf.keras.preprocessing.image.img_to_array(img)/255.0
  image_array=np.expand_dims(image_array,axis=0)

  prediction=model.predict(image_array)[0][0]
  label="Fake" if prediciton>0.5 else "Real"
  confidence = prediction if prediciton>0.5 else 1-prediciton

  st.subheader("Prediction:")
  st.write(f"**{label}** with {confidence:.2%} confidence.")
  

