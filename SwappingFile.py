def swapDataFile():
    fileName1 = input("Enter the first File Name To Swape Data Of File: ")
    fileName2 = input("Enter the second File Name To Swape Data Of File: ")
    with open(fileName1,'r') as a:
        data_a = a.read()

    with open(fileName2,'r') as b:
        data_b = b.read()



    with open(fileName1,'w') as a:
        a.write(data_b)

    with open(fileName2,'w') as b:
        b.write(data_a)

    print("Swapped the File Data from " + fileName1 + " to " + fileName2 + "!")

swapDataFile()