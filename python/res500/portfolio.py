#!/usr/bin/env python3
'''
Used for my financial analysis of Luman Technologies, Inc.

yfinance ref: 
https://pypi.org/project/yfinance/
https://aroussi.com/post/python-yahoo-finance
'''

import json
import pandas as pd
import plotly.express as px
import yfinance as yf

# Create ticker
lumn = yf.Ticker("LUMN")

# Get basic information on the company
info = lumn.info
with open("info.txt", "w") as f:
    f.write(json.dumps(info))

# Download stock price history and create dataframe
df = lumn.history(start="2018-09-01",end="2021-10-01")

fig1 = px.scatter(data_frame=df, y="Close")
fig1.write_image("closing_prices.png")

fig2 = px.scatter(data_frame=df, y="Volume")
fig2.write_image("volume.png")