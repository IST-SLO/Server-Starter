import os
import time

'''
general flow of program:
1) main method calls the menu creation method, and then waits for input
2) upon

a) in the /home/slo/server_configs folder, there are .txt files that this program runs to start and stop each server
   more documentation of them is available in that folder under the name readme.sh
'''

#yes these are global variables, fight me
user = ""
servers = {}
server_count = 0 #you could probably do this with dicts but nah


def get_user():
	global user
	user = os.path.expanduser("~").split("/")[2]

# this is kinda dumb and inefficent but like, it doesnt matter
def create_menu():
	# first, get all options in ~/server_configs (initally, and when a server just started)
	global servers
	global server_count
	try:
		os.mkdir("//tmp//istslo//")
		os.mkdir("//tmp//istslo//servers_running//")
	except FileExistsError:
		pass
		
	try:
		if len(servers) == 0 or len(os.listdir("//tmp//istslo//servers_running//")) !=  server_count: 
			dir_list = os.listdir("//home//" + user + "//server_configs")
			dir_list.remove("readme.md")
			for entry in dir_list:
				f = open("//home//" + user + "//server_configs//" + entry, "r")
				line = f.readline().strip("\n")
				if line not in servers:
					servers.update({line : "//home//" + user + "//server_configs//" + entry})
				f.close()
	except:
		print("unexpected error:" +  sys.exc_info()[0])
		
	# next, print it all to the screen
	i = 0
	for line in servers:
		print(str(i+1) + ") " + line)
		i+=1
		
def pid_checker():
	pass
	
def server_launcher(sel):
	global servers
	print(list(servers.items())[sel-1])
	#f = open(list(servers.items()[sel]))
	#f.readline()
		

if __name__ == "__main__":
	get_user()
	while(True):
		print("Welcome to the IST SLO steamcmd interface!")
		print("created by VP Finch 2020-2021, messagable at altmcman@gmail.com")
		print("\nChoose a server to start by typing its corresponding number:\n")
		
		create_menu()
		pid_checker() # todo: check if servers are still running via PID
		try:
			server_launcher(int(input("\n\n>")))
		except ValueError:
			print("that value sucks, try using another")
		except:
			print("unexpected error:" +  sys.exc_info()[0])
		time.sleep(2)
		
	


# steamcmd +login anonymous +force_install_dir ../czero +app_set_config 90 mod czero +app_update 90 +quit
