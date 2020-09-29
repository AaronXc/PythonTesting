import subprocess
# first attempt at iteration and running command line programs
# look through a file and grep a line for "someString"
#subprocess.run(["cd", "~/TestMyPy"])
subprocess.run(['ls', "etc"])
someString = input("enter some text to look for")
if subprocess.run(["ls", "/etc", "|", "grep", "someString", "|", "wc", "-l" ]):
    count = subprocess.run(["cat", "/etc", "|", "grep", "someString", "|", "wc", "-l" ]):
    print("succesfully found %2.1i instances of that string"% (count))
    
else:
        print("no instances of that text found")
    