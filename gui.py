import os
import numpy as np
import PIL
import matplotlib.pyplot as plt
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
from implementResults import main
from Color import main1



def load_image():
    # Open a file dialog to select an image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        print(f"Loaded image path: {file_path}")  # Debug print
        # Display the selected image in the GUI
        display_input_image(file_path)


def search_images():
    # Get the input image path
    input_image_path = input_image_label.cget("text")
    
    # Check if an image has been loaded
    if input_image_path:
        try:
            print(f"Input image path: {input_image_path}")
            # Pass the input image to the program and get similar images
            similar_images = main(input_image_path)
            print(f"Similar images: {similar_images}")
            
            # Display the similar images in the GUI
            display_results(similar_images)
        except Exception as e:
            print(f"Error in search_images: {e}")
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("No Image", "Please load an image first.")


def search_images2():
    # Get the input image path
    input_image_path = input_image_label.cget("text")
    
    # Check if an image has been loaded
    if input_image_path:
        # Pass the input image to the program and get similar images
        similar_images = main1(input_image_path)
        
        # Display the similar images in the GUI
        display_results_color(similar_images)

def display_results_color(results):
    for widget in results_frame.winfo_children():
        widget.destroy()
    
    row = 0
    column = 0
    for img_path in results:
        img = Image.open(img_path)
        img.thumbnail((200, 200))
        img = ImageTk.PhotoImage(img)
        label = ctk.CTkLabel(results_frame, image=img)
        label.image = img
        label.grid(row=row, column=column, padx=5, pady=5)
        column += 1
        if column >= 5:
            column = 0
            row += 1

    results_frame.update()  # Update the frame to adjust scrollbar




def display_input_image(image_path):
    # Display the selected image in the GUI
    img = Image.open(image_path)
    img.thumbnail((200, 200))
    img = ImageTk.PhotoImage(img)
    input_image_label.configure(text=image_path, image=img, compound='top')
    input_image_label.image = img
    print(f"Input image label text set to: {image_path}")  # Debug print


def display_results(results):
    for widget in results_frame.winfo_children():
        widget.destroy()
    
    row = 0
    column = 0
    for img_path, score in results:
        img = Image.open(img_path)
        img.thumbnail((200, 200))
        img = ImageTk.PhotoImage(img)
        label = ctk.CTkLabel(results_frame, text=f'Similarity: {score:.2f}', image=img, compound='top')
        label.image = img
        label.grid(row=row, column=column, padx=5, pady=5)
        column += 1
        if column >= 5:
            column = 0
            row += 1

    results_frame.update()  # Update the frame to adjust scrollbar

def show_intro_window(window=None):
    if window:
        window.destroy()  # Destroy the existing window if it exists

    intro_window = ctk.CTk()
    intro_window.geometry("800x600")
    intro_window.configure(bg="red")  # Set background color to black
    ctk.set_appearance_mode("dark")
    intro_window.title("Search Engine")

    txt = "Welcome to Ali's Search Engine..."
    global count,text
    count = 0
    text = ''
    label = ctk.CTkLabel(intro_window,
                         text=text,  # Initially empty
                         font=('Orbitron', 45, 'bold'),
                         text_color="#6F0761"
                        )
    label.pack(pady=100)

    def slider():
        global count, text
        if count >= len(txt):
            count = -1
            text = ''
        else:
            text = text + txt[count]
        label.configure(text=text)
        count += 1
        intro_window.after(100, slider)  # Call slider function again after 100 milliseconds

    slider()  # Call slider function once to start the animation

    button_intro = ctk.CTkButton(intro_window, text="Image Search",  hover_color="#6F0761", font=("Arial", 14), command=lambda: update_intro(intro_window))
    button_intro.pack(pady=10)

    button_another = ctk.CTkButton(intro_window, text="Image Search By Color",  hover_color="#6F0761", font=("Arial", 14), command=lambda: show_another_window(intro_window))
    button_another.pack(pady=10)

    intro_window.mainloop()


def update_intro(window):
    window.title("Image Search")  # Update window title
    for widget in window.winfo_children():  # Hide all widgets in the intro window
        widget.pack_forget()

    # Create a frame for the main content
    main_frame = ctk.CTkFrame(window)
    main_frame.place(relwidth=1, relheight=1)

    # Add content for the main window
    # Create the Load Image button
    load_image_button = ctk.CTkButton(master=main_frame, text="Load Image", corner_radius=32, hover_color="#6F0761", command=load_image)
    load_image_button.place(relx=0.05, rely=0.05, relwidth=0.2)

    # Create the Search button
    search_button = ctk.CTkButton(master=main_frame, text="Search", corner_radius=32, hover_color="#6F0761", command=search_images)
    search_button.place(relx=0.05, rely=0.15, relwidth=0.2)

    # Create a label to display the input image path
    global input_image_label
    input_image_label = ctk.CTkLabel(master=main_frame)
    input_image_label.place(relx=0.05, rely=0.25, relwidth=0.2)

    # Create a frame to display the results
    global results_frame
    results_frame = ctk.CTkScrollableFrame(main_frame, width=1100, height=700)  # Adjust the height as needed
    results_frame.place(relx=0.3, rely=0.05, relwidth=0.55, relheight=0.9)

    window.mainloop()

def show_another_window(window):
    window.title("Image Search By Color")  # Update window title
    for widget in window.winfo_children():  # Hide all widgets in the intro window
        widget.pack_forget()

    # Create a frame for the main content
    main_frame = ctk.CTkFrame(window)
    main_frame.pack(fill="both", expand=True)

    # Add content for the main window
    # Create the Load Image button
    load_image_button = ctk.CTkButton(master=main_frame, text="Load Image", corner_radius=32, hover_color="#6F0761", command=load_image)
    load_image_button.pack(pady=10)

    # Create the Search button
    search_button = ctk.CTkButton(master=main_frame, text="Search", corner_radius=32, hover_color="#6F0761", command=search_images2)
    search_button.pack(pady=10)

    # Create a label to display the input image path
    global input_image_label
    input_image_label = ctk.CTkLabel(master=main_frame)
    input_image_label.pack(pady=10)

    # Create a frame to display the results
    global results_frame
    results_frame = ctk.CTkScrollableFrame(main_frame, width=1100, height=700)  # Adjust the height as needed
    results_frame.pack(pady=10)  # Adjust the pady value to add space between widgets

    # Create a back button
    #back_button = ctk.CTkButton(master=main_frame, text="Back", corner_radius=32, hover_color="#6F0761", command=lambda: back_to_intro(main_frame, window))
    #back_button.pack(pady=10)

def back_to_intro(main_frame, window):
    main_frame.pack_forget()  # Hide the current frame
    show_intro_window()  # Display the intro page again


show_intro_window()

