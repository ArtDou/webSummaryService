import requests
def requests_model(text_to_summarize):
 model_port= 5000
 url = f"http://wym_model:{model_port}/model/predict"
 headers = {"Content-Type": "application/json; charset=utf-8","accept": "application/json"}
 json = {"text":[text_to_summarize]}
 res = requests.post(url,  headers=headers, json=json)
 if res.status_code == 200:
  return res.json()['summary_text'][0]
 else:   
   return f"status_code:{res.status_code}"    