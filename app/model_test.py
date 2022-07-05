import requests
res_get=requests.get('http://localhost:5000/model/metadata')
print(res_get.status_code)
payload = res_get.json()
print(payload)
##payload2 = res_get.text 
#print('text',res_get.text)
print(res_get.headers['Content-Type'])

text_to_summarize = input("Please enter your text: ")

res=requests.post("http://localhost:5000/model/predict", json={
  "text": [
    text_to_summarize
  ]
})
print(res.status_code)
print(res.text)