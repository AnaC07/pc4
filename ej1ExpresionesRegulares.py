
import re
path = './src/re/short_tweets.csv'

s = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'
print(re.findall(r"@\w+\W*\w+",s))
