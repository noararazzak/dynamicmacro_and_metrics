from matplotlib import pyplot as plt


def worker(m, l):
    output = (1 + m) * l
    return output


def technology(g, a):
    output = (1 + g) * a
    return output


def capital_agg(s, a, k, alpha, delta):
    output = s * (k ** alpha) * (a ** (1 - alpha)) + (1 - delta) * k
    return output


def capital_pw(s, a, k, alpha, delta, m):
    output = (s * (k ** alpha) * (a ** (1 - alpha)) + (1 - delta) * k) * (1 / (1 + m))
    return output


def capital_pew(s, a, k, alpha, delta, m, g):
    output = (s * (k ** alpha) * (a ** (1 - alpha)) + (1 - delta) * k) * (1 / ((1 + m) * (1 + g)))
    return output


def gdp(k, alpha, a, l):
    output = (k ** alpha) * (a ** (1 - alpha)) * (l ** (1 - alpha))
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


def calculations_agg(s, a, l, k, alpha, delta):
    number = range(1000)
    k1_list = []
    gdp_list = []
    for n in number:
        k1 = capital_agg(s, a, k, alpha, delta)
        y = gdp(k, alpha, a, l)
        k1_list.append(k1)
        gdp_list.append(y)
        k = k1
    k_list = [10] + k1_list
    del k_list[-1]
    k_star = (s / delta) ** (1 / (1 - alpha))
    y_star = (s / delta) ** (alpha / (1 - alpha))
    xlist = list(range(1000))
    plotcapitalgdp(k_list, gdp_list)
    plotcapitaltime(xlist, k_list)
    plotgdptime(xlist, gdp_list)
    return k_star, y_star, k_list[-1], k1_list[-1], k_list[0], k1_list[0], k_list[1], k1_list[1], k_list[2], k1_list[2]


def calculations_pw(s, a, k, l, alpha, delta, m):
    number = range(1000)
    k1_list = []
    gdp_list = []
    for n in number:
        k1 = capital_pw(s, a, k, alpha, delta, m)
        y = gdp(k, alpha, a, l)
        if (k1 - k) > 0.1:
            l1 = worker(m, l)
        else:
            l1 = worker(0, l)
        k1_list.append(k1)
        gdp_list.append(y)
        k = k1
        l = l1
    k_list = [10] + k1_list
    del k_list[-1]
    k_star = (s / (delta + m)) ** (1 / (1 - alpha))
    y_star = (s / (delta + m)) ** (alpha / (1 - alpha))
    xlist = list(range(1000))
    plotcapitalgdp(k_list, gdp_list)
    plotcapitaltime(xlist, k_list)
    plotgdptime(xlist, gdp_list)
    return k_star, y_star, k_list[-1], k1_list[-1], k_list[0], k1_list[0], k_list[1], k1_list[1], k_list[2], k1_list[2]


def calculations_pew(s, a, k, l, alpha, delta, m, g):
    number = range(1000)
    k1_list = []
    gdp_list = []
    for n in number:
        k1 = capital_pew(s, a, k, alpha, delta, m, g)
        y = gdp(k, alpha, a, l)
        if (k1 - k) > 0.1:
            l1 = worker(m, l)
            a1 = technology(g, a)
        else:
            l1 = worker(0, l)
            a1 = technology(0, a)
        k1_list.append(k1)
        gdp_list.append(y)
        k = k1
        l = l1
        a = a1
    k_list = [10] + k1_list
    del k_list[-1]
    xlist = list(range(1000))
    plotcapitalgdp(k_list, gdp_list)
    plotcapitaltime(xlist, k_list)
    plotgdptime(xlist, gdp_list)
    k_star = (s / (delta + m + g)) ** (1 / (1 - alpha))
    y_star = (s / (delta + m + g)) ** (alpha / (1 - alpha))
    return k_star, y_star, k_list[-1], k1_list[-1], k_list[0], k1_list[0], k_list[1], k1_list[1], k_list[2], k1_list[2]
