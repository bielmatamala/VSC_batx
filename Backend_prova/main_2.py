import requests

SERVER_IP = "192.168.232.167"  # PC A's IP Address
url = f"http://{SERVER_IP}:8000/transf"

response = requests.get(url)

if response.status_code == 200:
    with open("received_file.zip", "wb") as f:
        f.write(response.content)
    print("File downloaded successfully!")
else:
    print("Failed to download file.")