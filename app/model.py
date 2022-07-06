import requests

text_to_summarize = input("Please enter your text: ")

res=requests.post("http://localhost:5000/model/predict", json={
  "text": [
    text_to_summarize
  ]
})
print(res.status_code)
print('Text summarized',res.text)
print('Info headers:',res.headers)