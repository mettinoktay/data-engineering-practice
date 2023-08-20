import requests
import pandas
import os

from pathlib import Path

download_url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
download_path = Path(__file__).parent / "downloads"
def main():
    print(download_path)
    
    try:
        os.mkdir(download_path)
        print("downloads folder created.")
    except FileExistsError:
        print("Folder already exists. Continuing.")

    os.chdir(download_path)
    input("download about to start")
    with open("weather_data", "wb") as f:
        f.write(requests.get(download_url, allow_redirects=True).content)
    
    print("Download complete.")
    
    
if __name__ == "__main__":
    main()
