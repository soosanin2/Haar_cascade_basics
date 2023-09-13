import numpy as np

def act(x):
    return 0 if x < 0.5 else 1

def start(taste, color, shape):
    x = np.array([taste, color, shape])
    w11 = [0.1, 0.2, 0.1]
    w12 = [0.1, 0.3, 1]
    weight1 = np.array([w11, w12])
    weight2 = np.array([-1, 1])
    print(weight1)
    print(weight2)
    print(x)

    sum_hidden = np.dot(weight1, x)
    '''
    weight1= [[0.1 0.2 0.1] [0.1 0.3 1. ]]
    x = [1 1 1]
    Розрахунок суми для прихованого шару:
    sum_hidden = np.dot(weight1, x)
    Для першого нейрона у прихованому шарі:
    sum_hidden[0] = (0.1 * 1) + (0.2 * 1) + (0.1 * 1) = 0.4
    Для другого нейрона у прихованому шарі:
    sum_hidden[1] = (0.1 * 1) + (0.3 * 1) + (1 * 1) = 1.4
    Отже, sum_hidden містить суми для кожного з нейронів у першому прихованому шарі:
    sum_hidden = [0.4 1.4]
    '''
    print("Значенyя сум на нейронах прихованного шару: " + str(sum_hidden))

    out_hidden = np.array([act(x) for x in sum_hidden])
    print("Значения на виходах нейронів прихованного шару: " + str(out_hidden))

    sum_end = np.dot(weight2, out_hidden)
    print(sum_end)
    y = act(sum_end)
    print("Вихідні значення НС: " + str(y))

    return y

sweet, sour = 1, 0
red, yellow = 1, 0
round, long = 1, 0

# умови що повинні виконуватись

# 1 # 1 банан
# shape = long
# taste = sweet
# color = yellow

# 2 # 2 банан
# shape = long
# taste = sour
# color = yellow

# 3 # 3 банан
# shape = long
# taste = sour
# color = red

# 4 # 1 яблуко
# shape = round
# taste = sour
# color = red

# 5 # 2 яблуко
# shape = round
# taste = sour
# color = yellow

# 6 # 3 яблуко
# shape = round
# taste = sweet
# color = yellow

# 7 # 4 яблуко
shape = round
taste = sweet
color = red

res = start(taste, color, shape)
if res == 1:
    print("яблуко")
else:
    print("банан")

