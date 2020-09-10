import os
import time

'''
general flow of program:
1) main method calls the menu creation method, and then waits for input
2) upon

a) in the /home/slo/server_configs folder, there are .txt files that this program runs to start and stop each server
   more documentation of them is available in that folder under the name readme.sh
'''

#yes this is a global variable, fight me
user = ""
def get_user():
	global user
	user = os.path.expanduser("~").split("/")[2]


def create_menu():
	dir_list = os.listdir("//home//" + user + "//server_configs")
	dir_list.remove("readme.md")
	for entry in dir_list:
		f = open("//home//" + user + "//server_configs//" + entry, "r")
		print(f.readline())
	time.sleep(1)
	

if __name__ == "__main__":
	get_user()
	while(True):
		print("Welcome to the IST SLO steamcmd interface!")
		print("created by VP Finch 2020-2021, messagable at altmcman@gmail.com")
		
		#create_menu()
		
		time.sleep(1)
		
	


# steamcmd +login anonymous +force_install_dir ../czero +app_set_config 90 mod czero +app_update 90 +quit
