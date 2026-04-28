# Belu-AI
This is an AI app
# Belu-AI Setup Guide

This guide will help you set up and run **Belu-AI** on Windows, Linux, and macOS.

---

## 📦 1. Clone the Repository

Open your terminal (or Command Prompt/PowerShell on Windows) and run:

```bash
git clone https://github.com/marcosswan-bit/Belu-AI.git
cd Belu-AI
```

---

## 🧰 2. Install Dependencies

Make sure you have **Python 3.9+** installed.

Then install required packages:

```bash
pip install -r requirements.txt
```

---

## 🔑 3. Set Up Your OpenAI API Key

Copy the example environment file:

### On macOS/Linux:

```bash
cp .env.example .env
```

### On Windows (Command Prompt):

```cmd
copy .env.example .env
```

### On Windows (PowerShell):

```powershell
cp .env.example .env
```

Now open the `.env` file in a text editor and add your API key:

```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

---

## 🚀 4. Run the App

Start the application:

```bash
python main.py
```

---

## 🔐 How to Get an OpenAI API Key

1. Go to: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Click **Create new secret key**
4. Copy the key
5. Paste it into your `.env` file

---

## 🖥️ OS-Specific Notes

### 🪟 Windows

* Use **Command Prompt** or **PowerShell**
* Make sure Python is added to PATH
* If `pip` doesn't work, try:

  ```cmd
  python -m pip install -r requirements.txt
  ```

### 🐧 Linux

* You may need to install Python and pip:

  ```bash
  sudo apt update
  sudo apt install python3 python3-pip
  ```
* Then run:

  ```bash
  pip3 install -r requirements.txt
  ```

### 🍎 macOS

* Install Python via Homebrew (if not installed):

  ```bash
  brew install python
  ```
* Then:

  ```bash
  pip3 install -r requirements.txt
  ```

---

## ✅ You're Ready!

Your Belu-AI app should now be running locally 🎉

If something breaks, check:

* Python version (`python --version`)
* Whether your API key is correct
* That all dependencies installed successfully

---

## 💡 Optional Tips

* Use a virtual environment:

  ```bash
  python -m venv venv
  source venv/bin/activate  # macOS/Linux
  venv\Scripts\activate     # Windows
  ```

* Upgrade pip if needed:

  ```bash
  python -m pip install --upgrade pip
  ```

---

Happy coding 🚀


