#!/usr/bin/python3

from urllib.request import urlopen

def get_request_id(url):
  """Fetches the X-Request-Id header from the given URL using urllib.

  Args:
      url: The URL to send the request to.

  Returns:
      The value of the X-Request-Id header, or None if not found.
  """
  with urlopen(url) as response:
    headers = response.headers
    if 'X-Request-Id' in headers:
      return headers['X-Request-Id']
    else:
      return None

if __name__ == "__main__":
  url = "https://www.example.com"  # Replace with your desired URL
  request_id = get_request_id(url)
  if request_id:
    print(f"X-Request-Id: {request_id}")
  else:
    print("X-Request-Id not found in response headers.")
