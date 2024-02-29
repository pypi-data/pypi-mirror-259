# emailspoofergui

emailspoofergui is a Python package that allows you to easily spoof emails using a graphical user interface (GUI) or a command-line interface (CLI).
It provides a simple and intuitive way to send spoofed emails with custom sender addresses, recipients, subject, and content.

## Installation

You can install EmailSpooferGUI via pip:


pip install emailspoofergui


## Usage

### Graphical User Interface (GUI)

After installing EmailSpooferGUI, you can launch the graphical user interface by running the following command:


emailspoofergui


The GUI will prompt you to enter your email username, password, and SMTP server address. Once you provide this information, you can start spoofing emails by entering the sender address, recipient(s), subject, and content in the respective fields and clicking the "Send" button.

### Command-Line Interface (CLI)

Alternatively, you can use the command-line interface (CLI) to send spoofed emails. You can simply type the following command in the terminal:

emailspoofercli


This will automatically prompt you to enter your email username, password, SMTP server address, sender address, recipient(s), subject, and message. After providing this information, the email will be sent.

## Configuration

EmailSpooferGUI saves your email configuration (username, password, SMTP server address) in a `config.json` file located in the package directory. You can also manually edit this file if needed.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue on the [GitHub repository](https://github.com/IMApurbo/emailspoofergui).
Pull requests are also appreciated.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
