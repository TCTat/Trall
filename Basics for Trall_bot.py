botToken = "168581170:AAEF8mbrsK9FI1sSR04ipEwYA7C1Yl8n_wQ";
website = "https://api.telegram.org/bot"+botToken;

updateLink = "https://api.telegram.org/bot"+botToken+"/getupdates"


import urllib2, json
update = urllib2.urlopen(updateLink).read()
updateDict = json.loads(update)


##Read 1st text message
text = updateDict["result"][0]["message"]["text"]

print text



##Read sender chatId
chatId = updateDict["result"][0]["message"]["chat"]["id"]
chatId = str(chatId)
print chatId


urllib2.urlopen(website+"/sendmessage?chat_id="+chatId+"&text=test").read()
