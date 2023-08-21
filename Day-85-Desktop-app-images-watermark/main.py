import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarking App")

        self.canvas = Canvas(self.root, width=300, height=300)
        self.canvas.pack()

        self.upload_button = Button(self.root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.watermark_button = Button(self.root, text="Add Watermark", command=self.add_watermark)
        self.watermark_button.pack()

        self.image_path = ""
        self.uploaded_image = None

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if self.image_path:
            self.uploaded_image = Image.open(self.image_path)
            self.uploaded_image.thumbnail((300, 300))
            self.uploaded_image_tk = ImageTk.PhotoImage(self.uploaded_image)
            self.canvas.create_image(150, 150, image=self.uploaded_image_tk)

    def add_watermark(self):
        if self.uploaded_image:
            watermark_text = "Your Watermark"
            watermark_image = Image.new("RGBA", self.uploaded_image.size)
            draw = ImageDraw.Draw(watermark_image)
            font = ImageFont.truetype("arial.ttf", 20)
            text_width, text_height = draw.textsize(watermark_text, font)
            x = self.uploaded_image.width - text_width - 10
            y = self.uploaded_image.height - text_height - 10
            draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

            final_image = Image.alpha_composite(self.uploaded_image, watermark_image)
            final_image.show()

if __name__ == "__main__":
    root = Tk()
    app = WatermarkApp(root)
    root.mainloop()
