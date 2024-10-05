import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk # type: ignore

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("7SB_Equipo#3_Sarricolea_Cañas_Vazquez_Toache")
        self.master.configure(bg='light green')

        # Center the window
        self.center_window(1200, 800)

        # List of painters and images
        self.painting_buttons = ["Leonardo da Vinci", "Edvard Munch", "Johannes Vermeer"]
        self.images = ["images/gioconda.jpg", "images/the_scream.jpg", "images/the_girl_with_the_pearl.jpg"]
        self.create_widgets()

    def center_window(self, width, height):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.master.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        self.buttons_frame = tk.Frame(self.master, bg='light green')
        self.buttons_frame.pack(pady=20)

        # Create a button for each painter
        for index, painter in enumerate(self.painting_buttons):
            button = tk.Button(self.buttons_frame, text=painter, command=lambda i=index: self.show_painting(i))
            button.pack(pady=5)

        # Main button to close the window
        self.close_button = tk.Button(self.master, text="Cerrar ventana", command=self.confirm_close)
        self.close_button.pack(pady=10)

        # Label to show the painting
        self.image_label = tk.Label(self.master, bg='light green')
        self.image_label.pack(side='bottom', anchor='se')

    def show_painting(self, index):
        self.clear_image()  # Clear the current image
        try:
            self.img = Image.open(self.images[index])  # Open the image
            self.img = self.img.resize((300, 400), Image.LANCZOS)  # Change the size of the image
            self.img_tk = ImageTk.PhotoImage(self.img)
            self.image_label.configure(image=self.img_tk)
            self.image_label.image = self.img_tk

            # Buttoon to close the painting
            close_image_button = tk.Button(self.master, text="Cerrar pintura", command=self.clear_image)
            close_image_button.pack(pady=5)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir la imagen: {e}")

    def clear_image(self):
        # Clear the current image
        self.image_label.configure(image='')
        self.image_label.image = None
        # Destroy the button to close the painting
        for widget in self.master.pack_slaves():
            if isinstance(widget, tk.Button) and widget.cget("text") == "Cerrar pintura":
                widget.destroy()

    def confirm_close(self):
        if messagebox.askyesno("Confirmar", "¿Desea cerrar la ventana?"):
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
