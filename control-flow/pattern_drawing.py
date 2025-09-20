size = int(input("Enter the size of the pattern:"))
row = 0
while row < size: #outer loop → controls rows
    for col in range (size):# inner loop → controls columns
        print("*", end="") # print stars on the same line
    print() # move to the next line after a row
    row +=1 # increase the number of rows