import tkinter.messagebox

def showTip(title, content):
    condition = content == None or len(content)==0

    if(condition):
        print('The content is empty.')
        return
    
    tkinter.messagebox.showinfo(title='温馨提示', message=content)

def showWarning(title, content):
    condition = content == None or len(content)==0

    if(condition):
        print('The content is empty.')
        return
    
    tkinter.messagebox.showwarning(title='温馨提示', message=content)

def askForRetry(title, content):
    condition = content == None or len(content)==0

    if(condition):
        print('The content is empty.')
        return
    
    result = tkinter.messagebox.askretrycancel(title='温馨提示', message=content)
    return result