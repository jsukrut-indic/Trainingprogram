# Tower of Hanoi program for Training Program 

def towerOfHanoi(n,fromrod,torod,auxrod):
    if n == 1:
        print("\n Move disk 1 from rod %c to rod %c" % (fromrod, torod));
        return;
    towerOfHanoi(n-1, fromrod, auxrod, torod);
    print("\n Move disk %d from rod %c to rod %c" % (n, fromrod, torod));
    towerOfHanoi(n-1, auxrod, torod, fromrod);


n = 4
towerOfHanoi(n,'A','C','B')
