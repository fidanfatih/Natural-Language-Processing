#!pip install clean-text

import numpy as np
import pandas as pd
import re
import nltk
from cleantext import clean

try:
  with open("test1_2.txt", "r", encoding="utf-8") as file:
    text_data1 = file.read()
    print(text_data1)
except:
  print("There is not such a file  or path is incorrect")