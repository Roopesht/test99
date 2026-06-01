import requests

# Install requests if needed: pip install requests

# Make a simple GET request
response = requests.get('https://ojasamiraskljdfljkasdi.com')

# Check the response
print(f"Status Code: {response.status_code}")
print(f"Headers: {response.headers['Content-Type']}")
print(f"Response Text: {response.text[:200]}...")
