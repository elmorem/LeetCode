'''
write a function name solution (X,Y,Z that takes as arguments)
the given three arrays of integers of X,Y,Z of equal size this function 
should result in a function of the form:
Z =a*x^2 +b*y^2
with interger values a and b that has the nest fire to the given sets 
of points using Mean Absolute Error Metric (MAE). return the array 
with to integers [a,b].
for example:
1. fiven the arrays X = [1,2], Y =[2,2], Z = [9,12], the 
function should return [1,2] because z = 1*x^2 + 2*y^2 fits the points

2. given the array X= [1,-2,3], Y = [-1,2,-100], Z =[2,8,10008],
the function should return [1,1] because z = 1*x^2 + 1*y^2 fits the points

'''
def solution(X,Y,Z):
    x2 = [x*x for x in X]
    y2 = [y*y for y in Y]
    best_mae = float('inf')
    best_a, best_b = 0,0
    for a in range(-100,101):
        for b in range(-100,101):
            total_abs_err = 0
            for xi2, yi2, zi in zip(x2,y2,Z):
                pred = a*xi2 + b*yi2
                total_abs_err += abs((pred-zi))
            mae = total_abs_err/len(Z)
            if mae < best_mae:
                best_mae = mae
                best_a, best_b = a,b
    return [best_a, best_b]
if __name__ == "__main__":
    X = [1,2]
    Y = [2,2]
    Z = [9,12]
    print(solution(X,Y,Z))  # Expected output: [1,2]

    X = [1,-2,3]
    Y = [-1,2,-100]
    Z = [2,8,10008]
    print(solution(X,Y,Z))  # Expected output: [1,1]