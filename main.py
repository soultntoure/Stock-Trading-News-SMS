import requests
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_KEY = "69QX3ONP057NI49Y"
NEWS_KEY = "0c9616339b5d41e9a26fbe02cbb109ae"

## STEP 1: Use https://www.alphavantage.co/query
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "outputsize" : "compact",
    "apikey" : STOCK_KEY,
}
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)

daily_data = stock_response.json()['Time Series (Daily)']
data_list = [value for (key,value) in daily_data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

before_yesterday_data = data_list[1]
before_yesterday_closing_price = before_yesterday_data["4. close"]

positive_difference = abs(float(yesterday_closing_price) - float(before_yesterday_closing_price))
print(positive_difference)
diff_percentage = (positive_difference / float(yesterday_closing_price)) * 100
print(diff_percentage)



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
news_params = {
    "apiKey" : NEWS_KEY,
    "qInTitle": COMPANY_NAME,
    "pageSize": 3,
    "sortBy": "publishedAt",
}
news_response = requests.get(NEWS_ENDPOINT, params=news_params)
articles = news_response.json()['articles']
print(articles)


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

