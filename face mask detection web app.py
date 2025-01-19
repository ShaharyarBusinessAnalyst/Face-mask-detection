#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install -r requirements.txt

import numpy
import pickle
import streamlit
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import requests


# In[4]:


#loaded_model = pickle.load(open('C:/Users/ShaharyarAmjad/Downloads/face mask detection deployment model/face_mask_detection_model.sav','rb')

def load_model_from_drive(url):
    response = requests.get(url)
    with open("face_mask_detection_model.sav", "wb") as f:
        f.write(response.content)
    
    with open("face_mask_detection_model.sav", "rb") as f:
        return pickle.load(f)

model_url = "https://drive.google.com/file/d/1UPCuyxIouOYMeQkrfBEO9OQ9TpwWo3u6/view?usp=sharing"  # Replace <FILE_ID> with your file ID
st.write("Loading model from Google Drive...")
loaded_model = load_model_from_drive(model_url)
st.write("Model loaded successfully!")


                           


# In[ ]:


def face_detection(input_image_path):

    if isinstance(input_image, Image.Image):
        input_image = np.array(input_image)
        
    #input_image = cv2.imread(input_image_path)
    
    #plt.imshow(input_image)
    
    input_image_resized = cv2.resize(input_image, (128,128))
    
    input_image_scaled = input_image_resized/255
    
    input_image_reshaped = np.reshape(input_image_scaled, [1,128,128,3])
    
    input_prediction = model.predict(input_image_reshaped)
    
    print(input_prediction)
    
    input_pred_label = np.argmax(input_prediction)
    
    if input_pred_label == 1:
      return 'The person in the image is wearing a mask'
    else:
      return 'The person in the image is not wearing a mask'                           
        


# In[ ]:


def main():

    #giving a title
    st.title('Face mask detection web app')

    #getting the input from user
    image = st.file_uploader('Please upload the image', type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Open image using PIL
        image = Image.open(uploaded_file)
    
        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        #prediction
        conclusion = ''

        #creating a button for prediction
        if st.button('Image result'):
            face_detection(image)

        st.success(conclusion)

if __name__ == '__main__':
    main()

