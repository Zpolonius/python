import urllib.request
import base64
import datetime
import os

# Set the base URL and initial ID value
base_url = ".altapaysecure.com/merchant.php/API/fundingDownload?id="

# Set the current date and format it for the URL
current_date = datetime.datetime.today().strftime('%Y-%m-%d')

# Set the filename to use for the downloaded file
folder_name = "funding filer"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

filename = os.path.join(folder_name, f"funding_{current_date}.csv")
#User inputs
# Set your Basic Authentication credentials
username = input('Enter username: ')
password = input('Enter the password: ')

# Ask the user for the ID value
id_value = int(input("Enter the ID value: "))

#Set the domain
domain_url = 'altapay'


# Encode the credentials as base64
auth = base64.encodebytes(f"{username}:{password}".encode()).decode().strip()

# Construct the full URL for the CSV file to download, including Basic Authentication
url = f"https://{domain_url}{base_url}{id_value}"
request = urllib.request.Request(url)
request.add_header("Authorization", f"Basic {auth}")

# Download the CSV file and save it to disk
with urllib.request.urlopen(request) as response:
    with open(filename, "wb") as file:
        file.write(response.read())

print(f"CSV file downloaded to {filename}")
print(url)
