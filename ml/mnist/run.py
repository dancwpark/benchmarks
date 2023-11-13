import numpy as np
import torch
import torch.nn.functional as F
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import torchvision.datasets as dataset
import torchvision.transforms as transforms
import argparse
import time


def parse_args():
    parsed = argparse.ArgumentParser()
    parsed.add("-d", "--device",
               default="cpu")

    args = parsed.parse_args()
    return args

def one_hot(x, K):
    return np.array(x[:, None] == np.arange(K)[None, :], dtype=int)





def main():
    args = parse_args()
    if args.device == 'cpu':
        device = 'cpu'
    elif args.device == 'gpu':
        device = 'cuda:0'
    elif args.device == 'apple':
        device = 'mps'




if __name__ = '__main__':
    main()
