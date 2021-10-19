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
installpygame = input("Install Pygame for python? y/n:>")
installguake = input("Install guake(user interface terminal that is transparent)? y/n:>")
installconky = input("Install conky(its like Htop)? y/n:>")
installcairo = input("Install Cairo Dock(its a dock for graphical user interface)? y/n:>")
installvokoscreen = input("Install vokoscreen (its a screen recorder)? y/n:>")
installopenvpn = input("Install OpenVPN(its a vpn client for raspberry pi )? y/n:>")

if installrdp == "y":
	print("Installing XRDP")
	os.system("sudo apt-get install xrdp -y")
else:
	print("Skiping rdp installer...")
	
if installcode == "y":
	print("Installing code")
	os.system("sudo apt-get install code -y")
else:
	print("Skiping vs code installer...")
	
if installffmeg == "y":
	print("Installing ffmeg")
	os.system("sudo apt-get install ffmpeg -y")
else:
	print("Skiping ffmpeg installer...")

if installpygame == "y":
	print("Installing pygame")
	os.system("sudo pip3 install pygame")
else:
	print("Skiping ffmpeg installer...")

if installffmeg == "y":
	print("Installing guake")
	os.system("sudo apt-get install guake -y")
else:
	print("Skiping guake installer...")

if installconky == "y":
	print("Installing conky")
	os.system("sudo apt-get install conky -y")
else:
	print("Skiping conky installer...")
	
if installcairo  == "y":
	print("Installing cairo-dock")
	os.system("sudo apt-get install cairo-dock -y")
else:
	print("Skiping cairo-dock installer...")
	
if installvokoscreen  == "y":
	print("Installing vokoscreen")
	os.system("sudo apt install vokoscreen -y")
else:
	print("Skiping vokoscreen installer...")

if installopenvpn  == "y":
	print("Installing openvpn")
	os.system("sudo apt install openvpn -y")
else:
	print("Skiping vokoscreen installer...")
print("Installlation complete!")
