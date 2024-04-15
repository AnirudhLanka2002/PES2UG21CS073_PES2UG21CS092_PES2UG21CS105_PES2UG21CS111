import base64

data = "897308618510-qmll99e22kvomvij45e33773a5n0r5cv.apps.googleusercontent.com"
encoded_data = base64.b64encode(data.encode()).decode()
print(encoded_data)
