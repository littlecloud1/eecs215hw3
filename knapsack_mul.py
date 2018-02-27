
import sys
#value for testing

# val = [40, 35, 30]
# weight = [3, 2, 5]
# totalweight = 8
# n = len(val)

def knapsack_mul(W,weight,val,n,vol,Z):
    #initialization
    OPT = [[[0 for x in range(W+1)] for y in range(n+1)] for z in range(Z+1)]
    
    #compute opt table
    for i in range(1,n+1):
        for w in range(1,W+1):
            for z in range(1,Z+1):
                if weight[i-1] > w or vol[i-1] > z:
                    OPT[i][w][z] = OPT[i-1][w][z]
                else:
                    OPT[i][w][z] = max(val[i-1]+OPT[i-1][w-weight[i-1][z-vol[i-1]]], OPT[i-1][w][z]) #no

    for i in range(n+1):
        print (OPT[i])
        #calculate the item chosen
    
#    choice=[]
#    weightremaining = W
#    w = W
#    i = n
#    while weightremaining>0:
#        if val[i - 1] + OPT[i][weightremaining- weight[i - 1]] >= OPT[i - 1][weightremaining]:
#            if weight[i-1] <= weightremaining:
#                choice.append(i)
#                weightremaining -= weight[i - 1]
#            else:
#                i -= 1
#                if i==0:
#                    i = n
#        else:
#            i -= 1
#            if i == 0:
#                i = n
#    print "choose: ",choice
#    print "optimal value", OPT[n][W]
    return OPT[n][W][Z]#, choice



# print(knapsack_rep(totalweight,weight,val,n))

#def output(outfile,optimal,choice):
#    # file output
#    f = open(outfile, 'w')
#    f.write(str(optimal) + "\n")
#    f.write(str(choice) + "\n")
#    f.close()

def main(argv):
    weight = []
    val = []
    vol = []
    l = 0;#line
    fn = argv[1]
    with open(fn) as fp:
        
        for line in fp:
            if l == 0:
                nodes = line.strip().split(" ")
                totalweight = int(nodes[0])
                totalvolume = int(nodes[1])
                print "totalweight: %s total  volume %s" % (totalweight,totalvolume)
            if l > 0:
                # Split lines by chosen character.
                nodes = line.strip().split(" ")
                # Format string example:
                weight.append(int(nodes[1]))
                val.append(int(nodes[2]))
                vol.append(int(nodes[3]))
                print "weight: %s\t value: %s\t volume: %s" % (nodes[1], nodes[2],nodes[3])
            # Add edge to graph with integer IDs.
            l += 1
    n = len(val)
    #optimal,choice = knapsack_mul(totalweight, weight, val, n, vol, totalvolume)
    #output(argv[2],optimal,choice)



if __name__ == "__main__":
    main(sys.argv)

