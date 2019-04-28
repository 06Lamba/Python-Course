from argparse import ArgumentParser
from .laboratory import Laboratory
import yaml


def process():
    parser = ArgumentParser(description="Generate final state of the shelves")

    parser.add_argument('--reactions', '-r', action="store_false")
    parser.add_argument("x", type=str, help="Location of yml file")
    arguments = parser.parse_args()

    lab = Laboratory()

    dic = yaml.load(open(arguments.x))
    shelf1, shelf2, count = lab.run_full_experiment(dic)

    if arguments.reactions:
        print('lower: [%s]' % ', '.join(map(str, shelf1)))
        print('upper: [%s]' % ', '.join(map(str, shelf2)))

    else:
        print(count)


if __name__ == "__main__":
    process()
