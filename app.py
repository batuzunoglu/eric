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

from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    print_message = "Hello, Render!"
    print(print_message)
    return print_message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))