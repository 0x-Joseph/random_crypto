# !/usr/bin/python3


import yfinance as yf
import pandas as pd
import numpy as np
import json
#from datetime import datetime, date, timedelta 


aapl = yf.Ticker('AAPL')

print(aapl)
print(aapl.option_chain('2022-04-29'))


# joe@Josephs-iMac python scripts %  cd "/Users/joe/python scripts" ; /usr/bin/env /usr/local/bin/python3 
# /Users/joe/.vscode/extensions/ms-python.python-2022.4.1/pythonFiles/lib/python/debugpy/launcher 59734 -- "/Users/joe/python scripts/Crypto API/yf_practice.py" 