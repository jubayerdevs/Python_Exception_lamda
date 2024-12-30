try:
    file = open("data.txt","r")
    #something to do with the file
    #error wala line
    #file.close();
    #print(file)
except:
    print("Error while reading the file")
finally:
    file.close();
