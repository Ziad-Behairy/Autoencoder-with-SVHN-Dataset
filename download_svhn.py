#!/usr/bin/env python3
"""Download SVHN dataset from working source"""
import os
import sys

try:
    # Try using torchvision to download SVHN
    import torchvision
    import numpy as np
    from scipy.io import savemat

    print("Downloading SVHN dataset using torchvision...")

    # Download train set
    train_dataset = torchvision.datasets.SVHN(
        root='./data',
        split='train',
        download=True
    )

    # Download test set
    test_dataset = torchvision.datasets.SVHN(
        root='./data',
        split='test',
        download=True
    )

    print("Converting to .mat format...")

    # Convert train to mat format
    train_data = train_dataset.data.transpose(0, 2, 3, 1)  # NCHW -> NHWC
    train_labels = train_dataset.labels

    # Transpose to HWCN for MATLAB format
    train_X = train_data.transpose(1, 2, 3, 0)

    savemat('train_32x32.mat', {'X': train_X, 'y': train_labels.reshape(-1, 1)})
    print(f"Saved train_32x32.mat with {train_data.shape[0]} images")

    # Convert test to mat format
    test_data = test_dataset.data.transpose(0, 2, 3, 1)  # NCHW -> NHWC
    test_labels = test_dataset.labels

    # Transpose to HWCN for MATLAB format
    test_X = test_data.transpose(1, 2, 3, 0)

    savemat('test_32x32.mat', {'X': test_X, 'y': test_labels.reshape(-1, 1)})
    print(f"Saved test_32x32.mat with {test_data.shape[0]} images")

    print("Dataset download complete!")

except ImportError:
    print("torchvision not installed. Installing...")
    os.system("python3 -m pip install --user torch torchvision --index-url https://download.pytorch.org/whl/cpu")
    print("Please run this script again")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
