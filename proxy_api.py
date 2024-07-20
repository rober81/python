import requests
from requests.auth import HTTPBasicAuth
from fastapi import FastAPI, Query, Request
import uvicorn
import json

app = FastAPI()
ip_original = "http://10.7.232.113/"

def api_call(url, headers=None):
    print(f"Llamando api: {url}")
    if headers:
        #print(f"headers: {headers}")
        response = requests.get(f'{url}', headers=headers)
    print(f"Status_code: {response.status_code}")
    return response

@app.get("/{path_param:path}")
async def handle_path(path_param: str, request: Request):
    print(f"path_param: {path_param}")
    param_url = str(request.url).split(path_param)[1]
    response = api_call(f"{ip_original}{path_param}{param_url}", request.headers)
    modified_response = modify_key(response, "tag", "proxy_api7")
    #print(json.dumps(modified_response, indent=4))
    return modified_response

def modify_key(response, key, value):
    json_data = None
    try:
        json_data = json.loads(response.content)
        if isinstance(json_data, list):
            for item in json_data:
                item[key] = value
        else:
            raise ValueError("response_json must be a list")
    except json.JSONDecodeError:
        pass
    if json_data is None:
        json_data = response.content
    return json_data

if __name__ == '__main__':
    uvicorn.run("proxy_api:app", port=80, reload=True)