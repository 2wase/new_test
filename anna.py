float = []
t = input("enter no. of towers:" )
n = int(t)+1
for i in range(0, int(t)+1):
    n-=1

    print(" "*n + "*"*((i*2)-1) + " "*n )
