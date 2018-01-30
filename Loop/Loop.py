## for loop
def for_loop():
    for i in 'letter':
        print(i)
    fruits = ['banana', 'apple',  'mango']
    for i in fruits:
        print(i)

##Iterating by Sequence Index
def ite_seq():
    fruits = ['banana', 'apple', 'mango']

    for i in range(len(fruits)):
        print(fruits[i])

def nested_loop():
    for i in range(5):
        for j in range(5):
            print('*',end='', flush=True)
        print("\n",end='', flush=True)

def nested_with_condition():
    for i in range(10):
        for j in range(i):
            if i <= 5:
                print('*',end='', flush=True)
        print("\n", end='', flush=True)







if __name__ == '__main__':
    #for_loop()
    #ite_seq()
    nested_loop()
    nested_with_condition()
