import requests

test=requests.get("http://saral.navgurukul.org/api/courses/74/exercises")
test2=test.text
print(test2)