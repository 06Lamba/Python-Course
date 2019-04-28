# change * to np
import numpy as np
import matplotlib.pyplot as plt
from argparse import ArgumentParser

def zxy (scale_factor,current_value,max_value,denom):
    return scale_factor*(current_value-max_value/2)/(denom*1*max_value)

def build_julia(iter,size_x,size_y,scale_factor_x,scale_factor_y,denom_x,denom_y,inter_x,inter_y,factor_zy):
    A = np.zeros([size_y,size_x])
    for x in range(size_x):
        for y in range(size_y):
            zx = zxy(scale_factor_x,x,size_x,denom_x)
            zy = zxy(scale_factor_y,y,size_y,denom_y)
            i = iter
            t=True
            while t==True:
                if zx*zx+zy*zy>=4:
                    t=False
                if i<=1:
                    t=False
                a=zx*zx-zy*zy+inter_x
                zy=factor_zy*zx*zy+inter_y
                zx=a
                i=i-1
            A[y][x]=i
    plt.imshow(A)
    plt.show()
    plt.savefig('test.png')

def process():
    
    parser = ArgumentParser(description="Implement a Julia set")
    parser.add_argument('--iterate', nargs='?', const=255, type=int, default=255,
                        help='Number of iterations for each position '
                        '(default: %(default)s)')
    parser.add_argument("--xlength", nargs='?', const=800, type=int, default=800,
                        help='Size of x (default: %(default)s)')
    parser.add_argument("--ylength", nargs='?', const=600, type=int, default=600,
                        help='Size of x (default: %(default)s)')
    parser.add_argument("--xscale", nargs='?', const=1.5, type=float, default=1.5,
                        help='Scale factor for x lengths (default: %(default)s)')
    parser.add_argument("--yscale", nargs='?', const=1.0, type=float, default=1.0,
                        help='Scale factor for y lengths (default: %(default)s)')
    arguments = parser.parse_args()

    iter = arguments.iterate
    size_x = arguments.xlength
    size_y = arguments.ylength
    scale_factor_x = arguments.xscale
    scale_factor_y = arguments.yscale


    denom_x = 0.5
    denom_y = 0.5
    inter_x = - 0.7
    inter_y = 0.27015
    factor_zy = 2.0

    build_julia(iter,size_x,size_y,scale_factor_x,scale_factor_y,denom_x,denom_y,inter_x,inter_y,factor_zy)

if __name__ == "__main__":
    process()