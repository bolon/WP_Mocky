import requests
import json

# Mock HTTP Resp 200
def test_ResponseOK():
    mockURL = "https://run.mocky.io/v3/058fcb1c-d573-4ce0-bcf1-40597481237d"
    headers = {'Content-Type': 'application/json' } 
    payload = {
        'prefix': 'PT',
        'name': 'Sejahtera',
        'suffix': 'Tbk',
        'industry_id': '1',
        'employee_size': '500',
        'street': 'Jl.Sudirman kav. 21',
        'place': 'Sudirman Tower',
        'geograph_id': 100,
        'phone': '08561290092'
    }
    
    expectedRespBody = {
      "data": {
        "company_id": 11
      },
      "message": "Resource has been created",
      "code": "STATUS_CREATED"
    }
    
    resp = requests.post(mockURL, headers=headers, data=json.dumps(payload,indent=4))
    assert resp.status_code == 200
    assert json.dumps(resp.json()) == json.dumps(expectedRespBody)
    
# Mock HTTP Resp 400
def test_ResponseBadRequest():
    url = "https://run.mocky.io/v3/f6a01737-54c9-4f0d-9990-35da6a05250c"
    headers = {'Content-Type': 'application/json' } 
    payload = {
        'prefix': 'PT',
        'name': 'Sejahtera',
        'suffix': 'Tbk',
        'industry_id': '1',
        'employee_size': '500',
        'street': 'Jl.Sudirman kav. 21',
        'place': 'Sudirman Tower',
        'geograph_id': 100,
        'phone': '08561290092'
    }
    
    expectedRespBody = {
      "message": "Check your payload",
      "code": "INVALID_PAYLOAD"
    }
    
    resp = requests.post(url, headers=headers, data=json.dumps(payload,indent=4))
    assert resp.status_code == 400
    assert json.dumps(resp.json()) == json.dumps(expectedRespBody)
    
# Mock HTTP Resp 404
def test_ResponseNotFound():
    url = "https://run.mocky.io/v3/3da2048d-0a9a-4b28-937c-8b3cb75f659c"
    headers = {'Content-Type': 'application/json' } 
    expectedRespBody = {
      "message": "Check path",
      "code": "INVALID_RESOURCE"
    }
    
    resp = requests.post(url, headers=headers)
    assert resp.status_code == 404
    assert json.dumps(resp.json()) == json.dumps(expectedRespBody)
    
# Mock HTTP Resp 500
def test_ResponseInternalServerError():
    url = "https://run.mocky.io/v3/dcf47b02-7b91-4b70-b665-1d16eb24c109"
    headers = {'Content-Type': 'application/json' } 
    expectedRespBody = {
      "message": "Something wrong",
      "code": "INTERNAL_SERVER_ERROR"
    }
    
    resp = requests.post(url, headers=headers)
    assert resp.status_code == 500
    assert json.dumps(resp.json()) == json.dumps(expectedRespBody)