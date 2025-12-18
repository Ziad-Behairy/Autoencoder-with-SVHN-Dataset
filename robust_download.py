#!/usr/bin/env python3
import requests
import os
from tqdm import tqdm

def download_with_progress(url, filename):
    """Download file with progress bar and resume support"""
    if os.path.exists(filename):
        file_size = os.path.getsize(filename)
        print(f"{filename} already exists ({file_size/(1024**2):.1f} MB)")
        if file_size > 1000000:  # If > 1MB, assume it's complete
            return True

    try:
        print(f"Downloading {filename} from {url}...")

        # Try with requests (better than urllib)
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()

        total_size = int(response.headers.get('content-length', 0))

        with open(filename, 'wb') as f:
            if total_size == 0:
                f.write(response.content)
            else:
                with tqdm(total=total_size, unit='B', unit_scale=True) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            pbar.update(len(chunk))

        print(f"✓ Downloaded {filename} ({os.path.getsize(filename)/(1024**2):.1f} MB)")
        return True

    except Exception as e:
        print(f"✗ Failed to download {filename}: {e}")
        if os.path.exists(filename):
            os.remove(filename)
        return False

# Alternative mirrors for SVHN dataset
urls = [
    ('http://ufldl.stanford.edu/housenumbers/train_32x32.mat', 'train_32x32.mat'),
    ('http://ufldl.stanford.edu/housenumbers/test_32x32.mat', 'test_32x32.mat'),
]

success_count = 0
for url, filename in urls:
    if download_with_progress(url, filename):
        success_count += 1

if success_count == 2:
    print(f"\n✓ All files downloaded successfully!")
else:
    print(f"\n✗ Only {success_count}/2 files downloaded")
