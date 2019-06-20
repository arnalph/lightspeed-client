import tkinter
import client
import socket

tk = tkinter.Tk(screenName=None,  baseName=None,  className='Light Speed',  useTk=1)
tk.title('Light Speed') 
tk.geometry('250x200')

tkinter.Label(tk, text='Enter Server URL', padx=70).pack()
c = client.Client((socket.socket(socket.AF_INET, socket.SOCK_STREAM)),'127.0.0.1','291550',8200)
tkinter.Button(tk, text='Start Brawlhalla', command=c.connect).pack()

tk.mainloop()
