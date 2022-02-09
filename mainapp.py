import urllib, json
from urllib import request, error
import socket
import tkinter as tk
from item import item
from hero import hero
from history import history
from detail import detail
from tkinter import ttk, filedialog, simpledialog
from tkinter.ttk import Style

if __name__ == '__main__':
    main = tk.Tk()
    main.title("Jonas")
    main.geometry("720x480")
    main.option_add('*tearOff',False)
    main.configure(background = '#121212')
    main.update()
    frame = tk.Frame(master = main, height = main.winfo_height()-50,width = main.winfo_width(),background = '#000000')
    frame.pack(fill=tk.BOTH)
    entry = tk.Entry(master = frame, font = "Calibri 12",fg = 'black',bd = 1, width = 50,justify = 'center',background = '#1c1c1e',foreground = '#ebebf5')
    entry.place(relx=0.5, rely= 0.5, anchor = 'center')
    account = entry.get()
    style = Style()
        
    def heroes():
        for i in frame.winfo_children():
            i.destroy()
        frame.update()
        listing = tk.Text(master = frame, font = 'Calibri 12 normal',height = main.winfo_height()-453,width=main.winfo_width())
        listing.tag_configure("center",justify='center')
        for i in hero().keys():
            listing.insert('1.0',i+'\n\n')
        listing.tag_add('center','1.0','end')
        listing.config(state=tk.DISABLED)
        
        
        entr = tk.Entry(master = frame,font = 'Calibri 12',fg='black',bd = 1,width = 50,justify = 'center',background='#1c1c1e',foreground = '#ebebf5')
        entr.pack(side = 'top')
        entr.insert(0,str(account))
        listing.pack()
    
    def items():
        for i in frame.winfo_children():
            i.destroy()
        frame.update()
        '''listing = tk.Text(master = frame, font = 'Calibri 12 normal',height = main.winfo_height()-453,width=main.winfo_width())
        listing.tag_configure("center",justify='center')
        for i in item().keys():
            listing.insert('1.0',i+'\n\n')
        listing.tag_add('center','1.0','end')
        listing.config(state=tk.DISABLED)
        listing.pack()'''
        tree = ttk.Treeview(frame,height = main.winfo_height()-453,columns=("Item"))
        tree.column('#1',width = main.winfo_width(),anchor = 'center')
        tree['show'] = 'headings'
        for i,j in enumerate(item().keys()):
            tree.insert(parent = '',index = 'end', iid=i,text = '',value = (j))
        entr = tk.Entry(master = frame,font = 'Calibri 12',fg='black',bd = 1,width = 50,justify = 'center',relief = 'ridge')
        entr.pack(side = 'top')
        entr.insert(0,str(account))
        tree.tag_configure('#1', background='lightgrey')
        tree.pack()
        

    herobtn = tk.Button(font = 'Calibri 12 normal',text = 'hero',width = 10,command = heroes,background = '#3a3a3c',foreground = '#ebebf5',relief = 'ridge')
    herobtn.pack(anchor = 's',side = 'left',padx = 15,pady = 15)
    itembtn = tk.Button(font = 'Calibri 12 normal',text = 'item',width = 10,command = items, background = '#3a3a3c',foreground = '#ebebf5',relief = 'ridge')
    itembtn.pack(anchor = 's',side = 'left',padx = 15,pady = 15)
    
    def text():
        def fixed_map(option):
            return [elm for elm in style.map("Treeview", query_opt=option)
                    if elm[:2] != ("!disabled", "!selected")]
            
        global account
        account = entry.get()
        for i in frame.winfo_children():
            i.destroy()
        frame.update()
        entri = tk.Entry(master = frame,font = 'Calibri 12',fg = 'black',bd = 1,width = 50,justify = 'center',background = '#3a3a3c',foreground = '#ebebf5')
        entri.pack(side='top')
        entri.insert(0,str(account))
        tree = ttk.Treeview(frame,height = 18,columns=("Hero",'KDA'))
        tree.tag_configure('', background = 'black',foreground = 'white')
        tree.column('#1',anchor='center')
        tree.column('#2',anchor='center')
        tree.pack(pady= 5)
        tree.heading('#0',text='GAME ID')
        tree.heading('#1',text='HERO')
        tree.heading('#2',text='KDA')
        h = hero()
        #style.configure('Treeview',background="#383838", foreground="white", fieldbackground="red")
        #tree.tag_configure('lose', background=[('selected','red')])
        #style.map('Treeview',background=[('active','#1c1c1e')])
        
        for i,j in enumerate(history(i = account)):
            a1 = None 
            a2 = None 
            for k in detail(account,j):
                for x,y in h.items():
                    if y == k[0]:
                        a1 = x
                        a2 = k[1]
            tree.insert(parent='',index='end',text=j,value=(a1,a2),tags=(''))
        
    btn = tk.Button(master = frame,font = 'Calibri 12 normal',text = 'Go',width = 5,command = text,background = '#3a3a3c', foreground = '#ebebef',relief = 'ridge')
    btn.place(relx=0.9,rely = .5,anchor = 'e')
    
    main.mainloop()
#358706417
