from keras.layers import Dense, Dropout, Activation
from keras.models import Sequential
import pandas as pd
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def istarget(csv):
    # for idx, val in enumerate(csv['sex']):
    #     if val == 'male':
    #         csv['sex'].copy()[idx] = 1
    #     else:
    #         csv['sex'].copy()[idx] = 0

    # np.where(csv['sex'] == 'male', 1, 0)
    csv.loc[csv['sex'] == 'male', 'sex'] = 1
    csv.loc[csv['sex'] == 'female', 'sex'] = 0
    csv["age"] = (csv["age"] - min(csv["age"])) / (max(csv["age"]) - min(csv["age"]))
    csv["distance"] = (csv["distance"] - min(csv["distance"])) / (max(csv["distance"]) - min(csv["distance"]))
    csv["impression"] = (csv["impression"] - min(csv["impression"])) / (max(csv["impression"]) - min(csv["impression"]))
    csv["click"] = (csv["click"] - min(csv["click"])) / (max(csv["click"]) - min(csv["click"]))
    csv["conversion"] = (csv["conversion"] - min(csv["conversion"])) / (max(csv["conversion"]) - min(csv["conversion"]))

    # SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame
    # for idx, val in enumerate(csv['issingle_household']):
    #     if val:
    #         csv['issingle_household'].copy()[idx] = 1
    #     else:
    #         csv['issingle_household'].copy()[idx] = 0
    # np.where(csv['issingle_household'], 1, 0)
    csv.loc[csv['issingle_household'], 'issingle_household'] = 1
    csv.loc[csv['issingle_household'] == False, 'issingle_household'] = 0
    # print(csv)
    x = csv[["sex", "age", "distance", "issingle_household", "impression", "click", "conversion"]].to_numpy()
    # print(x)
    targeting_class = {
        True: [1, 0],
        False: [0, 1]
    }
    y = np.empty((len(csv), 2))

    for idx, value in enumerate(csv["targeting"]):
        y[idx] = targeting_class[value]

    x_train, y_train = x[1:71], y[1:71]
    x_test, y_test = x[71:], y[71:]
    print('x_train')
    print(x_train)
    print('y_train')
    print(y_train)
    # print(len(x_train), len(y_train))

    model = Sequential()
    model.add(Dense(512, input_dim=7))
    model.add(Activation('relu'))
    model.add(Dropout(0.1))
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.1))
    model.add(Dense(2))
    model.add(Activation('sigmoid'))
    model.compile("rmsprop", "categorical_crossentropy", metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=30, batch_size=1)

    score = model.evaluate(x_test, y_test)
    y_predict = model.predict(x_test)
    print('y_predict')
    print(y_predict)
    print('y_test')
    print(y_test)
    print("score:", score)
    return

csv = pd.read_csv("KAKAO_data.csv")
istarget(csv)
