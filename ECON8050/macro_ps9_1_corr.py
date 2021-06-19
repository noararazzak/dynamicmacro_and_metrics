from matplotlib import pyplot as plt


# Created Capital Stock and GDP Growth following the Solow Growth Model
# We consider capital stock and GDP for aggregate, per worker and per effective worker

def worker(m, l):
    output = (1 + m) * l
    return output


def technology(g, a):
    output = (1 + g) * a
    return output


def capital_agg(s, y, k, delta):
    output = s * y + (1 - delta) * k
    return output


def gdp(k, alpha, a, l):
    output = (k ** alpha) * ((a * l) ** (1 - alpha))
    return output


def gdp_perworker(k, alpha, a):
    output = (k ** alpha) * (a ** (1 - alpha))
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


def calculations_agg(s, a, l, k, alpha, delta, m, g):
    number = range(100)
    k1_list = []
    gdp_list = []
    k_star = a * (s / (m + g + delta)) ** (1 / (1 - alpha))
    y_star = a * (s / (m + g + delta)) ** (alpha / (1 - alpha))
    for n in number:
        l1 = worker(m, l)
        a1 = technology(g, a)
        y = gdp(k, alpha, a, l)
        k1 = capital_agg(s, y, k, delta)
        k1_list.append(k1)
        gdp_list.append(y)
        k = k1
        l = l1
        a = a1
    k_list = [10] + k1_list
    del k_list[-1]
    # k_list = [x * l for x in k_list]
    xlist = list(range(len(k_list)))
    plotcapitalgdp(k_list, gdp_list)
    plotcapitaltime(xlist, k_list)
    plotgdptime(xlist, gdp_list)
    return k_star, y_star, k_list[-1], k_list[0], l, a


def calculations_pw(s, a, k, l, alpha, delta, m, g):
    number = range(219)
    k1_list = []
    gdp_list = []
    k_pw_list = []
    y_pw_list = []
    k_star = a * (s / (delta + m + g)) ** (1 / (1 - alpha))
    y_star = a * (s / (delta + m + g)) ** (alpha / (1 - alpha))
    for n in number:
        l1 = worker(m, l)
        a1 = technology(g, a)
        y = gdp(k, alpha, a, l)
        k1 = capital_agg(s, y, k, delta)
        k1_list.append(k1)
        gdp_list.append(y)
        y_pw = y / l1
        k_pw = (k1 / l1)
        y_pw_list.append(y_pw)
        k_pw_list.append(k_pw)
        k = k1
        l = l1
        a = a1
    k_list = [2] + k_pw_list
    del k_list[-1]
    xlist = list(range(len(k_list)))
    plotcapitalgdp(k_list, y_pw_list)
    plotcapitaltime(xlist, k_list)
    plotgdptime(xlist, y_pw_list)
    return k_star, y_star, k_list[-1], k_list[0], l, a


def calculations_pew(s, a, k, l, alpha, delta, m, g):
    k_star = a * (s / (delta + m + g)) ** (1 / (1 - alpha))
    y_star = a * (s / (delta + m + g)) ** (alpha / (1 - alpha))
    number = range(219)
    k1_list = []
    gdp_list = []
    k_pew_list = []
    y_pew_list = []
    for n in number:
        l1 = worker(m, l)
        a1 = technology(g, a)
        y = gdp(k, alpha, a, l)
        k1 = capital_agg(s, y, k, delta)
        k1_list.append(k1)
        gdp_list.append(y)
        y_pew = y / (l1*a1)
        k_pew = (k1 / (l1*a1))
        y_pew_list.append(y_pew)
        k_pew_list.append(k_pew)
        k = k1
        l = l1
        a = a1
    k_list = [2] + k_pew_list
    del k_list[-1]
    xlist = list(range(len(k_list)))
    plotcapitalgdp(k_list, y_pew_list)
    plotcapitaltime(xlist, k_list)
    plotgdptime(xlist, y_pew_list)
    return k_star, y_star, k_list[-1], k_list[0], l, a
