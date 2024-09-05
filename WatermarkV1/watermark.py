import fitz  # PyMuPDF
import os
import datetime

def add_watermark(PDF_Path, Approver, Out_Path=None):
    # Use os.path.splitext() to get file name and extension
    file_name = os.path.splitext(os.path.basename(PDF_Path))[0]
    print(file_name)
    
    # Open PDF via PyMuPDF
    doc = fitz.open(PDF_Path)
    
    # Get current time
    now = datetime.datetime.now()
    
    # Transform to friendly string
    formatted_date = now.strftime("%Y/%#m/%#d %H:%M:%S")
    page = doc[0]  # new page, or choose doc[n]
    
    # The text strings, each having 3 lines
    remark_text = f" Confirmed by: {Approver}\n Confirm time: {formatted_date}"
    
    # Get center of the page
    center_x = page.rect.width / 2
    center_y = page.rect.height - 50  # Place the text at the bottom of the page, leaving some whitespace
    p1 = fitz.Point(center_x - 40, center_y + 25)
    
    # Create a Shape to draw on
    shape = page.new_shape()
    
    # Draw the insertion points as red, filled dots
    shape.draw_circle(p1, 1)
    red = (1, 0, 0)  # RGB for red
    
    # Insert the text strings
    shape.insert_text(p1, remark_text, color=red, fontname="helv")
    
    # Store our work to the page
    shape.commit()
    
    # Output modified pdf
    if Out_Path is None:
        doc.save(f"{file_name}_added.pdf")
    else:
        doc.save(os.path.join(Out_Path, f"{file_name}_added.pdf"))
