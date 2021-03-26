import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjExNzY0NjI3LCJqdGkiOiIzM2FjMzVjM2JmNGM0ZmZkYmVhYjRlZDA3ZTIzZmVlMCIsInVzZXJfaWQiOjF9.WeP7X11gFte_yMGZt_CbTLbYpoyQDlqJ2XdIEoFYQxs'

req = requests.get('http://localhost:8000/programmers/', headers=headers)

print(req.text)