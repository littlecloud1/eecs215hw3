def knapsack_rep(W,weight,val,n):
    #initialization
    OPT = [[0 for x in range(W+1)] for y in range(n+1)]

    #compute opt table
    for w in range(W+1):
        for i in range(n+1):
            if i==0 or w==0:
                OPT[i][w] = 0;
            elif weight[i] > W:
                OPT[i][w] = OPT[i-1][w]
            else:
                OPT[i][w] = max(val[i]+OPT[i-1][w-weight[i]], OPT[i-1][w])

    return OPT[n][W]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))
