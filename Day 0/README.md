# Simple Web Server Setup

This demonstrates a simple web server running on an Azure Virtual Machine, displaying my name and photo.

## Setup Instructions

1.  **Created `index.html`:** A basic HTML file was created with the following content using VS Code on the remote VM:
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Webpage</title>
    </head>
    <body>
        <h1>Hello, my name is Papil</h1>
        <img src="photo1.jpg" alt="My Photo" width="200">
    </body>
    </html>
    ```

2.  **Transferred Photo:** The `photo1.jpg` file was transferred to the remote VM using the drag-and-drop functionality within the VS Code Explorer.

3.  **Started Web Server:** The built-in `http.server` module in Python 3 was used via the VS Code Integrated Terminal with the command:
    ```bash
    sudo python3 -m http.server 80
    ```

4.  **Accessed via Public IP:** The webpage was accessed using the public IP address of the Azure Virtual Machine in a web browser.

5. ## Command-Line Application Demonstration

You can see a recording of the command-line actions, including starting and stopping the simple web server, here:

[Asciinema Recording](  https://asciinema.org/connect/5a0d2475-c7f1-4f1b-9193-7cc816caa932 )

# Docker Setup

## Installation

To install Docker, we followed these steps:

1.  Updated the package index:
    ```bash
    sudo apt update
    ```
2.  Installed the necessary packages:
    ```bash
    sudo apt install apt-transport-https ca-certificates curl gnupg lsb-release
    ```
3.  Added Docker's official GPG key:
    ```bash
    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL [https://download.docker.com/linux/ubuntu/gpg](https://download.docker.com/linux/ubuntu/gpg) | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    ```
4.  Added the Docker repository to APT sources:
    ```bash
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] [https://download.docker.com/linux/ubuntu](https://download.docker.com/linux/ubuntu) $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ```
5.  Updated the package index again:
    ```bash
    sudo apt update
    ```
6.  Installed Docker Engine:
    ```bash
    sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin
    ```
7.  Verified the installation:
    ```bash
    sudo docker run hello-world
    ```

## Pulling and Running a Python Image

1.  Pulled the Python image:
    ```bash
    docker pull python:latest
    ```
2.  Created a `hello.py` file:
    ```python
    print("Hello, World! from Docker Python")
    ```
3.  Ran the Python script in a Docker container:
    ```bash
    docker run --rm -v "$(pwd)":/app -w /app python python3 /app/hello.py
    ```

# Python Environment Setup

## Installing Python 3.11 and 3.13

1.  Installed Python 3.11:
    ```bash
    sudo apt update
    sudo apt install python3.11
    ```
    Verification:
    ```bash
    python3.11 --version
    ```
2.  Installed Python 3.13 (built from source):
    ```bash
    sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev
    wget [https://www.python.org/ftp/python/3.13.0/Python-3.13.0.tgz](https://www.python.org/ftp/python/3.13.0/Python-3.13.0.tgz) # Replace with actual version if different
    tar xzf Python-3.13.0.tgz
    cd Python-3.13.0
    ./configure --enable-optimizations
    make -j $(nproc)
    sudo make altinstall
    python3.13 --version
    ```

## Creating and Using a Virtual Environment

1.  Created a virtual environment:
    ```bash
    python3.13 -m venv bootcamp #or venv_test
    ```
2.  Activated the virtual environment:
    ```bash
    source bootcamp/bin/activate #or venv_test/bin/activate
    ```
3.  Verified the Python version within the environment:
    ```bash
    python --version
    ```
4.  Deactivated the virtual environment:
    ```bash
    deactivate
    ```

# SSH Key Setup

## Generating SSH Keys

1.  Generated the SSH key pair:
    ```bash
    ssh-keygen -t rsa -b 2048
    ```

## Adding the Public Key to the Server

1.  Ensured the `~/.ssh` directory exists and has the correct permissions:
    ```bash
    mkdir -p ~/.ssh
    chmod 700 ~/.ssh
    ```
2.  Appended the public key to the `authorized_keys` file:
    ```bash
    echo "$(cat ~/.ssh/id_rsa.pub)" >> ~/.ssh/authorized_keys
    chmod 600 ~/.ssh/authorized_keys
    ```

## Testing SSH Login

    ```bash
    ssh azureuser@your_server_ip_address
    ```

# Rsync Usage
## Copying files
1.  Copy from local to server
    ```bash
    rsync -avz /path/to/local/file.txt azureuser@your_server_ip_address:/path/on/server/
    ```
2. Copy from server to local
    ```bash
    rsync -avz azureuser@your_server_ip_address:/path/on/server/file.txt /path/to/local/
    ```


# Setting Up Passwordless SSH and Using rsync

This document outlines the steps taken to set up passwordless SSH access for GitHub and a local server (in this case, the same machine), and how to use `rsync` for file transfers.

## Step 1: Generate SSH Keys

We used the `ssh-keygen` command to generate a new EdDSA SSH key pair.

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
Replace "your_email@example.com" with your actual email address.
The private key was saved to /home/azureuser/.ssh/id_ed25519.
The public key was saved to /home/azureuser/.ssh/id_ed25519.pub.
A passphrase was set for the private key for added security.
Step 2: Add the Public Key to GitHub
The content of the public key file (/home/azureuser/.ssh/id_ed25519.pub) was copied.
The public key was added to the SSH keys section of the GitHub account settings.
Step 3: Add the Public Key to the Server (Local Machine)
Ensured the .ssh directory exists and has the correct permissions:
Bash

mkdir -p ~/.ssh
chmod 700 ~/.ssh
Appended the public key to the authorized_keys file:
Bash

cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
Set the correct permissions for the authorized_keys file:
Bash

chmod 600 ~/.ssh/authorized_keys
Step 4: Test SSH Connection to GitHub
The following command was used to test the connection to GitHub:

Bash

ssh -T git@github.com
This confirmed that the SSH key was correctly configured for GitHub, and we received a message:

Hi PAPIL001! You've successfully authenticated, but GitHub does not provide shell access.
Step 5: Test SSH Connection to the Server (Local Machine)
Initially, the command ssh azureuser@localhost prompted for the passphrase of a potentially existing id_rsa key.

To explicitly use the newly generated key, the following command was used:

Bash

ssh -i ~/.ssh/id_ed25519 azureuser@localhost
This successfully logged into the local machine after entering the passphrase for the id_ed25519 key.

Step 6: Using SSH Agent for Convenience (Recommended)
To avoid entering the passphrase repeatedly, the SSH agent was used:

Start the SSH Agent:
Bash

eval "$(ssh-agent -s)"
Add the private key to the agent (you'll be prompted for the passphrase):
Bash

ssh-add ~/.ssh/id_ed25519
After adding the key to the agent, subsequent ssh azureuser@localhost commands should not require a passphrase during the current session.
Step 7: Using rsync for File Transfers
rsync is a command-line tool for synchronizing files and directories efficiently. Here are some example uses:

Copying files from your local machine to the server:
Bash

rsync -avz /path/to/local/files azureuser@localhost:/path/to/remote/directory
Copying files from the server to your local machine:
Bash

rsync -avz azureuser@localhost:/path/to/remote/files /path/to/local/directory
Synchronizing directories (keeping them identical):
Bash

rsync -avz --delete /path/to/local/directory/ azureuser@localhost:/path/to/remote/direc
