from matplotlib import pyplot as plt


def consumption2(a1, k1, alpha):
    y1 = a1 * (k1 ** alpha)
    c1 = y1 + k1
    return c1, y1


def utilityfunc2(c1, y1, sigma, alpha, beta, a2, k1, r):
    alphap = 1 / (alpha - 1)
    k2 = (r / (alpha * a2)) ** alphap
    i1 = k2 - k1
    c2 = (1 + r) * (y1 - c1 - i1) + a2 * (k2 ** alpha) + k2
    sigmainv = 1 / sigma
    power = 1 - sigmainv
    utility = 1 / power * ((c1 ** power) + beta * (c2 ** power))
    return k2, c2, utility


def indifference2(clist, maxutil, sigma, beta):
    power = 1 - (1 / sigma)
    c2optlist = []
    for i in clist:
        c2opt = ((power / beta) * (maxutil - (i ** power / power))) ** (1 / power)
        c2optlist.append(c2opt)
    return c2optlist


def maxutility2(a1, k1, sigma, alpha, beta, a2, r):
    utilitylist = []
    c1list = []
    c2list = []
    c1, y1 = consumption2(a1, k1, alpha)
    number = range(198)

    for n in number:
        c1 = c1 - 0.01
        k2, c2, utility = utilityfunc2(c1, y1, sigma, alpha, beta, a2, k1, r)
        utilitylist.append([c1, utility, k2])
        c1list.append(c1)
        c2list.append(c2)

    maxutil = max(utilitylist, key=lambda x: x[1])
    c1 = maxutil[0]
    umax = maxutil[1]
    k2 = maxutil[2]
    i1 = k2 - k1
    y2 = a2 * (k2 ** alpha)
    b2 = y1 - c1 - i1
    c2 = (1 + r) * (y1 - c1 - i1) + y2 + k2
    print(k2, y2, c2, b2)
    c2optlist = indifference2(c1list, umax, sigma, beta)
    plt.plot(c1list, c2list)
    plt.plot(c1list, c2optlist, 'r')
    plt.xlabel('C1')
    plt.ylabel('C2')
    plt.title('C1 vs C2')
    plt.show()
    return maxutil


def main():
    answer = maxutility2(1, 1, 3, 0.25, 0.98, 2, 1.6)
    print(answer)


if __name__ == "__main__":
    main()
