import math

import matplotlib.pyplot as plt


def fn_8n(x):
    return 8 * x


def fn_4n_log_n(x):
    if x == 0:
        return 0
    return 4 * x * math.log(x)


def fn_2n_raised_2(x):
    return 2 * x * x


def fn_n_raised_3(x):
    return x * x * x


def fn_2_raised_n(x):
    return math.pow(2, x)


def get_logarithm(n):
    if n == 0:
        return 0
    return math.log(n)


if __name__ == '__main__':
    plot_to = 10

    coordinates_y = [] * plot_to
    coordinates_x_8n = [] * plot_to
    coordinates_4n_log_n = [] * plot_to
    coordinates_2n_raised_2 = [] * plot_to
    coordinates_fn_n_raised_3 = [] * plot_to
    coordinates_2_raised_n = [] * plot_to

    for i in range(plot_to):
        coordinates_y.append(get_logarithm(i))
        coordinates_x_8n.append(get_logarithm(fn_8n(i)))
        coordinates_4n_log_n.append(get_logarithm(fn_4n_log_n(i)))
        coordinates_2n_raised_2.append(get_logarithm(fn_2n_raised_2(i)))
        coordinates_fn_n_raised_3.append(get_logarithm(fn_n_raised_3(i)))
        coordinates_2_raised_n.append(get_logarithm(fn_2_raised_n(i)))

    plt.plot(coordinates_x_8n, coordinates_y)
    plt.plot(coordinates_4n_log_n, coordinates_y)
    plt.plot(coordinates_2n_raised_2, coordinates_y)
    plt.plot(coordinates_fn_n_raised_3, coordinates_y)
    plt.plot(coordinates_2_raised_n, coordinates_y)
    plt.show()