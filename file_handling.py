import os # this module provides a way of using Operating System dependent functionality
# must import this module to import remove() module
#python has several fn for creating, reading, updating and deleting files.

#fn open()
#open() fn takes two parameters: filename, mode
#4 modes - "r" read, "a" -append, "w" write, "x" create a file,error if it alreay exists
#in addition you can specify the file mode as text or binary with "t" or "b"
#example "rt" - read the text (it is default value, incase you do not provide mode, it takes as "rt")

#f = open("example_file1.txt") #this would error because file does not exist, to creat either give append or write or create
#f =open("example_file2.txt","w") #this will create file in the location, will error out if file already exists
f =open("example_file2.txt", "a") #(switch this with "w" and "a" to see the changes, "w" overrites, "a" appends)
f.write("Hello! I am Paramjoth, I am trying to learn Python for a very long time now \n")
f.close()

#the open() method returns a file object, which has a read() method for reading the contents
#print(f.read()) this would fail because you would have to go to read mode and then use read()
p =open("example_file2.txt","r")
print(p.read())

#to delete a file you must import OS module and run its os.remove() method
os.remove("example_file2.txt")
print("removed file example_file2.txt")

if os.path.exists("hello_world.py"):
    os.remove("hello_world.py")
    print("deleted hello_world.py file")
else:
    print("file hello_world.py does not exists")


#os.rmdir("data_extraction")
#print("deleted dir data_extarction")
os.mkdir("data_extarction")
print("create empty directory data_extraction")

