
import sys

val = [40, 35, 30]
weight = [3, 2, 5]
totalweight = 8
n = len(val)

def knapsack_rep(W,weight,val,n):
    #initialization
    OPT = [[0 for x in range(W+1)] for y in range(n+1)]
    
    #compute opt table
    for w in range(1,W+1):
        for i in range(1,n+1):
            if weight[i-1] > w:
                OPT[i][w] = OPT[i-1][w]
            else:
                OPT[i][w] = max(val[i-1]+OPT[i][w-weight[i-1]], OPT[i-1][w]) #no repetition if OPT[i][w] = max(val[i-1]+OPT[i-1][w-weight[i-1]], OPT[i-1][w])

for i in range(n+1):
    print (OPT[i])
    #calculate the item chosen
    
    choice=[]
    weightremaining = totalweight
    w = totalweight
    i = n
    while weightremaining>0:
        if val[i - 1] + OPT[i][w - weight[i - 1]]>=OPT[i - 1][w]:
            choice.append(i)
            weightremaining -= weight[i - 1]
        else:
            i-=1
    print(choice)
    return OPT[n][W]



print(knapsack_rep(totalweight,weight,val,n))


# def main(fn, s):
#     weight = []
#     val = []
#     l = 0;#line
#     with open(fn) as fp:
#
#         for line in fp:
#             if l == 0:
#                 totalweight = fp.readline
#                 print totalweight
#             if l > 1:
#                 # Split lines by chosen character.
#                 nodes = line.strip().split(" ")
#                 # Format string example:
#                 weight.append(nodes[1])
#                 val.append(nodes[2])
#                 print "weight: %s\t value: %s" % (nodes[1], nodes[2])
#                 # Add edge to graph with integer IDs.
#             l += 1
#     val = [40, 35, 30]
#     weight = [3, 2, 5]
#     totalweight = 8
#     n = len(val)
#     print(knapsack_rep(totalweight, weight, val, n))
#
#
#
# if __name__ == "__main__":
#     print "Program starts"
#     print sys.argv
#     if len(sys.argv) == 3:
#         fn = sys.argv[1] # Filename
#         print "filename: "+fn
#         s  = sys.argv[2] # Source
#         main(fn,int(s))
