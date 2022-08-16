book={}
book["tom"]={"name":"tom",
    "address":"green streat",
    "phone":9506908614
}
book["ashish"]={"name":"ashish",
    "address": "Gazipur",
    "phone": 8052628284
}

import json
s=json.dumps(book)
print(s)