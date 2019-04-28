from matplotlib import pyplot as plt
from argparse import ArgumentParser
import numpy as np


def plot_tree(node1, node2, plot):
    if plot is False:
        plt.plot(node1, node2)


def make_tree_np(iterations, initial_branch_length, scale_factor, d_angle,
                 no_plot):

    node_x = np.array([0])
    node_y = np.array([1])
    node_angle = np.array([0])

    plot_tree([0, 0], [0, 1], no_plot)

    for i in range(iterations):
        new_angle_ac = node_angle-d_angle
        new_x_ac = node_x+initial_branch_length*np.sin(new_angle_ac)
        new_y_ac = node_y+initial_branch_length*np.cos(new_angle_ac)

        plot_tree([node_x, new_x_ac], [node_y, new_y_ac], no_plot)

        new_angle_c = node_angle+d_angle
        new_x_c = node_x+initial_branch_length*np.sin(new_angle_c)
        new_y_c = node_y+initial_branch_length*np.cos(new_angle_c)

        plot_tree([node_x, new_x_c], [node_y, new_y_c], no_plot)

        node_angle = np.hstack((new_angle_ac, new_angle_c))
        node_x = np.hstack((new_x_ac, new_x_c))
        node_y = np.hstack((new_y_ac, new_y_c))

        initial_branch_length *= scale_factor

    if no_plot is False:
        plt.savefig('tree_np.png')


def main_np():

    parser = ArgumentParser(description="Generate appropriate tree")
    parser.add_argument('--iterate', nargs='?', const=5, type=int, default=5,
                        help='Number of layers of branchs above first level '
                        '(default: %(default)s)')
    parser.add_argument("--length", nargs='?', const=1, type=float, default=1,
                        help='Initial branch length (default: %(default)s)')
    parser.add_argument("--scale", nargs='?', const=0.6, type=float,
                        default=0.6, help='Scale factor for sequential branch '
                        'lengths (default: %(default)s)')
    parser.add_argument("--angle", nargs='?', const=0.1, type=float,
                        default=0.1, help='Change in angle at each node '
                        '(default: %(default)s)')
    parser.add_argument('--noplot', action="store_true",
                        help="Suppess creation of tree.png")
    arguments = parser.parse_args()

    iterations = arguments.iterate
    initial_branch_length = arguments.length
    scale_factor = arguments.scale
    d_angle = arguments.angle
    no_plot = arguments.noplot

    make_tree_np(iterations, initial_branch_length, scale_factor, d_angle,
                 no_plot)


if __name__ == "__main__":
    main_np()
