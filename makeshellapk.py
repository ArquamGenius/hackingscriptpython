import os;
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
						
print("\033[33             __ ");
print('\033[33m       .-        -.');
print("\033[31m      /            \ ");
print();
print("\033[32m     |,  .-.  .-.  ,|  ");
print("\033[31m     | )(_ /  \_ )( |  ");
print("     |/     /\     \|       ");
print('\033[32m     <__    ^^  j9  __>');
print("\033[32m      \__|IIIIII|__/");
print();
print("\033[31m        \ IIIIII / ");
print("\033[31m         -------- " );
print("\033[31m            _ ");
input("\n\n\n\033[33mcontinue...");
print("\033[33m::::::::::::"*5);
print("\033[33m::::::::::::"*5);
print("\033[32m:::[1]\033[31m Hack");
print("\033[32m:::[2]\033[31m Hack")
print("\033[32m:::[3]\033[31m Hack")
print("\033[32m:::[4]\033[31m Hack")
print("\033[32m:::[5]\033[31m Hack")
print("\033[32m:::[6]\033[31m Hack")
print("\033[32m:::[7]\033[31m Hack")
print("\033[32m:::[8]\033[31m Hack")
print("\033[32m:::[9]\033[31m Hack")
print("\033[32m:::[10]\033[31m Hack")
print("\033[32m:::[11]\033[31m Hack")
print("\033[32m:::[12]\033[31m Hack")
print("\033[32m:::[13]\033[31m Hack")
print("\033[32m:::[14]\033[31m Hack")
print("\033[32m:::[15]\033[31m Hack")
print("\033[33m::::::::::::"*5);
print("\033[33m::::::::::::"*5);
option=input("");