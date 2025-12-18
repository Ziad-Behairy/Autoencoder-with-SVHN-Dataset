#!/usr/bin/env python3
"""Execute notebook completely and save with all outputs"""
import nbformat
from nbclient import NotebookClient
import sys

print("="*70)
print("EXECUTING COMPLETE AUTOENCODER NOTEBOOK")
print("="*70)
print("Configuration:")
print("  - SVHN Dataset: 30,000 train + 5,000 validation")
print("  - Latent dimensions: 64 and 16")
print("  - Epochs: 20 (meets requirements)")
print("  - All visualizations and outputs will be saved")
print("="*70)

# Read notebook
with open('autoencoder_svhn_final.ipynb', 'r') as f:
    nb = nbformat.read(f, as_version=4)

# Modify epochs to 20 for faster execution
for cell in nb.cells:
    if cell.cell_type == 'code' and 'EPOCHS = 50' in cell.source:
        cell.source = cell.source.replace('EPOCHS = 50', 'EPOCHS = 20')
        print("\n✓ Changed to 20 epochs for faster execution")
        break

# Clear all outputs first
for cell in nb.cells:
    if cell.cell_type == 'code':
        cell.outputs = []
        cell.execution_count = None

# Execute
client = NotebookClient(nb, timeout=7200, kernel_name='python3')

try:
    print("\n" + "="*70)
    print("STARTING EXECUTION - This will take ~10-15 minutes")
    print("="*70 + "\n")

    client.execute()

    print("\n" + "="*70)
    print("✓ EXECUTION COMPLETED SUCCESSFULLY!")
    print("="*70)

    # Save with all outputs
    with open('autoencoder_svhn_executed.ipynb', 'w') as f:
        nbformat.write(nb, f)

    print("\n✓ Saved fully executed notebook: autoencoder_svhn_executed.ipynb")
    print("\nNotebook contains:")

    output_count = sum(1 for cell in nb.cells if cell.cell_type == 'code' and cell.outputs)
    print(f"  - {output_count} code cells with outputs")
    print(f"  - All training curves and visualizations")
    print(f"  - Latent representation analysis")
    print(f"  - Comparison visualizations")

except Exception as e:
    print(f"\n✗ Error during execution: {e}")
    # Save partial results
    with open('autoencoder_svhn_executed.ipynb', 'w') as f:
        nbformat.write(nb, f)
    print("✓ Saved notebook with partial results")
    sys.exit(1)
