import subprocess
import json
import pkg_resources
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os

def send_email():
    # Function to send the email
    def send():
        sender_name = sender_entry.get()
        receiver_email = receiver_entry.get()
        subject = subject_entry.get()
        message = message_entry.get("1.0", "end-1c")

        sendemail_command = f"sendemail -xu {config['username']} -xp {config['password']} -s {config['smtp_server']} -f '{sender_name}' -t {receiver_email} -u '{subject}' -m '{message}'"

        try:
            subprocess.run(sendemail_command, shell=True, check=True)
            result_label.config(text="Email sent successfully!", fg="green")
        except subprocess.CalledProcessError as e:
            result_label.config(text=f"Error: {e}", fg="red")

    # Function to open config file in editor
    def open_config_file():
        config_path = get_config_path()
        os.startfile(config_path)  # Open with default program

    # Function to open dialog box to edit config
    def edit_config():
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Configuration")

        # Read configuration from file
        config = load_config()

        # Create text box to display converted text
        text_box = tk.Text(edit_window, wrap="word", height=20, width=50, fg="green")
        text_box.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        text_box.insert(tk.END, json.dumps(config, indent=4))  # Insert JSON content into text box

        # Save button to overwrite config file
        def save_config():
            new_config = json.loads(text_box.get("1.0", "end-1c"))  # Get JSON content from text box
            config_path = get_config_path()
            with open(config_path, "w") as config_file:
                json.dump(new_config, config_file, indent=4)
            messagebox.showinfo("Success", "Configuration saved successfully.")
            edit_window.destroy()
            # Reload the JSON configuration
            global config
            config = load_config()

        save_button = tk.Button(edit_window, text="Save", command=save_config)
        save_button.grid(row=1, column=0, pady=10)

    root = tk.Tk()
    root.title("Email Spoofer from AKM KORISHEE APURBO")
    root.geometry("800x500+500+0")

    # Read configuration from file
    global config
    config = load_config()

    if config:
        label = tk.Label(root, text="KORISHEE THE CYBERMASTER", font=("Comic Sans MS", 18 , "bold"))
        label.grid(row=0, column=0, columnspan=2, pady=10)

        sender_label = tk.Label(root, text="Sender's Email:", fg="green")
        sender_label.grid(row=1, column=0, sticky="w")

        sender_entry = tk.Entry(root, width=70, font=("Arial", 12), fg="purple")
        sender_entry.grid(row=1, column=1, sticky="e")

        receiver_label = tk.Label(root, text="Recipient's Email:", fg="green")
        receiver_label.grid(row=2, column=0, sticky="w")

        receiver_entry = tk.Entry(root, width=70, font=("Arial", 12), fg="green")
        receiver_entry.grid(row=2, column=1, sticky="e")

        subject_label = tk.Label(root, text="Subject:", fg="green")
        subject_label.grid(row=3, column=0, sticky="w")

        subject_entry = tk.Entry(root, width=70, font=("Arial", 12), fg="red")
        subject_entry.grid(row=3, column=1, sticky="e")

        message_label = tk.Label(root, text="Message:", fg="green")
        message_label.grid(row=4, column=0, sticky="w")

        message_entry = tk.Text(root, width=70, height=12, wrap="word", font=("Arial", 12), fg="blue")
        message_entry.grid(row=4, column=1, sticky="e")

        send_button = tk.Button(root, fg="green", text="Send Email", command=send)
        send_button.grid(row=5, column=0, columnspan=2, pady=10)

        result_label = tk.Label(root, text="", font=("Arial", 12))
        result_label.grid(row=6, column=0, columnspan=2)

        # Button to edit config
        edit_config_button = tk.Button(root, text="->", command=edit_config)
        edit_config_button.grid(row=7, column=0, columnspan=2, pady=10, sticky="se")

        root.mainloop()
    else:
        print("Failed to load configuration.")

def load_config():
    try:
        # Load the config.json file from the package data
        config_path = get_config_path()
        with open(config_path) as config_file:
            config = json.load(config_file)
        return config
    except FileNotFoundError:
        print("Config file not found or invalid.")
        return None

def get_config_path():
    # Get the directory of the package data
    data_dir = pkg_resources.resource_filename("emailspoofergui", "data")
    # Construct the path to the config.json file
    config_path = os.path.join(data_dir, "config.json")
    return config_path

if __name__ == "__main__":
    send_email()
