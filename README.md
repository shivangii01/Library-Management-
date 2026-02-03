# 📚 Library Management System  
### 🐍 Python + 🗄️ MySQL (CLI Based)

---

## 🧾 About the Project

The **Library Management System** is a **Python-based command-line application** integrated with a **MySQL database**, built to efficiently manage core library operations.

This system emphasizes **administrative control**, **user management**, **book tracking**, and **automated fine calculation using dates**, ensuring smooth and reliable day-to-day library management.

It is ideal for **academic projects**, **Python–SQL practice**, and understanding **real-world CRUD operations**.

---

## ✨ Key Features

### 🔐 Admin Authentication
- Secure login system for librarians/admins  
- Prevents unauthorized access  

### 📘 Book Management (CRUD)
- ➕ Add new books  
- 👀 View all books  
- ✏️ Update book quantity  
- ❌ Delete books  
- 📄 Automatically exports book data to `book_list.txt`

### 👤 Member Management
- ➕ Add library members  
- 👀 View all members  
- ✏️ Update member details  
- ❌ Delete members  
- 📄 Member list exported to `members_list.txt`

### 🔄 Issue & Return System
- Issue books to registered users  
- Automatically stores issue date  
- Updates book quantity dynamically  
- Validates issued books before return  

### 💰 Fine Management
- ⏳ 7-day borrowing period  
- 💸 ₹10 per day fine after due date  
- Fine calculated automatically using `datetime`

---

## 🛠️ Tech Stack

| Technology | Usage |
|---------|------|
| 🐍 Python | Core logic |
| 🗃️ MySQL | Database |
| 🔌 mysql-connector-python | DB connectivity |
| ⏰ datetime | Date & fine calculation |
| 📄 Text Files | Exporting records |

---

## 📂 Project Structure
