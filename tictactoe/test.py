import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

ser = pd.Series(data={'r':"red","g":"green","b":"blue","c":"cyan"},index={'r','g','b'})
print(ser)