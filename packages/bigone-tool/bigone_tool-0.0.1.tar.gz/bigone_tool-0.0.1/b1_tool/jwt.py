import jwt
import time

# GET bigone api JWT
def get_jwt(key, secret_key):
	current_time = str(time.time_ns())
	data = {"type" : "OpenAPIV2", "sub" : key, "nonce": current_time}
	secret = secret_key
	data_signed = jwt.encode(data, secret, algorithm = "HS256").decode()
	bearer_token = 'Bearer ' + data_signed
	return bearer_token