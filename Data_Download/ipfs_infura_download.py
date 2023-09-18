# Script to download a file from IPFS Infura

import requests

def download_file_from_ipfs_infura(ipfs_hash, infura_api_key):
  """Downloads a file from IPFS Infura.

  Args:
    ipfs_hash: The IPFS hash of the file to download.
    infura_api_key: The Infura API key.

  Returns:
    The downloaded file as a bytes object.
  """

  headers = {
    "Authorization": f"Bearer {infura_api_key}"
  }

  response = requests.get(
    f"https://ipfs.infura.io/v0/cat/{ipfs_hash}",
    headers=headers
  )

  response.raise_for_status()

  return response.content


# Example usage:

ipfs_hash = "QmHashHere"
infura_api_key = "YOUR_INFURA_API_KEY"

file_content = download_file_from_ipfs_infura(ipfs_hash, infura_api_key)

# Write the file content to a file.
with open("downloaded_file.txt", "wb") as f:
  f.write(file_content)
