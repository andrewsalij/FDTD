import numpy as np
import itertools as it

def tuple_product(*args):
    return list(it.product(*args))

def zero_tuple_of_size(size):
    tuple = (0,)
    for i in range(size-1):
        tuple = tuple+(0,)
    return tuple

def create_film_params(*args,npol = 4,make_film = "both"):
    res = args[0]
    if np.size(res) > 1:
        res = res[0]
    pol = args[1]
    nargs=  len(args)
    narr = np.zeros(nargs)
    for i in range(0,nargs):
        narr[i] = np.size(args[i])
    if (make_film == "both"):
        nrows = int(np.prod(narr)+npol) # four blanks for the False makefilm params
    elif (make_film == "yes"):
        nrows = int(np.prod(narr))
    elif (make_film == "no"):
        nrows = int(npol)
    else:
        ValueError("Invalid make_film string")
    params = np.rec.array(None,dtype=("int,object,bool,float,float,float,float,float,float,float,float"),shape =nrows)
    j = 0 # tuple product indexing
    p = 0 # polarization list indexing
    tuple_prod= tuple_product(*args)
    tup_size = len(tuple_prod[0])
    for i in range(nrows):
        if (make_film == "both"):
            if (i%(nrows/npol) ==0):
                params[i] = (res[0],pol[p],False,args[2][0],args[3][0])+zero_tuple_of_size(tup_size-6)+(args[-2][0],args[-1][0])
                p = p+1
            else:
                cur_tuple = tuple_prod[j]
                new_tuple = cur_tuple[0:2]+(True,)+cur_tuple[2:tup_size]
                params[i] = new_tuple
                j = j+1
        elif (make_film == "yes"):
            cur_tuple = tuple_prod[j]
            new_tuple = cur_tuple[0:2] + (True,) + cur_tuple[2:tup_size]
            params[i] = new_tuple
            j = j + 1
        elif (make_film == "no"):
            params[i] = (res[0], pol[p], False, args[2][0], args[3][0]) + zero_tuple_of_size(tup_size - 6) + (
            args[-2][0], args[-1][0])
            p = p + 1
    return params
import csv
def create_params_file(fname,res,pols,sx,sy,dx,dy1,dy2,theta,freq_center,freq_width,make_film = "both"):
    # six_tuple= zero_tuple_of_size(6)
    # product = tuple_product(res,pols,sx,sy,dx,dy1,dy2)
    params = create_film_params(res,pols,sx,sy,dx,dy1,dy2,theta,freq_center,freq_width,make_film = make_film)
    with open(fname, "w") as the_file:
        writer = csv.writer(the_file, delimiter=" ",skipinitialspace=True)
        for tup in params:
            writer.writerow(tup)
