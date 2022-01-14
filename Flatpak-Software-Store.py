import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import *

a = Tk()

a.geometry("550x550")
a.title("Software Store")

searchsw = tk.StringVar()

def installwin():
  installwin_btn.config(relief = "flat")
  uninstallwin_btn.config(relief = "groove")
  uni_btn.config(text = "Install", command = install)
  hello_label.place_forget()
  installed_label.place_forget()
  list.delete(0,END)
  search_entry.delete(0,END)
  search_entry.place(x=15,y=43,width=400,height=30)
  search_btn.place(x=430,y=43, width = 108)

def uninstallwin():
  uninstallwin_btn.config(relief = "flat")
  installwin_btn.config(relief = "groove")
  uni_btn.config(text = "Uninstall", command = uninstall)
  hello_label.place_forget()
  search_entry.place_forget()
  search_btn.place_forget()
  list.delete(0,END)
  installed_label.place(x=15,y=48)
  val1 = subprocess.Popen("flatpak list | cut -f1,2", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  val2 = val1.stdout.read().decode("utf-8").replace("\t"," -- ").split("\n")
  val2_var = tk.StringVar(value = val2)
  list.delete(0,END)
  for apps_installed in val2:
    list.insert(tk.END, apps_installed)

def searchentry():
  value1 = subprocess.Popen(f"flatpak search {searchsw.get()} | cut -f1,2,3", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  value2 = value1.stdout.read().decode("utf-8").replace("\t"," -- ").split("\n")
  value2_var = tk.StringVar(value = value2)
  list.delete(0,END)
  for app_entry in value2:
    list.insert(tk.END, app_entry)

def install():
  app_selection = list.curselection()
  linelist = ",".join([list.get(i) for i in app_selection]).split()
  toinstall = linelist[-1]
  install_progress = Toplevel(a)
  install_progress.geometry("400x95")
  install_progress.title("Installing")
  label = tk.Label(install_progress, text = f"Installing {toinstall}")
  label.place(x=15,y=15)
  progressbar = ttk.Progressbar(install_progress, mode = "indeterminate", length = "370")
  progressbar.place(x=15,y=52)
  installexec = subprocess.Popen(f"flatpak install {toinstall} -y", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  progressbar.start()
  while installexec.poll() is None:
    progressbar.update()
  progressbar.stop()
  install_progress.destroy()
  fwin = Toplevel(a)
  fwin.geometry("400x95")
  fwin.title("Success")
  def okay():
    fwin.destroy()
  label1 = tk.Label(fwin, text = F"Successfully installed {toinstall}.").place(x=15,y=15)
  okay_btn = tk.Button(fwin, text = "Okay", command = okay, width = 43).place(x=14,y=53)
  fwin.mainloop()

def uninstall():
  app_selected = list.curselection()
  linelist = ",".join([list.get(i) for i in app_selected]).split()
  touninstall = linelist[-1]
  uninstall_progress = Toplevel(a)
  uninstall_progress.geometry("400x95")
  uninstall_progress.title("Uninstalling")
  label1 = tk.Label(uninstall_progress, text = f"Uninstalling {touninstall}")
  label1.place(x=15,y=15)
  progressbar = ttk.Progressbar(uninstall_progress, mode = "indeterminate", length = "370")
  progressbar.place(x=15,y=52)
  uninstallexec = subprocess.Popen(f"flatpak uninstall {touninstall} -y", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  progressbar.start()
  while uninstallexec.poll() is None:
    progressbar.update()
  progressbar.stop()
  uninstall_progress.destroy()
  fwin = Toplevel(a)
  fwin.geometry("400x95")
  fwin.title("Success")
  def okay():
    fwin.destroy()
  label2 = tk.Label(fwin, text = f"Successfully uninstalled {touninstall}.").place(x=15,y=15)
  okay_btn = tk.Button(fwin, text = "Okay", command = okay, width = 43).place(x=14,y=53)
  uninstallwin()
  fwin.mainloop()

def exit():
  a.destroy()

hello_label = tk.Label(a, text = "Choose one of the above options")
hello_label.place(x=15,y=48)
installwin_btn = tk.Button(a, text = "Install Software", command = installwin, width = 31)
installwin_btn.place(x=0,y=0)
uninstallwin_btn = tk.Button(a, text = "Uninstall Software", command = uninstallwin, width = 31)
uninstallwin_btn.place(x=275,y=0)
exit_btn = tk.Button(a, text = "Exit", command = exit, width = 10)
exit_btn.place(x=15,y=505)
uni_btn = tk.Button(a, text = "Hello", width = 10)
uni_btn.place(x=430,y=505)
list = tk.Listbox(a, relief = "flat")
list.place(x=15,y=83,width=523,height=410)

search_entry = tk.Entry(a, textvariable = searchsw, relief = "flat")
search_btn = tk.Button(a, text = "Search", command = searchentry)

installed_label = tk.Label(a, text = "Installed softwares:")

a.mainloop()