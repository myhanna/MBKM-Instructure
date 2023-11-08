import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

def nearestneighbor(file_name):

    file = open(file_name)
    data = file.readlines()

    n = int(data[0])
    species = data[1].strip() 
    atomlist = []
    coordlist = []

    if n != (len(data)-2):
        raise ValueError('n and number of atoms input mismatch')
        
    for i in range(n):
        row = data[i+2].split()
        atomlist.append([row[0], i+1])
        coordrow = list(map(float, row[1:4]))
        coordlist.append(np.array(coordrow))

    coordlist = np.array(coordlist)

    def interatomic_distance(atom1coord, atom2coord):
        #atomcoord = array berisi xyz
        deltax = atom1coord[0] - atom2coord[0]
        deltay = atom1coord[1] - atom2coord[1]
        deltaz = atom1coord[2] - atom2coord[2]

        r = np.sqrt(deltax ** 2 + deltay ** 2 + deltaz ** 2)
        return r

    def rel_err(a, b):
        return abs(a - b) / b

    min_distance_tol = 0.01
    min_distance_list = []

    for i in range(n):
        atomcoord_i = coordlist[i]
        id_i = atomlist[i]
        min_distance = 0

        for j in range(n):
            if i == j :
                continue
            atomcoord_j = coordlist[j]
            distance_ij = interatomic_distance(atomcoord_i, atomcoord_j)
            if min_distance == 0:
                min_distance = distance_ij
                nearest_neighbor = [j+1]
            else:
                if rel_err(distance_ij, min_distance) < min_distance_tol:
                    nearest_neighbor.append(j+1)
                else:
                    if distance_ij < min_distance:
                        min_distance = distance_ij
                        nearest_neighbor = [j+1]

        min_distance_list.append([id_i, nearest_neighbor])

    # if print_nearestneighbor:
    #     print(min_distance_list)
    return n, species, min_distance_list

def LCAO_Ham(out_of_nearestneighbor, eps0, t, s = 0):
    n, species, min_distance_list = out_of_nearestneighbor

    Ham = np.empty(shape = (n, n))
    S = np.empty(shape = (n, n))

    for i in range(n):
        p = min_distance_list[i][0][1] - 1 #jaga2 buat ada yg ngacak2in id number atomnya (id_i)
        Ham[p][p] = eps0
        S[p][p] = 1
        
        for j in range(n):
            if i == j:
                continue
            if j+1 in min_distance_list[i][1]:
                Ham[p][j] = t
                S[p][j] = s
            else:
                Ham[p][j] = 0
                S[p][j] = 0
    
    return Ham, S
    



