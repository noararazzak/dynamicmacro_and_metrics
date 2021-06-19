from matplotlib import pyplot as plt


# Created Capital Stock and GDP Growth following the Solow Growth Model
# We consider capital stock and GDP for aggregate, per worker and per effective worker


def capital_agg(s, a, k, alpha, delta):
    output = s * (k ** alpha) * a + (1 - delta) * k
    return output


def gdp_per(k, alpha, a):
    output = (k ** alpha) * a
    return output


def plotcapitalgdp(a, b):
    plt.plot(a, b, 'r')
    plt.xlabel('k_t')
    plt.ylabel('y_t')
    plt.title('y_t vs k_t')
    plt.show()


def plotcapitaltime(a, b):
    plt.plot(a, b, 'r')
    plt.xlabel('time')
    plt.ylabel('k_t')
    plt.title('k_t vs time')
    plt.show()


def plotgdptime(a, b):
    plt.plot(a, b, 'r')
    plt.xlabel('time')
    plt.ylabel('y_t')
    plt.title('y_t vs time')
    plt.show()


def calculations_agg(s, a, k, l, alpha, delta):
    number = range(1000)
    k1_list = []
    gdp_list = []
    k_not = k
    k_star = ((a*s) / delta) ** (1 / (1 - alpha))
    y_star = a * (k_star ** alpha)
    for n in number:
        k1 = capital_agg(s, a, k, alpha, delta)
        y = gdp_per(k, alpha, a)
        k1_list.append(k1)
        gdp_list.append(y)
        if (k_star - k1) < 0.1:
            print(n)
            break
        k = k1
    k_list = [k_not] + k1_list
    del k_list[-1]
    k_list = [x * l for x in k_list]
    xlist = list(range(len(k_list)))
    plotcapitalgdp(k_list, gdp_list)
    plotcapitaltime(xlist, k_list)
    plotgdptime(xlist, gdp_list)
    return k_star, y_star, k_list[-1], k1_list[-1], k_list[0]



