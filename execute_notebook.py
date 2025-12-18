#!/usr/bin/env python3
import nbformat
from nbclient import NotebookClient
import sys

# Read the notebook
with open('autoencoder_svhn.ipynb', 'r') as f:
    nb = nbformat.read(f, as_version=4)

# Execute the notebook
print("Starting notebook execution...")
print("This will take approximately 15-20 minutes...")
print("=" * 60)

client = NotebookClient(
    nb,
    timeout=3600,
    kernel_name='python3'
)

try:
    client.execute()
    print("\n" + "=" * 60)
    print("Notebook executed successfully!")

    # Save the executed notebook
    with open('autoencoder_svhn.ipynb', 'w') as f:
        nbformat.write(nb, f)

    print("Executed notebook saved!")

except Exception as e:
    print(f"\nError during execution: {e}")
    # Still save the notebook with partial results
    with open('autoencoder_svhn.ipynb', 'w') as f:
        nbformat.write(nb, f)
    sys.exit(1)
