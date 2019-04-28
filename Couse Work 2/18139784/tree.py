from math import sin, cos
from matplotlib import pyplot as plt
from argparse import ArgumentParser


def plot_tree(node1, node2, plot):
    if plot is False:
        plt.plot(node1, node2)


def create_branch(node, d_angle, initial_branch_length, plot):
    new_angle = node[2]+d_angle
    new_x = node[0]+initial_branch_length*sin(new_angle)
    new_y = node[1]+initial_branch_length*cos(new_angle)
    plot_tree([node[0], new_x], [node[1], new_y], plot)
    return [new_x, new_y, new_angle]


def make_tree(iterations, initial_branch_length, scale_factor, d_angle,
              no_plot):

    nodes = [[0, 1, 0]]

    plot_tree([0, 0], [0, 1], no_plot)
    for i in range(iterations):
        new_nodes = []
        for node in nodes:
            new_nodes.append(create_branch(node, -d_angle,
                                           initial_branch_length, no_plot))
            new_nodes.append(create_branch(node, d_angle,
                                           initial_branch_length, no_plot))
        nodes = new_nodes
        initial_branch_length *= scale_factor

    if no_plot is False:
        plt.savefig('tree.png')


def main():

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

    make_tree(iterations, initial_branch_length, scale_factor, d_angle,
              no_plot)


if __name__ == "__main__":
    main()
