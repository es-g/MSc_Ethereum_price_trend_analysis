# **Machine Learning-based Analysis of Ethereum’s Price Trend**

By: **Yesbol Gabdullin**

*Practical implementation of MSc Dissertation submitted in partial fulfilment
of the requirements for the degree of
Master of Science in Artificial Intelligence*

## Abstract
The financial market has witnessed a substantial growth in cryptocurrencies in the last years. To date, there are more than twenty thousand cryptocurrencies with a total market capitalisation of over a trillion USD. The increasing market acceptance of cryptocurrencies has attracted investors as well academic community. Even more credible investors including financial institutions started introducing cryptocurrencies into their portfolios. This is because cryptocurrencies provide an alternative investment instrument that offers diversification due to its low correlation with other financial instruments. Therefore, there is a growing demand for tools and frameworks to investigate cryptocurrencies and their price behaviour to make informed investment decisions. Although there is an increasing amount of literature on cryptocurrency price prediction and modelling, their price behaviour remains predominantly unexplored, especially for altcoins. Time-series forecasting of the financial markets, including cryptocurrency market, is an extremely complex task due to the highly noisy data, non-stationarity, and large volume of information available to investors. This work presents the investigation of predictability of Ethereum's price trend using Machine Learning. To account for non-stationarity nature of cryptocurrency market and reduce the bias towards more recent period, this work employs walk-forward sliding window approach instead of traditional train-test split adopted by most researchers. The findings indicate that prediction of price trend of Ethereum is possible. This contradicts with Efficient Market Hypothesis which states that prices already reflect all the available information making the market prediction impossible. The results in this research agree with Adaptive Market Hypothesis which claims that rationality and irrationality exist side-by-side, and profitable arbitrage opportunities exist for some periods of time. This research proposes a framework for predicting the price direction of cryptocurrency that can be used as an Expert System. This will benefit both retail and institutional investors. The results based on the methodology proposed in this work outperform other works in the scientific literature in terms of classification evaluation metrics

### **Aim**
* To investigate short-term predictability of Ethereum cryptocurrency using technical indicators, on-chain metrics and search volume (Google Trends)

### **Objectives**
1. Identify to what extent the price trend of Ethereum cryptocurrency is predictable
2. Identify what features result in highest accuracy
3. Explore if using a diverse set of input features (On-chain metrics and search volume) improve the accuracy of predictions
4. Explore various window (training) and testing sizes in walk-forward sliding window approach to identify the optimal
5. Identify the Machine Learning model that is better suited for Ethereum price trend prediction



# **How to Install (Windows)**

1. Create a virtual environment 

`python -m venv <myvenv>` 

where `<myvenv>` is the name of your virtual environment


2. Activate the virtual environment 

`myvenv\Scripts\Activate`

3. Install the dependencies (Python libraries)

`pip install -r requirements.txt` 


# **How to Use**

1. Get free API key from https://min-api.cryptocompare.com
2. Paste your API key into `config.py` file
3. Run simulations.ipynb

<br />
<br />

______________________
<br />
The MIT License (MIT)

Copyright (c) 2022 Yesbol Gabdullin

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

