import sys
import time

def getfile():
    
    file = open("My_csv.txt", "w") #the destination file the w depicts I want to write to the file
    filename = input("What file would you like to process: ") #input or type file name you wish to process
    print ("OK, you want to process this file:", filename)
    time.sleep(2) #suspends my code for 2 seconds
    yesno = input("Enter yes or no to confirm: ") #confirm file by typing a yes or a no. yesno is a variable
    if yesno == "yes" or yesno == "y" or yesno == "Yes": #trying out if/then logic flow and yesno logic
        print("patience...")
        time.sleep(1)
        openfile = open(filename, 'r') #open file and read 
    
        for line in openfile: #iterate thru each line
            var1 = line.replace("\n", ",") # for each line replace \n with a comma. \n same as line feed
            file.write("%s\n" % var1) #writing the results to My_csv.txt
            
        file.close()    
        print("Done") #tell me when this is complete
            
    elif yesno == "no" or yesno =="n":
        print("OK, let's start over")
        newfilename = input("OK, what file would you like processed?\n")
        print("patience...")
        time.sleep(1)
        openfile = open(newfilename, 'r')

        for line in openfile:
            var1 = line.replace("\n", ",") #replace \n with a comma
            file.write("%s\n" % var1) #writing file
            
        file.close()    
        print("Done")    
                     
getfile()
