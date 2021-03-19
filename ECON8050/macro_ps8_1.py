from matplotlib import pyplot as plt


# Created utility finction, production possibility frontier and
# indifference curve for Saving & Consumption Model with Investment Model
# for a cloed economy.

def consumption(a1, k1, alpha):
    y1 = a1 * (k1 ** alpha)
    c1 = y1 + k1
    return c1, y1


def utilityfunc(c1, y1, sigma, alpha, beta, a2, k1):
    k2 = k1 + y1 - c1
    c2 = a2*(k2**alpha) + k1 + y1 - c1
    sigmainv = 1 / sigma
    power = 1 - sigmainv
    utility = 1 / power * ((c1 ** power) + beta * (c2 ** power))
    return c2, utility


def indifference(clist, maxutil, sigma, beta):
    power = 1 - (1 / sigma)
    c2optlist = []
    for i in clist:
        c2opt = ((power / beta) * (maxutil - (i ** power / power))) ** (1 / power)
        c2optlist.append(c2opt)
    return c2optlist


def maxutility(a1, k1, sigma, alpha, beta, a2):
    utilitylist = []
    c1list = []
    c2list = []
    c1, y1 = consumption(a1, k1, alpha)
    number = range(198)

    for n in number:
        c1 = c1 - 0.01
        c2, utility = utilityfunc(c1, y1, sigma, alpha, beta, a2, k1)
        utilitylist.append([c1, utility])
        c1list.append(c1)
        c2list.append(c2)

    maxutil = max(utilitylist, key=lambda x: x[1])
    c1 = maxutil[0]
    umax = maxutil[1]
    c2optlist = indifference(c1list, umax, sigma, beta)
    k2 = k1 + y1 - c1
    y2 = a2*(k2**alpha)
    c2 = y2 + k2
    print(k2, y2, c2)
    plt.plot(c1list, c2list)
    plt.plot(c1list, c2optlist, 'r')
    plt.xlabel('C1')
    plt.ylabel('C2')
    plt.title('C1 vs C2')
    plt.show()
    return maxutil


def main():
    answer = maxutility(1, 1, 3, 0.25, 0.98, 2)
    print(answer)


if __name__ == "__main__":
    main()
