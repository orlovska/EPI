# A permutation is a rearrangement of members of a sequence into a new sequence. 
# Input is list of elements whith need to be rearrenged to possitions according to list with new indexes - perm.



def permute_elements(elem, perm) -> str:
    if elem == [] or perm == [] or type(elem) is not list or type(perm) is not list:
        raise TypeError (f"The input {elem}, {perm} sold be List & not empty - [1,2,0]")

    for i in range(len(elem)):
        if i != perm[i]:
            elem[i], elem[perm[i]] = elem[perm[i]], elem[i]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
    
    return elem 