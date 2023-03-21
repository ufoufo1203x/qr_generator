import tkinter as tk
import qrcode
from png

class QRGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("QR Code Generator")

        # Creating input field and button for URL
        self.label = tk.Label(self.master, text="Enter URL:")
        self.label.pack()
        self.url_entry = tk.Entry(self.master)
        self.url_entry.pack()
        self.button = tk.Button(self.master, text="Generate QR Code", command=self.generate_qr)
        self.button.pack()

    def generate_qr(self):
        # Get the URL from the input field
        url = self.url_entry.get()

        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Display the QR code in a new window
        qr_window = tk.Toplevel(self.master)
        qr_image = tk.PhotoImage(data=img.tobytes())
        label = tk.Label(qr_window, image=qr_image)
        label.image = qr_image
        label.pack()

# Creating the main window
root = tk.Tk()

# Creating the QRGenerator object
qr_gen = QRGenerator(root)

# Running the main loop
root.mainloop()
