import os
def is_root():
    return os.geteuid() != 0
if is_root():
	print("Please execute as root wiht sudo.")
	exit(1)
print("Starting installion... Please wait.")
f = open("/usr/bin/updatepi","w+")
f.write("#Ardumine raspberry pi tools \n")
f.write("sudo apt update \n")
f.write("sudo apt full-upgrade \n")
f.write("sudo apt auto-remove \n")
f.close()

print("Installlation complete!")
