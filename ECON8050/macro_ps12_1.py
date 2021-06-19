from matplotlib import pyplot as plt

# Created Capital Stock and GDP Growth following the Solow Growth Model
# We consider capital stock and GDP for aggregate, per worker and per effective worker


def capitalstock(a, l, k, c, alpha, delta):
    output = ((k ** alpha)*l * a) + ((1 - delta) * k) - c
    return output


def consumption(k, c, alpha, delta, beta, one):
    medium = alpha*(k**(alpha-1)) + one - delta
    output = beta*c*medium
    return output


def plotcapitalconsumption(a, b):
    plt.plot(a, b, 'r')
    plt.xlabel('k_t')
    plt.ylabel('c_t')
    plt.title('c_t vs k_t')
    plt.show()


def calculations(a, l, k, c, alpha, delta, beta, one):
    number = range(1000)
    k1_list = []
    con_list = []
    k_not = k
    c_not = c
    k_star = (alpha/((1/beta) - one + delta))**(1/(1-alpha))
    c_star = (k_star ** alpha) - (delta*k_star)
    for n in number:
        k1 = capitalstock(a, l, k, c, alpha, delta)
        c1 = consumption(k1, c, alpha, delta, beta, one)
        k1_list.append(k1)
        con_list.append(c1)
        if k1 == 0.0:
            print(n)
            break
        k = k1
        c = c1
    k_list = [k_not] + k1_list
    con_list = [c_not] + con_list
    xlist = list(range(len(k_list)))
    plotcapitalconsumption(k_list, con_list)
    return k_star, c_star, con_list[0], con_list[-1], k_list[-1], k_list[-2]
