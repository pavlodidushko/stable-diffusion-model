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

if __name__ == "__main__":
    public_ip = get_public_ip()
    if public_ip:
        print("Public IP address:", public_ip)
    else:
        print("Failed to retrieve public IP address.")
