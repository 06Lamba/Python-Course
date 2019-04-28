import numpy as np
from timeit import repeat
from matplotlib import pyplot as plt
from tree import make_tree
from tree_np import make_tree_np

iterations = np.arange(1, 15, 1)
length = 1
scale = 0.6
angle = 0.1


def plot_time(iterations):
    tree_list, = plt.plot(iterations,
                          list(map(time_to_make_tree, iterations)),
                          label='lists')
    print()
    tree_np, = plt.plot(iterations,
                        list(map(time_to_make_tree_np, iterations)),
                        label='numpy arrays')
    plt.ylim(bottom=0)
    plt.ylabel('seconds')
    plt.xlabel('iterations')
    plt.title('Comparison of performance times')
    plt.legend(handles=[tree_list, tree_np])
    plt.savefig('perf_plot.png')


def time_to_make_tree(iterate):
        def totime():
            make_tree(iterate, length, scale, angle, True)
        num_tests = 10
        tests = repeat(totime, repeat=1, number=num_tests)
        average = [t / num_tests for t in tests]
        return average


def time_to_make_tree_np(iterate):
        def totime():
            make_tree_np(iterate, length, scale, angle, True)
        num_tests = 15
        tests = repeat(totime, repeat=1, number=num_tests)
        average = [t / num_tests for t in tests]
        return average


if __name__ == "__main__":
    plot_time(iterations)
