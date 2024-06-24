import torch
import torch.nn as nn


# convert list to tensor
# data = torch.Tensor([1, 2, 3, 4, 5])
#
# softmax_func = nn.Softmax(dim=0)
# output = softmax_func(data)


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        total = x_exp.sum(0, keepdim=True)
        return x_exp / total


class SoftMaxStable(nn.Module):
    def __init__(self):
        super(SoftMaxStable, self).__init__()

    def forward(self, x):
        x_exp = torch.exp(x - torch.max(x))
        total = x_exp.sum(0, keepdim=True)
        return x_exp / total


data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)

softmax_stable = SoftMaxStable()
output_stable = softmax_stable(data)
print(output_stable)
