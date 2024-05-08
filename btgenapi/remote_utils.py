import requests

def get_public_ip():
    try:
        # Send a GET request to httpbin.org/ip to retrieve the public IP address
        response = requests.get('https://httpbin.org/ip')
        # Parse the JSON response and extract the IP address
        ip_address = response.json()['origin']
        return ip_address
    except Exception as e:
        print("Failed to retrieve public IP address:", e)
        return None

