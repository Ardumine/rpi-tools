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
os.system("sudo chmod +x /usr/bin/updatepi")

installrdp = input("Install Xrdp(Microsoft remote desktop)? y/n:>")
installcode = input("Install VS code(A IDE for python, etc...)? y/n:>")
installffmeg = input("Install FFMPEG? y/n:>")
installpygame = input("Install Pygmae\turle for python? y/n:>")

if installrdp == "y":
	os.system("sudo apt-get install xrdp")
else:
	print("Skiping rdp installer...")
	
if installcode == "y":
	os.system("sudo apt-get install code")
else:
	print("Skiping vs code installer...")
	
if installffmeg == "y":
	os.system("sudo apt-get install ffmpeg")
else:
	print("Skiping ffmpeg installer...")

if installpygame == "y":
	os.system("sudo pip3 install pygame")
else:
	print("Skiping ffmpeg installer...")
print("Installlation complete!")
