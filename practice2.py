import requests
import os

def download_file(url, save_path,max_retries=3):
    response = requests.get(url)
    retries=0
    while retries<max_retries:
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"File downloaded successfully to {save_path}")
        else:
            print(f"Failed to download file from {url} because of {status_code}")
            print("Retrying download......")
            retries+=1

def main():
    url = "http://example.com/samplefile.txt"  # Replace with the URL of the file you want to download
    save_path = "samplefile.txt"  # Replace with the path where you want to save the file

    if os.path.exists(save_path):
        print(f"File {save_path} already exists.")
    else:
        download_file(url, save_path)

if __name__ == "__main__":
    main()
