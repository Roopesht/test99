import requests
import json

# Using a free API - JSONPlaceholder
url = "https://jsonplaceholder.typicode.com/posts/1"

# Make GET request
response = requests.get(url)

if response.status_code == 200:
    # Parse JSON response
    data = response.json()  # Shortcut for json.loads(response.text)
    
    print("📄 Post Details:")
    print(f"Title: {data['title']}")
    print(f"Body: {data['body'][:100]}...")
    print(f"User ID: {data['userId']}")
else:
    print(f"❌ Error: {response.status_code}")
    