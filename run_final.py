#!/usr/bin/env python3
import nbformat
from nbclient import NotebookClient

# Read notebook
with open('autoencoder_svhn_final.ipynb', 'r') as f:
    nb = nbformat.read(f, as_version=4)

# Execute
print("=" * 60)
print("EXECUTING AUTOENCODER NOTEBOOK")
print("=" * 60)
print("This will train two models (latent 64 and 16) for 50 epochs each")
print("Estimated time: 15-20 minutes total")
print("=" * 60)

client = NotebookClient(nb, timeout=3600, kernel_name='python3')

try:
    client.execute()
    print("\n" + "=" * 60)
    print("✓ EXECUTION COMPLETED SUCCESSFULLY!")
    print("=" * 60)

    # Save executed notebook
    with open('autoencoder_svhn_final.ipynb', 'w') as f:
        nbformat.write(nb, f)

    print("Saved fully executed notebook: autoencoder_svhn_final.ipynb")

except Exception as e:
    print(f"\n✗ Error: {e}")
    # Save partial results
    with open('autoencoder_svhn_final.ipynb', 'w') as f:
        nbformat.write(nb, f)
    raise
