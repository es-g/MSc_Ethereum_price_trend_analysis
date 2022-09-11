# **Machine Learning-based Analysis of Ethereum’s Price Trend**

By: **Yesbol Gabdullin**

Practical implementation of MSc Dissertation submitted in partial fulfilment
of the requirements for the degree of
Master of Science in Artificial Intelligence

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
3. 




The MIT License (MIT)

Copyright (c) 2022 Yesbol Gabdullin

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

