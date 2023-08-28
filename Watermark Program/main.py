import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Image Watermark App")

        self.image_path = None
        self.watermark_text = "Your Watermark"
        self.watermark_opacity = 0.5

        self.canvas = tk.Canvas(root)
        self.canvas.pack()

        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.watermark_entry = tk.Entry(root)
        self.watermark_entry.pack()

        self.apply_button = tk.Button(root, text="Apply Watermark", command=self.apply_watermark)
        self.apply_button.pack()

        self.save_button = tk.Button(root, text="Save Watermarked Image", command=self.save_watermarked_image)
        self.save_button.pack()

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png")])
        if self.image_path:
            self.display_image()

    def display_image(self):
        img = Image.open(self.image_path)
        # Resize for display
        img.thumbnail((400, 400))
        self.tk_image = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def apply_watermark(self):
        if self.image_path:
            img = Image.open(self.image_path)
            draw = ImageDraw.Draw(img)

            width, height = img.size
            font_size = int(min(width, height) / 20)
            font = ImageFont.truetype("arial.ttf", font_size)

            # Update watermark text
            self.watermark_text = self.watermark_entry.get()

            text_size = font.getlength(self.watermark_text)
            x = width - text_size - 10
            # Adjust y position based on font size
            y = height - font_size - 10

            text_color = (255, 255, 255, int(255 * self.watermark_opacity))
            draw.text((x, y), self.watermark_text, font=font, fill=text_color)

            self.tk_image = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def save_watermarked_image(self):
        if self.image_path:
            img = Image.open(self.image_path)
            draw = ImageDraw.Draw(img)

            width, height = img.size
            font_size = int(min(width, height) / 20)
            font = ImageFont.truetype("arial.ttf", font_size)

            # Update watermark text
            self.watermark_text = self.watermark_entry.get()

            # Use getlength since getsize and gettext is deprecaeted
            text_size = font.getlength(self.watermark_text)
            x = width - text_size - 10
            # Adjust y position based on font size
            y = height - font_size - 10

            text_color = (255, 255, 255, int(255 * self.watermark_opacity))
            draw.text((x, y), self.watermark_text, font=font, fill=text_color)

            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                img.save(save_path)
                messagebox.showinfo("Watermark App", "Your Image is saved successfully with watermark!")

def main():
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
