#Exercise : Odd Tuples
#Write a python function oddTuples(aTup):  
def odd_tuples(a_tup):
    '''
    a_tup: a tuple
    returns: tuple, every other element of aTup. 
    '''
    p_p = ()
    l_p = len(a_tup)
    i_p = 0
    while i_p <= l_p-1:
        i_p = i_p + 1
        p_p = p_p + (a_tup[i_p],)
        i_p = i_p + 1
    return p_p
def main():
    """
    Main Fuction
    """
    data = input()
    data = data.split()
    a_tup=()
    for j in range(len(data)):
        a_tup += (int(data[j]),)
    print(odd_tuples(a_tup))
if __name__ == "__main__":
    main()
