#imports
import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

# Select PDF file
book = askopenfilename()
if book:
    # Init PDF reader
    pdf = PyPDF2.PdfReader(book)
    pages = len(pdf.pages)
    readto_page = int(input("What page would you like to read to:"))
    while readto_page > pages:
        print("Page being read to must be less total number of pages. Please input again")
        readto_page = int(input("What page would you like to read to:"))
    # Initialize text-to-speech engine
    player = pyttsx3.init()

    # Extract and read text from each page
    for num in range(readto_page):
        page = pdf.pages[num]
        text = page.extract_text()
        if text:
            player.say(text)
            player.runAndWait()
else:
    print("No file selected.")

