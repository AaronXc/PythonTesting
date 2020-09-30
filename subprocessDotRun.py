import subprocess
#
# some more arguments to add to the kwargs keymap are listed below:
###########################################################################
#, "|", "grep", message
#"input": message
#, "shell": True
#, "stdin": subprocess.PIPE
#, "universal_newlines": True
#
# "stderr": subprocess.PIPE

message = input("this will be the grep pattern")
kwargs={ }
#subprocess.run(['cd'])
grepThis = subprocess.run(['ls', '/usr/bin/'], stdout=subprocess.PIPE).stdout
print(subprocess.run(['ls', '/usr/bin/']))
grepResults = subprocess.run(["grep", message, grepThis], stdout=subprocess.PIPE).stdout
#subprocess.run(["echo", message], **kwargs).stdout

#p1 = subprocess.Popen(["echo", message], **kwargs)
#p1.communicate(input=message) 
#print(p1.communicate()) 

