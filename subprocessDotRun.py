import subprocess
#
# some more arguments to add to the kwargs keymap are listed below:
#------------------------------------------------
#, "|", "grep", message
#"input": message
#, "shell": True
#, "stdin": subprocess.PIPE
#, "universal_newlines": True
#, "stdout": subprocess.PIPE
message = input("this will be the grep pattern")
kwargs={"stderr": subprocess.PIPE }
#subprocess.run(['cd'])
subprocess.run(['ls', '/usr/bin/'], **kwargs)
print(subprocess.run(['ls', '/usr/bin/', "|", "grep", message], **kwargs))
#subprocess.run(["echo", message], **kwargs).stdout

p1 = subprocess.Popen(["echo", message], **kwargs)
#p1.communicate(input=message) 
print(p1.communicate()) 

