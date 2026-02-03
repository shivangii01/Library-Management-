CREATE database library_db;
use library_db;

CREATE TABLE admin (
    admin_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50),
    password VARCHAR(50)
);
INSERT INTO admin (username, password)
VALUES ('aman sharma', '12345678');

select* from admin;

CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    author VARCHAR(100),
	quantity INT);
    INSERT INTO books (title, author, quantity) VALUES
('The Alchemist', 'Paulo Coelho', 10),
('Atomic Habits', 'James Clear', 15),
('Rich Dad Poor Dad', 'Robert Kiyosaki', 12),
('Think and Grow Rich', 'Napoleon Hill', 8),
('The Power of Habit', 'Charles Duhigg', 9),
('Ikigai', 'Hector Garcia', 14),
('Deep Work', 'Cal Newport', 7),
('The Monk Who Sold His Ferrari', 'Robin Sharma', 11),
('Harry Potter 1', 'J.K. Rowling', 20),
('Harry Potter 2', 'J.K. Rowling', 18),
('Harry Potter 3', 'J.K. Rowling', 17),
('Harry Potter 4', 'J.K. Rowling', 16),
('Harry Potter 5', 'J.K. Rowling', 15),
('Harry Potter 6', 'J.K. Rowling', 14),
('Harry Potter 7', 'J.K. Rowling', 13),
('The Hobbit', 'J.R.R. Tolkien', 10),
('The Lord of the Rings', 'J.R.R. Tolkien', 9),
('The Catcher in the Rye', 'J.D. Salinger', 6),
('To Kill a Mockingbird', 'Harper Lee', 8),
('1984', 'George Orwell', 12),
('Animal Farm', 'George Orwell', 14),
('The Great Gatsby', 'F. Scott Fitzgerald', 7),
('Moby Dick', 'Herman Melville', 5),
('Pride and Prejudice', 'Jane Austen', 9),
('The Kite Runner', 'Khaled Hosseini', 11),
('The Book Thief', 'Markus Zusak', 10),
('The Da Vinci Code', 'Dan Brown', 13),
('Angels and Demons', 'Dan Brown', 12),
('Inferno', 'Dan Brown', 11),
('Digital Fortress', 'Dan Brown', 8),
('The Shining', 'Stephen King', 7),
('It', 'Stephen King', 6),
('Doctor Sleep', 'Stephen King', 5),
('The Fault in Our Stars', 'John Green', 9),
('Looking for Alaska', 'John Green', 8),
('The Hunger Games', 'Suzanne Collins', 14),
('Catching Fire', 'Suzanne Collins', 13),
('Mockingjay', 'Suzanne Collins', 12),
('The Maze Runner', 'James Dashner', 10),
('Divergent', 'Veronica Roth', 11);
select * from books;
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    course VARCHAR(50),
    phone VARCHAR(15),	
    email VARCHAR(255) UNIQUE);
    INSERT INTO users (name, course, phone, email) VALUES
('Amit Sharma', 'BCA', '9876543210', 'amit.sharma@gmail.com'),
('Neha Verma', 'BBA', '9876543211', 'neha.verma@gmail.com'),
('Rahul Singh', 'BSc IT', '9876543212', 'rahul.singh@gmail.com'),
('Priya Gupta', 'BCA', '9876543213', 'priya.gupta@gmail.com'),
('Rohan Mehta', 'MBA', '9876543214', 'rohan.mehta@gmail.com'),
('Sneha Patel', 'BCom', '9876543215', 'sneha.patel@gmail.com'),
('Arjun Kumar', 'BTech', '9876543216', 'arjun.kumar@gmail.com'),
('Pooja Jain', 'BCA', '9876543217', 'pooja.jain@gmail.com'),
('Vikas Malhotra', 'MCA', '9876543218', 'vikas.m@gmail.com'),
('Anjali Roy', 'BSc CS', '9876543219', 'anjali.roy@gmail.com'),

('Karan Khanna', 'BBA', '9876543220', 'karan.khanna@gmail.com'),
('Simran Kaur', 'MBA', '9876543221', 'simran.kaur@gmail.com'),
('Mohit Aggarwal', 'BCom', '9876543222', 'mohit.ag@gmail.com'),
('Ritu Saxena', 'BCA', '9876543223', 'ritu.saxena@gmail.com'),
('Nikhil Joshi', 'BTech', '9876543224', 'nikhil.j@gmail.com'),
('Ayesha Khan', 'BSc IT', '9876543225', 'ayesha.khan@gmail.com'),
('Suresh Yadav', 'MCA', '9876543226', 'suresh.y@gmail.com'),
('Kavita Nair', 'MBA', '9876543227', 'kavita.nair@gmail.com'),
('Manish Pandey', 'BCom', '9876543228', 'manish.p@gmail.com'),
('Isha Kapoor', 'BBA', '9876543229', 'isha.k@gmail.com'),

('Deepak Choudhary', 'BCA', '9876543230', 'deepak.c@gmail.com'),
('Naina Arora', 'BSc CS', '9876543231', 'naina.a@gmail.com'),
('Sahil Bansal', 'BTech', '9876543232', 'sahil.b@gmail.com'),
('Meena Joshi', 'BCom', '9876543233', 'meena.j@gmail.com'),
('Abhishek Tiwari', 'MBA', '9876543234', 'abhishek.t@gmail.com'),
('Pallavi Deshmukh', 'MCA', '9876543235', 'pallavi.d@gmail.com'),
('Rakesh Mishra', 'BSc IT', '9876543236', 'rakesh.m@gmail.com'),
('Tanvi Kulkarni', 'BCA', '9876543237', 'tanvi.k@gmail.com'),
('Harsh Vardhan', 'BBA', '9876543238', 'harsh.v@gmail.com'),
('Sonia Sehgal', 'MBA', '9876543239', 'sonia.s@gmail.com'),

('Ajay Rana', 'BTech', '9876543240', 'ajay.r@gmail.com'),
('Preeti Lal', 'BCom', '9876543241', 'preeti.l@gmail.com'),
('Yash Oberoi', 'BCA', '9876543242', 'yash.o@gmail.com'),
('Komal Sethi', 'BSc CS', '9876543243', 'komal.s@gmail.com'),
('Naveen Pillai', 'MCA', '9876543244', 'naveen.p@gmail.com'),
('Shruti Goyal', 'MBA', '9876543245', 'shruti.g@gmail.com');

select * from users;
CREATE TABLE issued_books (
    issue_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    book_id INT,
    issue_date DATE,
    due_date date,
    return_date DATE,
    fine int default 0,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);
select * from issued_books;


