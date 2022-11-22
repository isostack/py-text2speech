import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
# Module for text to speech conversion
from gtts import gTTS

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=600)
canvas.grid(columnspan=3, rowspan=5)

#logos
logoone = Image.open('img/google.png')
logoone = ImageTk.PhotoImage(logoone)
logo_label = tk.Label(image=logoone)
logo_label.image = logoone
logo_label.grid(column=1, row=0)

logotwo = Image.open('img/convert.png')
logotwo = ImageTk.PhotoImage(logotwo)
logo_label = tk.Label(image=logotwo)
logo_label.image = logotwo
logo_label.grid(column=1, row=1)



#instructions
instructions = tk.Label(root, text="Select a PDF file to convert into AudioBook", font="Raleway")
instructions.grid(columnspan=3, column=0, row=2)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    audioname = file.name.split('/')[-1].split('.')[0]
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        # The text that you want to convert to audio
        audtext =  page_content
  
        # Language in which you want to convert
        language = 'en'
        # Passing the text and language to the engine, 
        # here we have marked slow=False. Which tells 
        # the module that the converted audio should 
        # have a high speed
        myobj = gTTS(text=audtext, lang=language, slow=False)
        
        # Saving the converted audio in a mp3 file named
        # welcome 
        myobj.save(f"{audioname}.mp3")

        #text box
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=4)

        browse_text.set("Browse")

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#474fa2", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=3)

logothree = Image.open('img/log.png')
logothree = ImageTk.PhotoImage(logothree)
logo_label = tk.Label(image=logothree)
logo_label.image = logothree
logo_label.grid(column=1, row=5)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()