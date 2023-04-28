# Pytube Video Downloader
- This is a simple Python script that downloads videos from YouTube using the Pytube library. The script is interactive and allows you to enter a YouTube video URL of your choice, and then it downloads the video to your current working directory.

# Prerequisites
- Python 3.6 or above
- Pytube Library (can be installed via pip)

# Usage
- Clone the repository to your local machine or download the zip file and extract it.
- Open a terminal and navigate to the directory containing the script.
- Install Pytube library via pip using the command: pip install pytube
- Run the script using the command: python pytube_downloader.py
- Enter the YouTube video URL when prompted and hit enter.
- The script will download the video to your current working directory and display a progress bar showing the download progress.
- Once the download is complete, the script will display the download speed.
# Customization
- The script downloads the video to the current working directory by default. If you want to change the download location, simply modify the download_loc variable at the beginning of the script.
- You can modify the progress bar using the tqdm library's parameters.
