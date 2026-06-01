import requests
from datetime import datetime

def get_github_user_info(username):
    """Fetch and process GitHub user information"""
    url = f"https://api.github.com/users/{username}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            user_data = response.json()
            
            # Extract and format information
            info = {
                'name': user_data.get('name', 'No name provided'),
                'username': user_data['login'],
                'followers': user_data['followers'],
                'public_repos': user_data['public_repos'],
                'created_at': user_data['created_at'][:10],  # Format date
                'bio': user_data.get('bio', 'No bio available')
            }
            
            return info
        else:
            return {'error': f'User not found (Status: {response.status_code})'}
            
    except requests.RequestException as e:
        return {'error': f'Network error: {str(e)}'}

# Test the function
user_info = get_github_user_info('roopesht')
print("👤 GitHub User Info:")
for key, value in user_info.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
    