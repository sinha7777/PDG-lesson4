coding=["python","HTML","CSS","C"]
print(coding)
print(coding[0])
print(coding[-1])

print(len(coding))

coding.append("Javascript")
print(coding)
coding.insert(1,"Java")
print(coding)

coding.pop()
print(coding)
coding.pop(3)
print(coding)

coding.remove("HTML")
print(coding)

#2d lists

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print("Number of rows:",len(matrix))
print("number of coloms:",len(matrix[0]))
print((matrix[1][1]))
print(matrix[0][2])

for i in range(3):#rows
    for j in range (3):#cols
        print(matrix[i][j],end="   ")
    print("\n")

#creating a matrix and printing.
rows=int(input("How many rows do you want?"))
cols=int(input("How many coloms do you want?"))

matrix1=[]
for i in range(rows):
    temp=[]
    for j in range(cols):
        x=int(input("Enter the numbers."))
        temp.append(x)
    matrix1.append(temp)

print(matrix1)
for i in range(rows):
    for j in range(cols):
        print(matrix1[i][j],end=" ")
    print("\n")

# creatng a square matrix and printing it's diagonals.

n=int(input("enter the dimesions of the square matrix."))

matrix2=[]
for i in range(n):
    temp=[]
    for j in range(n):
        s=int(input("enter the numbers."))
        temp.append(s)
    matrix2.append(temp)

print(matrix2)
for i in range(n):
    print(matrix2[i][i])