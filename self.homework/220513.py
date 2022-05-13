
import pandas as pd
import numpy as np



print("###### X_train")
X_train = pd.read_csv('X_train.csv')
print(X_train.shape)
print(type(X_train))

print("###### X_train2")
X_train2 = X_train["tokenized"].squeeze()
print(type(X_train2))
print(X_train2.shape)

print("###### X_train3")
X_train3 = X_train2.values
print(X_train3[0])
print(type(X_train3[0]))
print(X_train3.shape)

print("###### X_train4")
X_train4 = []
print("#### Split 시작")
for str in X_train3:
    str = str.replace("[", "").replace("]", "").replace(" '", "").replace("'", "")
    X_train4.append(str.split(","))
print("#### Split 끝")
print(X_train4[0])
print(type(X_train4[0]))


X_train = X_train4.copy()