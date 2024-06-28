import os
import sys
from src.exceptions import CustomException
from src.logger import logging
import tensorflow as tf
import pickle

# logging.info("porocess starts")

# import transformers
# import torch 

# logging.info("porocess ends")

# try:
#     file = open("transcript.txt", "r")
#     FileContent = file.read().strip()
#     logging.info("File opened")
# except:
#     logging.error("File not found")
#     raise CustomException("File not found",sys)
    

import transformers
import torch 
import tensorflow as tf


try:
    file = open(r"C:\Users\aaditya\Desktop\aaditya\ml-dl\ml_project_1\Text_summarisation\transcript.txt", "r")
    FileContent = file.read().strip()
    # logging.info("File opened")
except:
    # logging.error("File not found")
    raise CustomException("File not found",sys)
    

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

checkpoint = "sshleifer/distilbart-cnn-12-6"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

import nltk
nltk.download('punkt')
sentences = nltk.tokenize.sent_tokenize(FileContent)

length = 0
chunk = ""
chunks = []
count = -1
for sentence in sentences:
  count += 1
  combined_length = len(tokenizer.tokenize(sentence)) + length # add the no. of sentence tokens to the length counter

  if combined_length  <= tokenizer.max_len_single_sentence: # if it doesn't exceed
    chunk += sentence + " " # add the sentence to the chunk
    length = combined_length # update the length counter

    # if it is the last sentence
    if count == len(sentences) - 1:
      chunks.append(chunk.strip()) # save the chunk
    
  else: 
    chunks.append(chunk.strip()) # save the chunk
    
    # reset 
    length = 0 
    chunk = ""

    # take care of the overflow sentence
    chunk += sentence + " "
    length = len(tokenizer.tokenize(sentence))


inputs = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]


for input in inputs:
  output = model.generate(**input)
  print(tokenizer.decode(*output, skip_special_tokens=True))



try:
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)

    with open(file_path, "wb") as file_obj:
        pickle.dump(obj, file_obj)

except Exception as e:
    raise CustomException(e, sys)
    

