# import numpy as np
#
# x = np.array([i for i in range(1, 11)])
# y = np.array([i for i in range(1, 11)])
#
# x_train = x[:7]
# y_train = y[:7]
# x_test = x[7:]
# y_test = y[7:]
#
# print(x_train)
# print(x_test)
#
# from keras.layers import Dense, Activation # 활성함수
# from keras.models import Sequential
#
# model = Sequential()
# model.add(Dense(10000, input_dim = 1, activation='relu'))
# model.add(Dense(5, activation='relu'))
# model.add(Dense(1))
#
# model.compile(loss='mse', optimizer='adam')
#
# model.fit(x_train, y_train, epochs=100, batch_size=1)
#
# y_predict = model.predict(x_test)
# print(y_predict)
#
# from sklearn.metrics import r2_score
# r2_predict = r2_score(y_test, y_predict)
# print('R2:', r2_predict)

import csv
fp = open('KAKAO_data.csv', 'r', encoding='utf-8')
rdr = csv.reader(fp)

first_line = True
for line in rdr:
    if first_line:
        first_line = False
        continue

    if int(line[2]) <= 25:
        if int(line[3]) <= 500:
            if line[4] == 'TRUE':
                if int(line[5]) <= 5:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)

            else:
                if int(line[5]) <= 5:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)

        elif int(line[3]) <= 1000:
            if line[4] == 'TRUE':
                if int(line[5]) <= 5:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)
            else:
                if int(line[5]) <= 5:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)

        elif int(line[3]) <= 1500:
            if line[4] == 'TRUE':
                if int(line[5]) <= 5:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)
            else:
                if int(line[5]) <= 5:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)

        elif int(line[3]) <= 2000:
            if line[4] == 'TRUE':
                if int(line[5]) <= 5:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.3 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)
            else:
                if int(line[5]) <= 5:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.3 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)


        elif int(line[3]) <= 2500:
            if line[4] == 'TRUE':
                if int(line[5]) <= 5:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.3 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)
            else:
                if int(line[5]) <= 5:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.3 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)

        else:
            if line[4] == 'TRUE':
                if int(line[5]) <= 5:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.3 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)
            else:
                if int(line[5]) <= 5:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.3 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)


    elif int(line[2]) <= 35:
        if int(line[3]) <= 500:
            if line[4] == 'TRUE':
                if int(line[5]) <= 5:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)

            else:
                if int(line[5]) <= 3:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)

        elif int(line[3]) <= 1000:
            if line[4] == 'TRUE':
                if int(line[5]) <= 5:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)
            else:
                if int(line[5]) <= 3:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)

        elif int(line[3]) <= 1500:
            if line[4] == 'TRUE':
                if int(line[5]) <= 3:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)
            else:
                if int(line[5]) <= 2:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)

        elif int(line[3]) <= 2000:
            if line[4] == 'TRUE':
                if int(line[5]) <= 2:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.3 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)
            else:
                if int(line[5]) <= 1:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.3 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)


        elif int(line[3]) <= 2500:
            if line[4] == 'TRUE':
                if int(line[5]) <= 2:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.3 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)
            else:
                if int(line[5]) <= 1:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.3 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)

        else:
            if line[4] == 'TRUE':
                if int(line[5]) <= 2:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.3 or int(line[7]) > 1:
                    print(True)
                else:
                    print(False)
            else:
                if int(line[5]) <= 1:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.3 or int(line[7]) > 1:
                    print(True)
                else:
                    print(False)


    else:
        if int(line[3]) <= 500:
            if line[4] == 'TRUE':
                if int(line[5]) == 0:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)

            else:
                if int(line[5]) == 0:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)

        elif int(line[3]) <= 1000:
            if line[4] == 'TRUE':
                if int(line[5]) == 0:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)

            else:
                if int(line[5]) == 0:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)

        elif int(line[3]) <= 1500:
            if line[4] == 'TRUE':
                if int(line[5]) == 0:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)

            else:
                if int(line[5]) == 0:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)

        elif int(line[3]) <= 2000:
            if line[4] == 'TRUE':
                if int(line[5]) == 0:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)

            else:
                if int(line[5]) == 0:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.2 or int(line[7]) > 0:
                    print(True)
                else:
                    print(False)


        elif int(line[3]) <= 2500:
            if line[4] == 'TRUE':
                if int(line[5]) == 0:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.3 or int(line[7]) > 1:
                    print(True)
                else:
                    print(False)

            else:
                if int(line[5]) == 0:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.3 or int(line[7]) > 1:
                    print(True)
                else:
                    print(False)

        else:
            if line[4] == 'TRUE':
                if int(line[5]) == 0:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.3 or int(line[7]) > 1:
                    print(True)
                else:
                    print(False)

            else:
                if int(line[5]) == 0:
                    print(True)
                elif int(line[6]) / int(line[5]) > 0.3 or int(line[7]) > 1:
                    print(True)
                else:
                    print(False)



fp.close()