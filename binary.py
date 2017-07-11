def toDenary(binaryNum):
    binaryNum=str(binaryNum)
    totalNumber=0
    numValue=1
    binaryNum=binaryNum[::-1] #reverses string
    
    for digit in binaryNum:
        if digit=='1': #if the digit is 1, add its corresponding value to the total
            totalNumber+=numValue
        numValue*=2 #doubles value; 1,2,4,8 etc. (binary)
    return totalNumber



def toBinary(denaryNum):
    denaryNum=int(denaryNum)
    binaryNums=[]
    value=1
    
    #below while creates list of binary numbers up to max value
    while True:
        binaryNums.append(value)
        value*=2
        if value>denaryNum:
            break

    binaryNums=binaryNums[::-1] #reverse list
    translated=''
    for num in binaryNums:
        if denaryNum>=num: #if the current binary number fits into the running total
            denaryNum-=num #subtract it
            translated+='1'#and add a 1 to the message
        else:              #if it doesn't fit: 
            translated+='0'#add a 0
    return translated

if __name__=="__main__":
    mode=input('What do you want to convert to, binary (b) or denary (d)? \n')[0].lower()
    if mode=='b':
        print (toBinary(input("Input denary number \n")))
    else:
        print (toDenary(input("Input binary number \n")))
