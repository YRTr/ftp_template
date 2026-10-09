import os
from ftplib import FTP_TLS, error_perm
from dotenv import load_dotenv

# Load variable from the .env file
load_dotenv()

# 1. Fetch FTP configuration securely
FTP_HOST = os.getenv("FTP_HOST")
FTP_USER = os.getenv("FTP_USER")
FTP_PASS = os.getenv("FTP_PASS")

# The File you want to upload and what it should be named on the server
LOCAL_FILE_PATH = 'text_document.txt'
REMOTE_FILE_NAME = 'uploaded_document.txt'

# Create a dummy file locally just so the script has something to upload
with open(LOCAL_FILE_PATH, "w") as f:
    f.write("This is a test file being sent via Python FTP.")

# 2. Connect and upload
try:
    # Initialize the TLS (secure) connection to the host
    print(F"Connectiong to {FTP_HOST}....")
    with FTP_TLS(FTP_HOST) as ftp:
        # Authenticate
        ftp.login(user=FTP_USER, passwd=FTP_PASS)

        # Upgrade the data connection to secure mode (Crucial for FTPS)
        ftp.prot_p()
        print("Authentication successful. Secure connection established.")

        # Navigate to a specific directory if needed (optional)
        # ftp.cwd("/public_html/uploads")

        # Open the local file in binary read mode ('rb')
        with open(LOCAL_FILE_PATH, "rb") as file:
            # Use storbinary to upload the file
            # The Command format is "STOR <filename>"
            print(f"Uploading {LOCAL_FILE_PATH}...")
            ftp.storbinary(f"STOR {REMOTE_FILE_NAME}", file)

        print("File successfully uploaded!")

except error_perm as e:
    print(f"FTP Permission/Authentication error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")