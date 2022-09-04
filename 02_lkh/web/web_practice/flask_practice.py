
# imports --------------------------------------------------
# framework
from flask import Flask, make_response, jsonify, request, render_template

# parser
from bs4 import BeautifulSoup
import json
import xmltodict
from pandas.io.json import json_normalize

# others
import pandas as pd
import numpy as np
import requests
import datetime
from pykrx import stock

# def ----------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------



# app ----------------------------------------------

app = Flask(__name__)

# route --------------------------------------------

@app.route('/')
def index():
    return render_template(
        'index.html',
        
    )


# dir ----------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)



