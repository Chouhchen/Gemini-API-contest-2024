#!/usr/bin/env python
# coding: utf-8


import google.generativeai as genai
import os
my_api_key = "your key here"
genai.configure(api_key=my_api_key)

# images input
import PIL.Image

sample1 = PIL.Image.open('.../Gemini0824/1983.png')
sample2 = PIL.Image.open('.../Motorola-StarTAC_1991.png')
sample3 = PIL.Image.open('.../FOMA_N900iS_3G2001.png')
sample4 = PIL.Image.open('.../4G2009.png')
sample5 = PIL.Image.open('...Galax_4G2017.png')
sample6 = PIL.Image.open('.../iPhone-2020.png')
sample7 = PIL.Image.open('...//2024-S9-PRO-for-4G-5g-GSM.png')



# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro")


# initial the model to analyse the product development trend

prompt = "I am giving you a historical development of mobile phone, the images are in order with the oldest first. Summarize the trend  of the product design and feature in the images in 1000 words"

response_1 = model.generate_content([prompt,sample1, sample2, sample3, sample4, sample5, sample6])

print(response_1.text)

# ask the model to make prediciton
prompt2 = f"base on the trend of mobile phone's design and feature development you state in {response_1}, make prediciton of the  next come up moble phone design would be with detailed features within 500 words"
response_2 = model.generate_content([prompt2])
print(response_2.text)


# train model to improve it's prediction
prompt3 = f"The phone in the image is a real-life example of next coming up mobile phone with your analysis of mobile phone trend in {response_1}, please compare your prediction on {response_2} make improvment on the way you make prediction of the next coming up phone design and detailed features whin 500 words"
response_3 = model.generate_content([prompt3,sample7])

print(response_3.text)

# make prediciton on the future phone 
prompt4 = f" Base on the mobile phone trend you analysed in {response_1} and improved prediction of {response_3}, please make prediction of the next coming up mobile phone design and detailed features whin 500 words"
response_4 = model.generate_content([prompt3])

print(response_4.text)

# transfer text in a prompt for image generation in Vertex, but I don't have access, so I use others
prompt5 = f" I would like to use Vertex AI to generate an mobile phone image that fits into the design and features you prediction in {response_4}, please write desciptive prompt to generate an mobile phone's image" 
response_5 = model.generate_content([prompt5])
print(response_5.text)






# In[ ]:





# In[ ]:





# In[ ]:




