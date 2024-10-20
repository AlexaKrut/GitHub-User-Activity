import argparse
import json
import requests

def fetch_github_activity(username):
  url = f'https://api.github.com/users/{username}/events'
  response = requests.get(url)

  if response.status_code == 200:
      data = response.json()
      return data
  else:
      print(f'Error: {response.status_code}')
      return None

def format_activity(events):
  output = []
  
  for event in events:
      event_type = event['type']
      repo_name = event['repo']['name']
      createdAt = event['created_at']
      
      if event_type == 'PushEvent':
          commit_count = len(event['payload']['commits'])
          output.append(f'Pushed {commit_count} commits to {repo_name} at {createdAt}')
      elif event_type == 'CreateEvent':
          output.append(f'Created a new repository or branch in {repo_name} at {createdAt}')
      elif event_type == 'IssuesEvent':
          output.append(f'Opened a new issue in {repo_name} at {createdAt}')
      elif event_type == 'WatchEvent':
          output.append(f'Starred {repo_name} at {createdAt}')

  return output

def main():
    parser = argparse.ArgumentParser('GitHub Username')
    parser.add_argument('username', type=str, help='GitHub username')
    args = parser.parse_args()
    username = args.username

    events = fetch_github_activity(username)
    if events:
        activity_output = format_activity(events)
        for line in activity_output:
            print(line)


if __name__ == '__main__':
    main()
