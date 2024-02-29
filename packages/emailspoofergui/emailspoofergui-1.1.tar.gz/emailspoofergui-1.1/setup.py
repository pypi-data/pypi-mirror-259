from setuptools import setup, find_packages
import json

def prompt_user():
    username = input("Enter your email username: ")
    password = input("Enter your email password: ")
    smtp_server = input("Enter your SMTP server address (e.g., smtp.example.com:587): ")
    return {"username": username, "password": password, "smtp_server": smtp_server}

def write_config(config):
    with open('emailspoofergui/config.json', 'w') as f:
        json.dump(config, f)

# Prompt user for information during installation
config = prompt_user()
write_config(config)

setup(
    name='emailspoofergui',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'emailspoofer = emailspoofergui.emailspoofergui:main',  # GUI entry point
            'emailspoofercli = emailspoofergui.emailspoofercli:main',  # CLI entry point
        ],
    },
    author='AKM Korishee Apurbo',
    author_email='bandinvisible8@gmail.com',
    description='A graphical email spoofing tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/IMApurbo/emailspoofergui',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
