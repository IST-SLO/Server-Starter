import os
import time
import sys
import subprocess
from tkinter import *

'''
let me take this moment to apologize for my python code
i am entirely self-taught so i have no idea how python goes

general flow of program:
1) main method calls the menu creation method, and then waits for input
2) upon

a) in the /home/slo/server_configs folder, there are .txt files that this program runs to start and stop each server
   more documentation of them is available in that folder under the name readme.sh
'''

#yes these are global variables, fight me
user = ""
servers = {}

'''
  / /													  \\
/ /			   HERE BE METHODS		\\
\ \														  //
  \ \													   //
'''
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
		dir_list = os.listdir("//home//" + user + "//server_configs")
		dir_list.remove("readme.md")
		for entry in dir_list:
			f = open("//home//" + user + "//server_configs//" + entry, "r")
			line = f.readline().strip("\n")
			if line not in servers:
				servers.update({
					line : [
						"//home//" + user + "//server_configs//" + "Start_" + entry.split("_")[1] ,
						"//home//" + user + "//server_configs//" + "Stop_" + entry.split("_")[1] ,
						"//home//" + user + "//server_configs//" + "Update_" + entry.split("_")[1],
						0
					]
				})
			f.close()
	except:
		pass
		#print("unexpected error:" +  sys.exc_info()[0])
	#print(servers)
	print(list(servers.items())[1][0])
		
def pid_checker():
	pass
	
def server_launcher(sel):
	print(sel)
	global servers
	print(list(servers.items())[sel][1][0])
	f = open(list(servers.items())[sel][1][0])
	commands = f.read().splitlines()
	
	
'''
  / /													  \\
/ /			   HERE BE CLASSES		  \\
\ \														  //
  \ \													   //
'''
class Application(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		# hi button
		self.hi_there = Button(self, text="Refresh Servers", command=create_menu)
		self.hi_there.pack(side="top")
		# terminal
		self.termf = Frame(root, height=400, width=500)
		wid = self.termf.winfo_id()
		os.system('xterm -into %d -geometry 120x80  -sb -e "//home//slo//Server-Starter//tmux.cfg" &' % wid)
		self.termf.pack(fill=BOTH, expand=YES, side="right")
		# quit
		self.quit = Button(self, text="QUIT", fg="red",
							  command=self.master.destroy)
		self.quit.pack(side="bottom")
		
		# button generator
		self.server_butts = [] # i am extremely mature
		for i in range (len(servers)):
			print(i)
			self.server_butts.append(Button(root, text=list(servers.items())[i][0], command= lambda: server_launcher(i)))
			self.server_butts[i].pack()


if __name__ == "__main__":
	get_user()
	create_menu()
	root = Tk()
	app = Application(master=root)
	app.mainloop()
	'''
	get_user()
	#while(True):
	root = Tk()
	termf = Frame(root, height=768, width=1024)
	hello_world = Button(root)
	hello_world['text'] = "meme"
	hello_world['command']=
	termf.pack(fill=BOTH, expand=YES)
	wid = termf.winfo_id()
	os.system('xterm -into %d -geometry 40x20 -sb &' % wid)

	root.mainloop()
	
	
	print("Welcome to the IST SLO server interface!")
	print("created by VP Finch 2020-2021, messagable at altmcman@gmail.com")
	print("\nChoose a server to start by typing its corresponding number:\n")
	# note: I have no formal python training so if you wanna restructure this to be better, have at it
	create_menu()
	pid_checker() # todo: check if servers are still running via PID
	try:
		server_launcher(int(input("\n\n>"))-1)
	except ValueError:
		print("that value sucks, try using another")
	except:
		print("unexpected error:" +  sys.exc_info()[0])
	time.sleep(2)
	'''

		
		
	


# steamcmd +login anonymous +force_install_dir ../czero +app_set_config 90 mod czero +app_update 90 +quit
