# 🤖 Auto Replier

A basic Python automation project that automatically copies a message, processes it using an API, and sends a reply.

## 📖 About

**Auto Replier** is a simple Python-based automation project created to automate the process of replying to messages.

The project uses **PyAutoGUI** for mouse and keyboard automation and **Pyperclip** for copying and pasting text. Screen coordinates are used to interact with the messaging interface. The copied message is then processed using an API, and the reply is automatically pasted and sent.

This project is currently a **basic prototype** built to explore Python automation and API integration.

## ✨ Features

* 📋 Automatically copies the message
* 🖱️ Uses coordinates for screen interaction
* 🤖 Uses an API to process/generate the reply
* 📎 Uses clipboard for copying and pasting
* 💬 Automatically pastes the generated reply
* 📤 Automatically sends the reply

## 🛠️ Technologies Used

* **Python**
* **PyAutoGUI**
* **Pyperclip**
* **API**

## 🔄 How It Works

```text
Message
   ↓
Select Message
   ↓
Copy Message
   ↓
Read Copied Text
   ↓
Send Text to API
   ↓
Get Reply
   ↓
Copy Reply
   ↓
Paste Reply
   ↓
Send Reply
```

## 🚀 Installation

Make sure Python is installed on your system.

Install the required libraries:

```bash
pip install pyautogui pyperclip
```

Install any other library required by the API used in the project.

## ▶️ Run the Project

Run the Python file:

```bash
python main.py
```

Before running the script, open the messaging interface and make sure the required UI elements are in the expected positions.

## 🖱️ Coordinate-Based Automation

The current project uses screen coordinates to perform actions such as clicking, selecting, and typing.

For example:

```python
pyautogui.click(x, y)
```

The coordinates depend on the position of the elements on the screen, so they may need to be changed on a different device or screen resolution.

## ⚠️ Limitations

* The project currently uses fixed screen coordinates.
* It may not work correctly if the screen resolution or UI layout changes.
* The current version is a basic prototype.
* Message detection and error handling can be improved.

## 🔮 Future Improvements

* Dynamic UI element detection
* Better message detection
* More intelligent AI-generated replies
* Improved error handling
* More reliable automation
* Support for multiple messaging platforms
* Customizable reply behavior

## 📌 Project Status

**Basic Prototype 🚧**

The basic auto-reply workflow is implemented. More features and improvements can be added in future versions.

## 👩‍💻 Author

**Mayuri Nagale**
