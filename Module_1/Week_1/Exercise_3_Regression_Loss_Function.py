import math
import random


def valid_int_number():
    while True:
        try:
            var = int(input(">> Input number of samples ( integer number ) which are generated: "))
            return var
        except ValueError:
            print("Number of samples must be an integer number")


def choose_loss_name():
    while True:
        var = input("Input loss name: ").upper()
        if var != "MSE" and var != "MAE" and var != "RMSE":
            print("Invalid input. Please enter MSE, MAE, or RMSE.")
            continue
        else:
            return var


def mae(pred, tar):
    return abs(pred - tar)


def rmse(pred, tar):
    return math.sqrt(mse(pred, tar))


def mse(pred, tar):
    return (pred - tar) ** 2


num_samples = valid_int_number()
loss_name = choose_loss_name()
for i in range(num_samples):
    predict = random.uniform(0.0, 10.0)
    target = random.uniform(0.0, 10.0)
    if loss_name == "MSE":
        loss = mse(predict, target)
    elif loss_name == "MAE":
        loss = mae(predict, target)
    else:
        loss = rmse(predict, target)
    print(f"loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {loss}")
