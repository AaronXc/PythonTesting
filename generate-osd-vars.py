import subprocess
# first attempt at iteration and running command line programs
# look through a file and grep a line for "someString"
#subprocess.run(["cd", "~/TestMyPy"])
subprocess.run(["ls"])
someString = input("enter some text to look for")
if subprocess.run(["cat", "c:/users/Aaron Wilcox/TestMyPy/listOfStuff"]):
    count = subprocess.run(["wc", "-l"])
    print("succesfully found %2.1i instances of that string"% (count))
