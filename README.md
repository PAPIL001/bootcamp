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