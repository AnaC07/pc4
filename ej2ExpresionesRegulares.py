import re
cadena =  "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"
print(re.findall(r"User_mentions:\d",cadena))

print(re.findall(r"likes:\s\d",cadena))

print(re.findall(r"number\sof\sretweets:\s\d",cadena))