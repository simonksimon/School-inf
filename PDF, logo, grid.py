import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root=tk.Tk()

canvas=tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)

logo=Image.open("my logo.png")
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.image=logo
logo_label.grid(column=1,row=0)

instructions=tk.Label(root, text="Vyber PDF súbor na svojom počítači na extrahovanie.")
instructions.grid(columnspan=3, column=0, row=1)

def open_file():
    file=askopenfile(parent=root,mode="rb",title="Vyberte si súbor",filetype=[("PDF súbor","*.pdf")])
    if file:
        #read_pdf = PyPDF2.PdfFileReader(file)
        read_pdf = PyPDF2.PdfReader(file)
        page=read_pdf.pages[0]
        page_content=page.extract_text()

        text_box=tk.Text(root,height=10,width=50,padx=15,pady=15)
        text_box.insert(1.0,page_content)
        text_box.grid(column=1,row=3)

browse_text=tk.StringVar()
browse_btn=tk.Button(root,textvariable=browse_text,command=lambda:open_file())
browse_text.set("Hľadaj.")
browse_btn.grid(column=1, row=2)

root.mainloop()