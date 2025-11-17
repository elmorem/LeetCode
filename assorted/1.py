'''
write a function names solution(X,Y) that takes as arguments
 distributions of two random variables x and y and returns 
 the possible values of random variales z=x^2 -y, 
 sorted by their probability from the least likely to 
 the most likely.  If seeral possible values
 have equal probability, put the smaller values first.
 a dn y are arrays fo integers in which odd positions represent 
 the variables between -1000 and 1000 and the corresponsing even positions 
 are the respective probabilities scaled between 0 and 100.
 x = [-1.50,1,50]
 y = -1,40,1,60]
 the variable z can have 2 values:
 z= 2 with probability. =.4
 z = 0 with a probability =.6

 note:
 The arrays contain values where the odd positions represent the variable values
 and the even positions represent the corresponding probabilities (scaled between 0 and 100).
 it is these probabilities that should be used to compute the probabilities of z.
Approach:
1. we parse the input arrays to get the val/prob pairs
2. because x and y are independent variables, we need to compute the joint probability of each pair or (x,y)

'''
def solution(X, Y):
    def parse(arr):
        parsed = []
        for i in range(0, len(arr), 2):
            val = arr[i]
            prob = arr[i+1]
            parsed.append((val, prob))
        return parsed
    
    x_pairs = parse(X)
    y_pairs = parse(Y)

    weights = {}
    for x_val, x_prob in x_pairs:
        x_sq = x_val * x_val
        for y_val, y_prob in y_pairs:
            z = x_sq - y_val
            w = x_prob * y_prob
            weights[z] = weights.get(z, 0) + w
            #this is the tricky part right here because different xy values 
            #can produce the same z value so we have to accumulate the probabilities
    print(weights.items())
    sorted_items = sorted(weights.items(), key = lambda kv: (kv[1], kv[0]))
    # this basically sorts by probability first then by value
    # this list comprehension means we are just going to return the z values
    return [z for z,_ in sorted_items]

if __name__ == "__main__":
    X = [-1,50,1,50]
    Y = [-1,40,1,60]
    print(solution(X,Y))  # Expected output: [(0, 60), (2, 40)]

    X = [2,50,0,25,1,25]
    Y = [-1000, 100]
    print(solution(X,Y))  # [1000, 1001, 1004]
