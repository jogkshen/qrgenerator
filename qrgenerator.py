import qrcode
from tkinter import *

root=Tk()
root.title('Qr Code Generator')
root.geometry("520x520")
root.config(bg="white")


def gen_qr():
    dt=entry.get()
    qr=qrcode.make(dt)
    qr.save("C:\\Users\\Aspire\\Desktop\\python bigining\\qr.png")
   
    global Image
    Image = PhotoImage(file="C:\\Users\\Aspire\\Desktop\\python bigining\\qr.png")
    image_view.config(image=Image)



heading = Label(root, text="Qr Generator by Jogkshen", font="times 20")
heading.pack(fill=X)

subtitle = Label(root, text="Enter your text", font="times 16")
subtitle.pack(pady=20)

entry = Entry(root, text="", width=50, font="times 14")
entry.pack(pady=20)

button = Button(root, text="generate qr", width=20, command=gen_qr, font="times 14")
button.pack(pady=10)
    
image_view = Label (root, bg="white")
image_view.pack(pady=20)




root.mainloop()



