# introstring="My name is Sanvi. I am 14 years old. I study in JPS Academy"
# words=introstring.split()
# print(words)

#user defined functions
'''
def functionName():

def functionName(variable):

'''

# def greet(name):
#     print("Hello! "+name+". How are you")
# greet("Sanvi")

def countWordsFromFile():
    filename=input("Enter a file name: ")
    file=open(filename,"r")
    numberofwords=0
    for line in file:
        words=line.split()
        numberofwords=numberofwords+len(words)
    print(numberofwords)
countWordsFromFile()
