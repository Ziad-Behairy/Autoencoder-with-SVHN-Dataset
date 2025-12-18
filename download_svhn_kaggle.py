#!/usr/bin/env python3
import kagglehub
import os
import shutil

print("Downloading SVHN dataset from Kaggle...")
path = kagglehub.dataset_download("stanfordu/street-view-house-numbers")
print(f"Dataset downloaded to: {path}")

# List files
print("\nFiles in dataset:")
for root, dirs, files in os.walk(path):
    for file in files:
        filepath = os.path.join(root, file)
        filesize = os.path.getsize(filepath) / (1024*1024)  # MB
        print(f"  {file} ({filesize:.1f} MB)")

        # Copy .mat files to current directory
        if file.endswith('.mat'):
            dest = os.path.join(os.getcwd(), file)
            print(f"  Copying to {dest}")
            shutil.copy2(filepath, dest)

print("\n✓ SVHN dataset ready!")
