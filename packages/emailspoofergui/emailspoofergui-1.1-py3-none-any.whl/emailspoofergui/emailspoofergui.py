import subprocess
import json
import tkinter as tk

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

    root = tk.Tk()
    root.title("Email Spoofer from AKM KORISHEE APURBO")
    root.geometry("800x500+500+0")

    # Read configuration from file
    try:
        with open('config.json') as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        print("Config file not found or invalid.")
        return

    label = tk.Label(root, text="KORISHEE THE CYBERMASTER", font=("Comic Sans MS", 18 , "bold"))
    label.grid(row=0, column=0, columnspan=2, pady=10)

    sender_label = tk.Label(root, text="Sender's Email:",fg="green")
    sender_label.grid(row=1, column=0, sticky="w")

    sender_entry = tk.Entry(root, width=70, font=("Arial", 12), fg="purple")
    sender_entry.grid(row=1, column=1, sticky="e")

    receiver_label = tk.Label(root, text="Recipient's Email:",fg="green")
    receiver_label.grid(row=2, column=0, sticky="w")

    receiver_entry = tk.Entry(root, width=70, font=("Arial", 12), fg="green")
    receiver_entry.grid(row=2, column=1, sticky="e")

    subject_label = tk.Label(root, text="Subject:",fg="green")
    subject_label.grid(row=3, column=0, sticky="w")

    subject_entry = tk.Entry(root, width=70, font=("Arial", 12), fg="red")
    subject_entry.grid(row=3, column=1, sticky="e")

    message_label = tk.Label(root, text="Message:",fg="green")
    message_label.grid(row=4, column=0, sticky="w")

    message_entry = tk.Text(root, width=70, height=12, wrap="word", font=("Arial", 12), fg="blue")
    message_entry.grid(row=4, column=1, sticky="e")

    send_button = tk.Button(root, fg="green", text="Send Email", command=send)
    send_button.grid(row=5, column=0, columnspan=2, pady=10)

    result_label = tk.Label(root, text="", font=("Arial", 12))
    result_label.grid(row=6, column=0, columnspan=2)

    root.mainloop()

send_email()
