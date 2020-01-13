# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
index = 0
list_num = len(headlines)
news_len = 0
# write your loop here
while index < list_num:
    news_ticker += headlines[index]+" "
    if len(news_ticker) > 140:
        news_ticker=news_ticker[:140]
        break
    index += 1
print(len(news_ticker))
print(news_ticker)