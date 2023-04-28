import pytube
from tqdm import tqdm
import time


def progress_function(stream, chunk, bytes_remaining):
    current_progress = (total_size - bytes_remaining) / total_size
    progress_bar.update(len(chunk))

# defining the download location as current working directory
download_loc = './'

video_url = input('Enter URL: ')

video_instance = pytube.YouTube(video_url)

# Using register_on_progress_callback to define custom function that will be called whenever
# there's a progress update in the download process.
video_instance.register_on_progress_callback(progress_function)

# Get the stream of the highest Resolution available on youtube
stream = video_instance.streams.get_highest_resolution()
total_size = stream.filesize

print("Downloading...")

# Adding the progress bar into the output window
# creates a progress bar with 'tqdm'and displays progress of download as it happens in real time.

with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024**2, desc="Downloading video") as progress_bar:

    # This block of code records the start time and downloads the file to specified location using 'stream.download()'.
    # Once download is complete, end time is recorded.
    start_time = time.time()
    stream.download(download_loc)
    end_time = time.time()


download_speed = total_size / (end_time - start_time) / (1024 ** 2)
print(f"Download completed. Download speed: {download_speed:.2f} MB/s")

