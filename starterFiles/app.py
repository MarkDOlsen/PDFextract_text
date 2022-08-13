import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile


def open_file():
    # print("You clicked the button")
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode="rb", title="Choose a file", filetypes=[
                       ("Pdf file", "*.pdf")])
    if file:  # if file = true, we picked a file
        # print("File was successfully loaded")
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)  # read first page
        page_content = page.extract_text()
        # print(page_content)

        # text box
        text_box = tk.Text(root, height=10, width=50, padx=15,
                           pady=15)  # initialize text box

        # create the box
        text_box.insert(1.0, page_content)

        # justify the text in the text box
        # text_box.tag_configure("center", justify="center")
        # text_box.tag_add("center", 1.0, "end")

        # place the text box on the grid below the button
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")


#! CREATE AND SET UP WINDOW OBJECT
# code before window object created won't be in window
root = tk.Tk()  # create the window object

# initial window is tiny, resize with Canvas by setting pixel size
canvas = tk.Canvas(root, width=600, height=300)

# initialize canvas object with three columns
# the columns and rows let us place elements precisely
canvas.grid(columnspan=3, rowspan=3)

#! LOGO
# first create a pillow image
imagefile = "D:\Projects Library\!Code Projects\PythonSimplified\PDFExtract_text\PDFextract_text\starterFiles\logo.png"
logo = Image.open(imagefile)

# convert pillow to tkinter image
logo = ImageTk.PhotoImage(logo)

# now place it within a label widget - requires 2 lines of code
logo_label = tk.Label(image=logo)
logo_label.image = logo

# place with the window - put it in middle column and first row
logo_label.grid(column=1, row=0)

#! INSTRUCTIONS
instructions = tk.Label(
    root, text="Select a PDF file to extract all its text",
    font=("JMH Pulp Paperback", 14))
# spans 3 columns, underneath logo
instructions.grid(columnspan=3, column=0, row=1)

#! BROWSE BUTTON
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(),
                       font=("JMH Pulp Paperback", 14), bg="#20bebe", fg="white", height=2, width=15)
# font, bg color, fg color, height, width are optional parameters
# command is also optional, but without it pushing the button won't do anything

browse_text.set("Browse")  # initial text
browse_btn.grid(column=1, row=2)  # create the button

# copied the canvas and grid from above, changed height, removed rowspan to add padding at bottom
# this effectively adds another empty canvas underneath the button
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

#! INITIALIZE THE WINDOW OBJECT AND DISPLAY IT
root.mainloop()
# code after mainloop won't be in window
