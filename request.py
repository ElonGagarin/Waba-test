# import requests

# def first_Login():
#     return requests.post(
#         "https://0.0.0.0:9090/v1/users/login",
#         # auth=('Authorization', 'Basic base64(admin:secret)'),
#         headers={'Authorization': 'Basic base64(admin:secret)'},
#         data={"new_password": "Su12345"},
#         )
# print(first_Login())
# print('='*10)

# =========================
# First Login

# curl -k -X POST https://0.0.0.0:9090/v1/users/login \
#   -w "\n%{http-code}\n" \
#   -H 'Content-Type: application/json' \
#   -H 'Authorization: Basic base64(admin:secret)' \
#   -d '{"new_password" : "Su12345"}'


# Standard Login

# curl -X POST \
#   -H 'Authorization: Basic base64(admin:secret)' \
#   -H 'Content-Type: application/json' \
#   -d '{}' \
#   https://0.0.0.0:9090/v1/users/login

