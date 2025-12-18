import urllib.request
import ssl

# Create unverified SSL context for downloads
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = {
    'train': 'http://ufldl.stanford.edu/housenumbers/train_32x32.mat',
    'test': 'http://ufldl.stanford.edu/housenumbers/test_32x32.mat'
}

for name, url in urls.items():
    filename = f'{name}_32x32.mat'
    print(f"Downloading {filename}...")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"✓ Downloaded {filename}")
    except Exception as e:
        print(f"✗ Failed to download {filename}: {e}")
