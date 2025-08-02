 🔐 Python Port Scanner

A simple but effective **multithreaded port scanner** built using Python. It allows you to scan a range of ports on any target IP address and performs **basic banner grabbing** for identified open ports.

---

## 📌 Features

- ✅ Scan a single IP address
- ✅ Specify port range (start and end)
- ✅ Multithreading for faster scanning
- ✅ Banner grabbing (e.g., for HTTP, FTP, SSH, etc.)
- ✅ Smart HTTP banner handling (sends `GET` request to port 80/8080)

---

## 🧰 Tools & Technologies Used

- `Python 3`
- `socket` (for connecting to ports)
- `threading` (for concurrent scans)

---

## 🧱 Folder Structure

port-scanner/
├── scanner.py # 🔧 Main scanner script
├── requirements.txt # 📦 Dependency list (empty for now)
├── README.md # 📘 Project documentation
└── screenshots/ # 📸 Optional folder for demo images

yaml
Copy code

---

## 🚀 How to Run This Project

### 1. ✅ Prerequisites

Make sure you have Python 3 installed.

To check:
```bash
python3 --version
2. 🛠 Create Project Folder
bash
Copy code
mkdir port-scanner
cd port-scanner
touch scanner.py requirements.txt README.md
mkdir screenshots
Paste the scanner code inside scanner.py.

3. ▶️ Run the Scanner
bash
Copy code
python3 scanner.py
4. 📥 Input Parameters
When prompted:

Enter the target IP address (e.g., scanme.nmap.org or 192.168.1.1)

Enter start port (e.g., 20)

Enter end port (e.g., 100)

📸 Sample Output
bash
Copy code
Scanning scanme.nmap.org from port 20 to 100...

[+] Port 22 is open - SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
[+] Port 80 is open - HTTP/1.1 400 Bad Request
Date: Sat, 02 Aug 2025 05:47:04 GMT
Server: Apache/2.4.7 (Ubuntu)
🧪 Example Targets
For testing safely:

scanme.nmap.org (by Nmap project)

Your local network IP (192.168.x.x)

⚠️ Disclaimer
This tool is for educational purposes only.
Do not scan IPs that you do not own or do not have permission to test.
Unauthorized port scanning may violate terms of service or laws in your country.

🙌 Contributing
Feel free to fork the project, submit pull requests, or add features like:

Logging output to a file

Colored terminal results

GUI interface using Tkinter
