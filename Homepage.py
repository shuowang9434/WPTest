# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 23:32:05 2025

@author: shuo22H
"""

import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image

st.set_page_config(layout="wide")
# st.markdown("""
#             <style>
#             .appview-container {
#                 width: 80%;
#                 max-width: none;
#             }
#             </style>
#             """, unsafe_allow_html=True)

st.header("Qi TANG")
 
#st.write("## Centre for Hydrogeology and Geothermics")

col1, col2, col3 = st.columns([3,0.5,2])


col1.subheader("Background")
col1.write('''
           2024.2 – present : Coordinator of the Swiss Water Earth Systems PhD School, University of Neuchâtel, Neuchâtel, Switzerland

2024.8 – present : Research fellow, Department of environment science, University of Basel, Basel, Switzerland

2022.7 – 2024.7 : Postdoc, Department of environment science, University of Basel, Basel, Switzerland

2022.6 – 2024.1 : Postdoc, Center for Hydrogeology and Geothermal Energy (CHYN), University of Neuchâtel, Neuchâtel, Switzerland

2021.1 – 2022.5 : Research fellow, Institute of Geographic Sciences and Natural Resources Research, Chinese Academy of Sciences, Beijing, China

2017.9 – 2020.12: Postdoc, Alfred Wegener Institute for Polar and Marine Research (AWI), Bremerhaven, Germany

2012.10 – 2017.8: PhD, Hydrogeology, Institute for Bio- and Geosciences (IBG-3: Agrosphere), Forschungszentrum Jülich & Rheinisch-Westfälische Technische Hochschule Aachen (RWTH Aachen University), Germany

2015.5 – 2015.8 : visiting PhD-student, Center for Hydrogeology and Geothermal Energy, University of Neuchâtel, Switzerland

2009.9 – 2012.6 : MSc, Hydrology and water resources, College of Water Science, Beijing Normal University, Beijing, China.

2005.9 – 2009.6 :  BSc, Applied mathematics, College of Science, China Agriculture University, Beijing, China.''')


#image = Image.open('Lisbon.jpg')

col3.image('Lisbon.jpg', caption='Qi Tang', width=400)


cc1, cc2, cc3 = col3.columns(3)
# cc1.link_button("GitHub", "https://github.com/qiqi1023t")
# cc3.link_button("Google Scholar", "https://scholar.google.com/citations?user=xUIF4CQAAAAJ&hl=en")
# cc2.link_button("LinkedIn", "https://www.linkedin.com/in/qi-tang-a0601822/")


button_html = """
<a href="https://github.com/qiqi1023t" target="_blank">
  <img src='icons/github.png' alt="Button Image" style="width:100px;height:50px;">
</a>
"""

cc1.markdown(button_html, unsafe_allow_html=True)
cc2.image('icons/github.png')

# try:
#     image = Image.open("icons/github.png") # Replace with the correct path
#     st.image(image, caption="Button Image", width=100)  # Display, set width
#     # Get the URL of the image from the st.image element
#     image_url = f"data:image/png;base64,{st.image(image, output_format='PNG').getvalue()}" # Use .getvalue() to get image data for the HTML link
# except FileNotFoundError:
#     st.error("Image file not found.  Please check the path.")
#     image_url = None # Set image_url to none if the image file cannot be found, prevents crashing

# # 2. Create the HTML button using the st.image() element
# if image_url: # Only displays HTML if there is a valid image url
#     button_html = f"""
#     <a href="https://github.com/qiqi1023t" target="_blank">
#       <img src="{image_url}" alt="Button Image" style="width:100px;height:50px;">
#     </a>
#     """

#     st.markdown(button_html, unsafe_allow_html=True)
# else:
#     st.write("Invalid Image File")





#%%

# social_icons_data = {
# "Kaggle": ["https://www.kaggle.com/abhisheak", "C:/Users/shuo22H/OneDrive/Qi_work/Homepage/github.png"],
# "LinkedIn": ["https://www.linkedin.com/in/abhisheaksaraswat", "https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
# "GitHub": ["https://github.com/abhisheaksaraswat", "https://cdn-icons-png.flaticon.com/128/5968/5968866.png"],
# "YouTube": ["https://www.youtube.com/@programmingisfunn", "https://cdn-icons-png.flaticon.com/128/1384/1384060.png"],
# "Medium": ["https://medium.com/@programmingisfun", "https://cdn-icons-png.flaticon.com/128/5968/5968906.png"]
# }

# social_icons_html = [
# f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'>"
# f"<img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'"
# f" style='width: 25px; height: 25px;'></a>"
# for platform in social_icons_data
# ]
# col1.write(f"""
# <div style="display: flex; justify-content: center; margin-bottom: 20px;">
# {''.join(social_icons_html)}
# </div>""", 
# unsafe_allow_html=True)


