## 🔐 Password Manager (Tkinter GUI)
A simple yet powerful **Password Manager** built with **Python** and **Tkinter**. This app allows you to securely generate, save, and search for passwords, while storing them in a local `data.json` file. It also supports one-click password copying to the clipboard using `pyperclip`.

---

## 📌 Features

- 🔒 Save login credentials securely in a local JSON file  
- 🔍 Search for saved credentials by website  
- 🔐 Generate strong, random passwords  
- 📋 Automatically copy generated passwords to clipboard  
- ❌ Error handling for empty fields or missing files  
- 🧠 Remembers last used email/username  
- 🎨 Intuitive and simple GUI with branding logo

  ## 🧠 How It Works

1. **Enter website, email/username, and password**  
2. **Click "Add"** to save credentials to `data.json`  
3. Use **"Generate Password"** to create a random secure password  
4. Use the **"Search"** button to retrieve stored credentials for any website  

> The passwords are stored in a nested JSON format, like this:
```json
{
  "Github.com": {
    "email": "user@example.com",
    "password": "securePass123!"
  }
}
```

## 🚀 Getting Started

Requirements

- Python 3.x

Required libraries:

- tkinter (built-in)
- random (built-in)
- json (built-in)
- pyperclip (external)

## Setup
1.  Clone the repository:
   
   ```bash
   git clone https://github.com/your-username/password-manager.git
   cd password-manager
   ```
2.  Install the required library:
   
   ```bash
 pip install pyperclip
   ```

3.  Make sure logo.png is in the same directory.

4.  Run the App:
   ```bash
   python main.py
  ```

## 📁 Project Structure
 ```bash
password-manager/
│
├── main.py             # Main Python script
├── data.json           # Created automatically to store credentials
├── logo.png            # App logo used in the GUI
└── README.md           # This documentation file
```

## 🖼️ Interface Overview

- 📝 Website Entry — name of the platform
- 📧 Email/Username Entry — used for login
- 🔑 Password Entry — typed or generated password
- ⚙️ Generate Password — creates a strong random password
- 💾 Add Button — saves entered data
- 🔎 Search Button — finds credentials by website

## 📃 Code Highlights

```bash

🔐 generate()

# Generates a strong password with:
# - 8–10 letters
# - 2–4 symbols
# - 2–4 numbers

# Copies it to clipboard and inserts into the password field.
```

```bash
💾 save()

# Validates input and:
# Reads existing data from data.json
# Updates or creates new records
# Handles missing file gracefully
```

```bash
🔍 search()

#Searches for website name in data.json and:
#Displays email and password in a message box
#Alerts if not found or file is missing
```
## 🎨 Design Constants

| Component   | Description                  |
| ----------- | ---------------------------- |
| `logo.png`  | Used as app logo in the GUI  |
| `pyperclip` | Copies password to clipboard |
| `data.json` | Stores all user credentials  |

## 🛠️ Ideas for Future Enhancements

- Encrypt the JSON file for more security 🔐
- Add master password authentication 🔓
- Export/Import functionality 📁
- Add light/dark mode toggle 🌗

## 📄 License
- This project is open-source and available under the MIT License.

## 🙌 Acknowledgments
- Password generation logic inspired by Python random module docs
- Built using Python and Tkinter



