# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 23:32:05 2025

@author: shuo22H
"""

import streamlit as st
import pandas as pd
import numpy as np


st.title("This is a test")
 
st.write("## To show the *Model!*")

col1, col2, col3 = st.columns(3)
k = col1.number_input(label='Input the slope', min_value=0.1, value=1.0)
b = col1.number_input(label='Input the offset', value=0)


col3.metric(label='Slope', value=f"{k:.2f}")
col3.metric(label='Intercept', value=f"{b:.2f}")

xx = np.arange(10)
yy = xx * k + b
xx = xx.reshape(-1,1)
yy = yy.reshape(-1,1)

data = np.concatenate([xx,yy], axis=1) 
df = pd.DataFrame(data, columns=['x', 'y'])
df.set_index('x', inplace=True)


st.line_chart(df)


table = pd.read_csv("industry.csv")
st.write(table)
