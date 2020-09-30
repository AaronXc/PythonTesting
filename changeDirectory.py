import subprocess
# attempt to change the present working directory
# , shell = True, stdout = subprocess.PIPE

#subprocess.run(['cd'])
subprocess.run(['ls', '/etc'])
print(subprocess.run(['ls', '/etc']))

   