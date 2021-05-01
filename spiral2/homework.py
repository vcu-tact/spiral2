def spiralize(size, n=1):
    dSum = n
    currentNum = n
    blocks = size * size + n - 1 
    counter = 0
    inc = 2


    while currentNum < blocks:
        currentNum = currentNum + inc
        dSum = dSum + currentNum
        counter+=1
    
        if counter % 4 == 0:
            inc = inc + 2
    return dSum

def main():
    test = spiralize (11,27)
    print(test)
    # just testing some code here 

if __name__ == "__main__":
    main()
