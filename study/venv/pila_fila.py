def simpleArraySum(ar):
    sum = 0
    for i in ar:
        sum = sum + i

    return sum

def solve(a0, a1, a2, b0, b1, b2):
        total_a = 0
        total_b = 0
        array_a = []
        array_b = []
        array_a.append(a0)
        array_a.append(a1)
        array_a.append(a2)
        array_b.append(b0)
        array_b.append(b1)
        array_b.append(b2)

        for i in range(2):
            if array_a[i] > array_b[i]:
                total_a = total_a + 1

            elif array_b[i] > array_a[i]:
                total_b = total_b + 1
        return total_a, total_b

def diagonalDifference(a):
    suma_diagonalprincipal = 0
    suma_diagonalsecundaria = 0
    n=len(a)
    for i in range(len(a)):

        suma_diagonalprincipal = suma_diagonalprincipal + a[i][i]
        suma_diagonalsecundaria = suma_diagonalsecundaria + a[i][n-i-1]






    dif = suma_diagonalprincipal - suma_diagonalsecundaria
    return dif

def gradingStudents(grades):

    for i in range(len(grades)):
        if grades[i] > 38 or grades[i]== 38:

            if (grades[i]%5)==0:
                if ((grades[i]+5)-grades[i])<3:

                    grades[i]=grades[i]+5

            elif ((grades[i]+1)%5)==0:
                if (grades[i]+1-grades[i])<3:
                    grades[i]=grades[i]+1
            elif ((grades[i]+ 2) % 5)==0:
                if grades[i]+2-grades[i]<3:
                    grades[i]=grades[i]+2
            elif ((grades[i]+3)%5)==0:
                if grades[i]+3-grades[i]<3:
                    grades[i]=grades[i]+3
            elif ((grades[i]+4)%5)==0:
                if grades[i]+4-grades[i]<3:
                    grades[i]=grades[i]+4
    return grades


grades=[73,67,38,33]


def factorial(n):
    if n==1:
        return 1
    else:
        fact=0
        fact=factorial(n-1)*n

    return fact


def tipo_variables(i,d,s):
    i = int(input())
    d = float(input())
    s = input()

    # Read and save an integer, double, and String to your variables.

    # Print the sum of both integer variables on a new line.
    print(int(i + d))

    # Print the sum of the double variables on a new line.
    print(2 * d)

    # Concatenate and print the String variables on a new line
    # The 's' variable above should be printed first.
    #print(s, "is the best place to learn and practice coding!.")


class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age=initialAge

    def amIOld(self):
        if self.age<13:
            print("You are young.")
        elif self.age>=13 and self.age<18:
            print("You are teenager.")
        else:
            print("You are old.")


    # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
# Increment the age of the person in here
        self.age=self.age+1


def binario_funcion(n):
    cont = 0
    while (int(n/2) >= 1):

        if int(n % 2) == 1:
            cont = cont + 1
        n = int(n / 2)
    cont = cont + 1





    #return cont

'''N = int(input())
lista=[]

for i in range(N):
    op=input().split()
    if op[0]=="insert":
        lista.append[int(op[1]),int(op[2])]
        print(lista)
    elif op[0]=="print":
        print(lista)
    elif op[0]=="remove":
        for i in lista:
            if i==op[1]:
                lista.remove(i)
        print(lista)
    elif op[0]=="append":
        lista.append(op[1])
        print(lista)
    elif op[0]=="sort":
        lista.sort()
        print(lista)
    elif op[0]=="pop":
        lista.pop()
        print(lista)
    elif op[0]=="reverse":
        lista.reverse()
        print(lista)'''

def split_and_join(line):
    line=line.split(" ")
    line = "-".join(line)
    return line

'''line = input()
result = split_and_join(line)
print(result)'''


def count_substring(string, sub_string):
    n = len(string)
    cont = 0
    for i in range(n):
        if sub_string[0] == string[i]:
            j = 1
            z = i + 1

            while (j < len(sub_string) and sub_string[j] == string[z]):
                j = j + 1
                z = z + 1
            if j == len(sub_string):
                cont = cont + 1

    return cont

def array_left_rotation(a, n, k):
    for i in range(k):
        x = a[0]
        for j in range(n - 1):

            a[j] = a[j + 1]
        a[n - 1] = x
    return a
#if __name__ == '__main__':
    # string = input().strip()
    # sub_string = input().strip()
    #
    # count = count_substring(string, sub_string)
    # print(count)




    #n, k = map(int, input().strip().split(' '))
    #a = list(map(int, input().strip().split(' ')))
    #answer = array_left_rotation(a, n, k);
    #print(*answer, sep=' ')








