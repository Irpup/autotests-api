import httpx

payload = {
  "email": "irina@example.com",
  "password": "123"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)
login_response_data = login_response.json()
print("Login response:", login_response.json())
print("Status Code:", login_response.status_code)


headers_get = {
          "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
          }
user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers_get)
end_user_response = user_response.json()
print("Get user:", end_user_response)
print("Status Code:", user_response.status_code)
