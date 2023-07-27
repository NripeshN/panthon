# random_string_generator.py
import torch
import torch.nn as nn
import random
import string


class RandomStringGenerator(nn.Module):
    def __init__(self, length):
        super(RandomStringGenerator, self).__init__()
        self.length = length

    def forward(self, x):
        return "".join(
            random.choices(string.ascii_uppercase + string.digits, k=self.length)
        )
