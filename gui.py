# -*- coding: utf8 -*-

import tkinter as tk

def guiMain():
    root_window = tk.Tk()
    root_window.geometry("400x400")
    root_window.title("AutoFishing")

    mainFrame = tk.Frame(root_window, padx=10, pady=10)
    mainFrame.grid()

    floatCheckRangeLabel = tk.Label(mainFrame, text="FloatCheckRange:")
    floatCheckRangeLabel.grid(row=0, column=0, sticky=tk.W)
    floatCheckRangeFrame = tk.Frame(mainFrame)
    floatCheckRangeFrame.grid(row=0, column=1, sticky=tk.W)
    floatCheckRangeX = tk.Entry(floatCheckRangeFrame, width=5)
    floatCheckRangeX.grid(row=0, column=0)
    floatCheckRangeLX = tk.Label(floatCheckRangeFrame, text="x")
    floatCheckRangeLX.grid(row=0, column=1)
    floatCheckRangeY = tk.Entry(floatCheckRangeFrame, width=5)
    floatCheckRangeY.grid(row=0,column=2)

    floatCheckIntervalLabel = tk.Label(mainFrame, text="FloatCheckInterval:")
    floatCheckIntervalLabel.grid(row=1, column=0, sticky=tk.W)
    floatCheckIntervalFrame = tk.Frame(mainFrame)
    floatCheckInterval = tk.Entry(floatCheckIntervalFrame, width=5)
    floatCheckInterval.insert(0, "0.4")
    floatCheckInterval.grid(row=0, column=0, sticky=tk.W)
    secLabel = tk.Label(floatCheckIntervalFrame, text="Sec")
    secLabel.grid(row=0, column=1, sticky=tk.W)
    floatCheckIntervalFrame.grid(row=1, column=1, sticky=tk.W)

    autoLogoutLabel = tk.Label(mainFrame, text="AutoLogout")
    autoLogoutLabel.grid(row=2, column=0, sticky=tk.W)
    autoLogoutCheckBox = tk.Checkbutton(mainFrame)
    autoLogoutCheckBox.grid(row=2, column=1, sticky=tk.W)

    buttonFrame = tk.Frame(mainFrame, bg="tan", width=80)
    buttonFrame.pack()
    runScriptButton = tk.Button(buttonFrame, text="Run", command=lambda: buttonExecute())
    runScriptButton.pack(fill=tk.BOTH, expand=True)
    buttonFrame.grid(row=0, column=2, rowspan=3, sticky=tk.N+tk.S)

    root_window.mainloop()

def buttonExecute():
    print "hoge"

if __name__ == "__main__":
    guiMain()
