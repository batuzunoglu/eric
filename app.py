import streamlit as st
import pandas as pd
import plotly.express as px


def draw_horse():
    horse = """
         ,--,
    _ ___/ /\|
 ,;'( )__, )  ~
//  //   '--;.
'   \     | ^
     ^    ^      
    """
    print(horse)

draw_horse()

st.title(draw_horse())

