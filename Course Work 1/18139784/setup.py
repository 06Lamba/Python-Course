from setuptools import setup, find_packages

setup(name="The Alchemist's Laboratory",
      version="0.1dev",
      author="Student Number 18139784",
      packages=find_packages(exclude=['*tests']),
      install_requires=['argparse', 'pyyaml', 'pytest'],
      entry_points={'console_scripts':
                    ['abracadabra = alchemist.command:process'], }
      )
