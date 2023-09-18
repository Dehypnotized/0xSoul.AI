# Script to download a file from Ocean Protocol

import requests
import json

def download_file_from_ocean_protocol(data_asset_id, ocean_api_key):
  """Downloads a file from Ocean Protocol.

  Args:
    data_asset_id: The ID of the data asset to download.
    ocean_api_key: The Ocean API key.

  Returns:
    The downloaded file as a bytes object.
  """

  headers = {
    "Authorization": f"Bearer {ocean_api_key}"
  }

  response = requests.get(
    f"https://api.oceanprotocol.com/v1/dataassets/{data_asset_id}/download",
    headers=headers
  )

  response.raise_for_status()

  data = json.loads(response.content)

  return data["fileContent"]


# Example usage:

data_asset_id = "1234567890ABCDEF"
ocean_api_key = "YOUR_OCEAN_API_KEY"

file_content = download_file_from_ocean_protocol(data_asset_id, ocean_api_key)

# Write the file content to a file.
with open("downloaded_file.txt", "wb") as f:
  f.write(file_content)
