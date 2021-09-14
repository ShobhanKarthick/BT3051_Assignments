series = [0, 1]
def ph_generator(series):
    new_num = series[-1] + series[-2]
    series.append(new_num)
    return series

for i in range(10):
    series = ph_generator(series)
print(series)
