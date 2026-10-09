# Python FTP File Uploader

A robust, secure Python script for uploading files to a remote server using FTPS (FTP over TLS). This template uses environment variables to keep credentials secure and separate from the source code.

## Prerequisites

*   Python 3.6 or higher
*   An FTP server that supports TLS/SSL (`FTP_TLS`)
*   `python-dotenv` library installed

## Installation

1.  **Clone or download** this repository.
2.  **Install the required dependency:**
    ```bash
    pip install python-dotenv
    ```
3.  **Create your environment file:**
    Create a file named `.env` in the same directory as the script. Add your credentials:
    ```env
    FTP_HOST=ftp.your-server.com
    FTP_USER=your_ftp_username
    FTP_PASS=your_super_secret_password
    ```
    *Note: Ensure `.env` is added to your `.gitignore` to prevent leaking credentials.*

## Usage

1.  **Configure file paths:** Open the script and modify the `LOCAL_FILE_PATH` and `REMOTE_FILE_NAME` variables if necessary. The template creates a dummy local file for testing purposes.
2.  **Run the script:**
    ```bash
    python ftp_upload.py
    ```
