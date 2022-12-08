# Import the necessary modules
import fitbit
import oauth2

# Define a function that accesses the Fitbit API
def access_fitbit_api(client_id, client_secret, access_token, refresh_token):
  # Create a Fitbit client using the OAuth2 credentials
  client = fitbit.Fitbit(client_id, client_secret, oauth2=True, access_token=access_token, refresh_token=refresh_token)

  # Use the Fitbit client to access the API
  response = client.activities()

  # Print the response from the API
  print(response)

# Call the access_fitbit_api function using the Fitbit API credentials
access_fitbit_api('CLIENT_ID', 'CLIENT_SECRET', 'ACCESS_TOKEN', 'REFRESH_TOKEN')


# same for whoop
##################################

# Import the necessary modules
import requests

# Define a function that accesses the Whoop API
def access_whoop_api(access_token):
  # Set the base URL for the Whoop API
  base_url = 'https://api.whoop.com/'

  # Set the headers for the API request
  headers = {
    'Authorization': 'Bearer ' + access_token
  }

  # Send a GET request to the Whoop API to retrieve the user's data
  response = requests.get(base_url + 'user', headers=headers)

  # Print the response from the API
  print(response.json())

# Call the access_whoop_api function using the Whoop API access token
access_whoop_api('ACCESS_TOKEN')