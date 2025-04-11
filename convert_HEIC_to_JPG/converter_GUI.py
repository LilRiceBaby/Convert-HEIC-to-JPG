import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import pillow_heif  # registers HEIC support automatically

root = tk.Tk()
root.title("HEIC to JPG Converter")
canvas1 = tk.Canvas(root, width=300, height=250, bg="orange", relief="raised")
canvas1.pack()

label1 = tk.Label(root, text="HEIC Converter", bg="lightsteelblue2")
label1.config(font=("helvetica", 20))
canvas1.create_window(150, 60, window=label1)

im1 = None


def getHEIC():
    global im1
    import_file_path = filedialog.askopenfilename(filetypes=[("HEIC files", "*.heic")])
    try:
        im1 = Image.open(import_file_path)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open image: {e}")
        im1 = None


font = ("helvetica", 12, "bold")
bg = "royalblue"
fg = "white"

browseButton_HEIC = tk.Button(
    text="Import HEIC File", command=getHEIC, bg=bg, fg=fg, font=font
)
canvas1.create_window(150, 130, window=browseButton_HEIC)


def convertToJPG():
    global im1
    if im1 is None:
        messagebox.showerror("Error", "No File selected")
    else:
        export_file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        try:
            rgb_im = im1.convert("RGB")  # ensure it's in RGB before saving as JPG
            rgb_im.save(export_file_path, "JPEG")
            messagebox.showinfo("Success", f"File saved as: {export_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {e}")


saveAsButton_JPG = tk.Button(
    text="Convert HEIC to JPG", command=convertToJPG, bg=bg, fg=fg, font=font
)
canvas1.create_window(150, 180, window=saveAsButton_JPG)

root.mainloop()
