filepath = r"C:\Users\USER\Desktop\Random\College\Github\Year 2\Lossless_Compression_Techniques\ExampleText.txt"

with open("ExampleText.txt",'r') as fh:
    data = fh.read()
    compressedData = ''
    count = 1
    for index in range(1,len(data)):

        if data[index - 1] == data[index]:
            count += 1
        else:
            compressedData +=  data[index - 1]  + str(count)
            count = 1
    print(compressedData)