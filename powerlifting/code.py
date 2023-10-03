import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy import binom

# Load all dataframe fragments
df_01 = pd.read_csv("https://github.com/thecyberdragon/data-analysis/tree/main/powerlifting/df_01.csv")
df_02 = pd.read_csv("https://github.com/thecyberdragon/data-analysis/tree/main/powerlifting/df_02.csv")
df_03 = pd.read_csv("https://github.com/thecyberdragon/data-analysis/tree/main/powerlifting/df_03.csv")
df_04 = pd.read_csv("https://github.com/thecyberdragon/data-analysis/tree/main/powerlifting/df_04.csv")
df_05 = pd.read_csv("https://github.com/thecyberdragon/data-analysis/tree/main/powerlifting/df_05.csv")
df_06 = pd.read_csv("https://github.com/thecyberdragon/data-analysis/tree/main/powerlifting/df_06.csv")
df_07 = pd.read_csv("https://github.com/thecyberdragon/data-analysis/tree/main/powerlifting/df_07.csv")
df_08 = pd.read_csv("https://github.com/thecyberdragon/data-analysis/tree/main/powerlifting/df_08.csv")
df_09 = pd.read_csv("https://github.com/thecyberdragon/data-analysis/tree/main/powerlifting/df_09.csv")
df_10 = pd.read_csv("https://github.com/thecyberdragon/data-analysis/tree/main/powerlifting/df_10.csv")
df_11 = pd.read_csv("https://github.com/thecyberdragon/data-analysis/tree/main/powerlifting/df_11.csv")
df_12 = pd.read_csv("https://github.com/thecyberdragon/data-analysis/tree/main/powerlifting/df_12.csv")
df_13 = pd.read_csv("https://github.com/thecyberdragon/data-analysis/tree/main/powerlifting/df_13.csv")

# Combine dataframes back together
df = pd.concat([df_01, df_02, df_03, df_04, df_05, df_06, df_07, df_08, df_09, df_10, df_11, df_12, df_13])

