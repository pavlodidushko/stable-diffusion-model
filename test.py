import requests

# Define the GraphQL query and variables as a dictionary
graphql_request = {'query': 'mutation UpdateImagesGeneration($data: ImageGenerationInput!) { updateImagesGeneration(data: $data) { status }}', 'variables': {'data': {'images': [{'url': 'http://173.208.151.203:9999/files/2024-05-16/2ab452c3-b828-4ef3-be24-faba43af032d.png', 'prompt': 'Preppy Beautiful'} ], 'isUserInput': True}}}

# Define the headers
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer" + " " +  "d7093c26-f508-47e4-833c-757706a62bfd", #userID
    "Cookie": "jgb_cs=s%3A96Q5_rfHS3EaRCEV6iKlsX7u_zm4naZD.yKB%2BJ35mmaGGryviAAagXeCrvkyAC9K4rCLjc4Xzd8c"
}
# Define the GraphQL API endpoint
url = "https://stage-graphql.beautifultechnologies.app/"
# Send the HTTP request using the `requests` library
response = requests.post(url, json=graphql_request, headers=headers)
# Print the response content and status code
print(response.content)
print(response.status_code)