matrix = [[1],
          [8,4],
          [2,6,9],
          [8,5,9,3]]
matrix2 = [[215],
           [193,124],
           [117,237,442],
           [218,935,347,235],
           [320,804,522,417,345],
           [229,601,723,835,133,124],
           [248,202,277,433,207,263,257],
           [359,464,504,528,516,716,871,182],
           [461,441,426,656,863,560,380,171,923],
           [381,348,573,533,447,632,387,176,975,449],
           [223,711,445,645,245,543,931,532,937,541,444],
           [330,131,333,928,377,733,17,778,839,168,197,197],
           [131,171,522,137,217,224,291,413,528,520,227,229,928],
           [223,626,34,683,839,53,627,310,713,999,629,817,410,121],
           [924,622,911,233,325,139,721,218,253,223,107,233,230,124,233]]
#Checks the number if it is prime
def isPrime(matrix,x,y):
    num=matrix[x][y]
    if num <=1:
       return 0 
    for i in range(2,num):
        if num%i==0:
            return 0
    return 1;
#Finds the maximum sum of the numbers that is not prime
def maxSum(matrix,x,y,sum):
    if (x+1 == len(matrix)):
        return matrix[x][y]
    
    if (isPrime(matrix, x, y) == 1) or ((isPrime(matrix, x+1, y) == 1) and (isPrime(matrix, x+1, y+1) == 1)):
        return 0
    
    return matrix[x][y]+max(maxSum(matrix, x+1, y+1, sum), maxSum(matrix, x+1, y, sum))
    
if __name__ == "__main__":
    max_sum =maxSum(matrix,0,0,0)
    print("Max Sum Matrix 1: ",max_sum)
    
    max_sum = maxSum(matrix2, 0, 0, 0)
    print("Max Sum Matrix 2: ", max_sum)
