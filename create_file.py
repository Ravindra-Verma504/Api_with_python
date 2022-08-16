import requests,json
url=requests.get("http://saral.navgurukul.org/api/courses").json()
with open("course.json","w") as obj:
    json.dump(url,obj,indent=4)
    print("data sent successfully..")