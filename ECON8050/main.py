# import macro_ps9_1
#import macro_ps9_1_corr
#import macro_ps10_1
import macro_ps12_1


def main():
    # answer = macro_ps9_1.calculations_pew(.25, 1, 5, 10, .8, 0.05, 0.02, 0.01)
    # print(answer)
    # answer = macro_ps8_2.maxutility2(1, 1, 3, 0.25, 0.98, 2, 1.6)
    # print(answer)
    answer = macro_ps12_1.calculations(1.0, 1.0, 0.691, 0.6, 0.33, 0.07, 0.98, 1.0)
    print(answer)
    #answer = macro_ps9_1_corr.calculations_pw(.25, 1, 10, 5, .333, 0.05, 0.02, 0.01)
    #print(answer)


if __name__ == "__main__":
    main()
