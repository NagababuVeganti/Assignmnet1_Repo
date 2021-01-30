#importing math library for square root function
from math import *

def PrintTriangles(n):
    #Returns Void
    '''Logic :
       Each row will have previousrow +2 stars,so we assume (2*n-1) grids and fill in the stars and spaces
    '''
    '''Outer loop  iterates through the number of rows'''
    try:
        for i in range(0,n+1):
            '''Inner loops is responsible for printing before spaces and stars'''
            for j in range(0,(((2*n)-1)/2)-i):
                print(" ",end="")
                for j in range((2*i)+1):
                    print("*",end="")
                print("\n")
    except Exception :
        print("Unkniown Error")




def PrintPellSeries(n):
    #Returns Void
    ''' Logic:
    we initialize 2 varaibles a=0 and b=1 and follow the logoic c=2*b+a and swap accordingly
    '''
    try:
        a=0
        b=1
        #outer
        for x in range(n+1):
            c=(2*b)+a
            print(c,end=" ")
            a=b
            b=c
    except Exception :
        print("Unknown error")

def SquareSums(n):
    #returns boolean value
    ''' Logic:
    Given N we start our search from 1 to Square root(N) and check if there are any two squares that
    add up to given N if yes we stop loop and return True else after end of loop we return False
    '''
    try:
        squareroot=int(sqrt(n))
        for i in range(0,squareroot+1):
            for j in range(0,squareroot+1):
                if(i**2 + j**2 ==n):
                    return True
                if(i**2 + j**2 > n):
                        ''' when the sum exceeds we break the loop as we know we already crossed it'''
                        break
        return False
    except Exception:
        print("unknwon Exception")

def DiffPairs(nums,K):
    #Returns INT I.e NUmber of pairs
    ''' Logic
    we store the numbers in the dictionary(hasmap with frequency).
    frequency of number is used in the case where K=0

    After that for each item in array we search of compliment of it, i.e a-b=k so we
    search for a=k+b in the dictionary.

    '''
    try:
        #declaration of dict
        numbers_dic={}
        count=0
        pairs=set()
        for i in nums:
            if(numbers_dic.get(i)==None):
                numbers_dic[i]=1
            else:
                numbers_dic[i]+=1

        #we iterate through the array
        for i in nums:
            temp=K+i
            if(temp == i):
                if(numbers_dic.get(temp)>1):
                    pairs.add((i,i))
            else:
                        if (numbers_dic.get(temp)!=None):
                            pairs.add((i,temp))
        print(pairs)
        return len(pairs)
    except Exception:
        print("unkown Exception")


def UniqueEmails(emails):
    '''logoic
    First we preprocess all the emails based on given conditions  and store in the list

    Then we iterate through all the emails in the  list and check for same emails after preprocessing then return result
    '''
    preprocessedEmails=[]
    count=0
    for i in emails:
        #Initalizing Temperary string
        temp=''
        index=0
        ignore=False
        for j in i:
            index+=1
            if j=='@':
                temp+=i[index-1:]
                preprocessedEmails.append(temp)
                break
            if ignore==True:
                continue;
            if j=='+':
                ignore=True
                continue
            elif j=='.':
                continue
            else:
                temp+=j

    #print(preprocessedEmails)
    for i in range(len(emails)):
        temp=0
        for j in range(i,len(emails)):
            if preprocessedEmails[i]==preprocessedEmails[j]:
                temp+=1
        count=max(temp,count)
    return count



def DestCity(cities):
    #returns City
    '''Logic:
    Since there is are no cycles in the graph the destination city wont be having any out going edges
    so after storing edges in the dictionary the city with no out going edges will be destination city.
    '''
    try:
        data={}
        for i in cities:
            print(i)
            if data.get(i[0])==None:
                data[i[0]]=[i[1]]
            else:
                data[i[0]].append(i[1])
                if data.get(i[1])==None:
                    data[i[1]]=[]
        for i in data.keys():
            if len(data[i])==0:
                return i
    except Exception:
        print("Unknwon Exception")
#print(DiffPairs([1, 2, 3, 4, 5],1))

if __name__ == "__main__":
    try:
        #Question 1
        print("Q1 : Enter the number of rows for the traingle:")
        printTriangle(int(input()))
        print("\n\n\n")

        #Question 2
        print("Q2 : Enter the number of terms in the Pell Series:")
        printPellSeries(int(input()))
        print("\n\n\n")

        #Question 3
        print("Q3 : Enter the number to check if squareSums exist:")
        falg=squareSums(int(input()))
        if flag:
            print("Yes, the number can be expressed as a sum of squares of 2 integers")
        else:
            print("No, the number cannot be expressed as a sum of squares of 2 integers")

        #Question 4
        a=[ 3, 1, 4, 1, 5 ]
        print("Q4: Enter the absolute difference to check:")
        k=int(input())
        x=diffPairs(a,k)
        print("There exists {0} pairs with the given difference".format(x))
