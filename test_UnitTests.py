import inspect
import pandas as pd
import numpy as np
import numpy as np
from scipy.stats import norm

import WhoAmI_File
def test_WhoAmI():
    assert WhoAmI_File.WhoAmI() != ''

import YFinance_File
def test_YahooData2returns():
    d = {   'Open': [100, 102, 101, 103],
            'High': [105, 104, 103, 105],
            'Low': [98, 100, 99, 101],
            'Close': [101, 103, 102, 104],
            'Adj Close': [101, 103, 102, 104],
            'Volume': [1000, 1200, 900, 1100]}

    index = pd.to_datetime(['2023-10-26', '2023-10-27', '2023-10-28', '2023-10-29'])
    tempdata = pd.DataFrame(d, index=index)
    assert np.array_equal(YFinance_File.YahooData2returns(tempdata), np.array([ 0.01980198, -0.00970874,  0.01960784]))

import Var_File
def test_VaR():
    r = np.random.normal(0.05, 0.03, 1000000)
    probability2SD = norm.cdf(2)  
    percent_var = Var_File.VaR(r, probability2SD)
    assert np.round(percent_var, 2) == 0.01

import ES_File
def test_ES():
    u = np.random.uniform(0, 100, 100000)

    # Test the ES function with an alpha of 0.8
    es_alpha = ES_File.es(losses=u, alpha=0.8)
    assert np.round(es_alpha, 0) == 90
    
    # Test the ES function with a VaR of 80
    es_var = ES_File.es(losses=u, VaR=80)
    assert np.round(es_var, 0) == 90
