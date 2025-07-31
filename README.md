# Book Review Web App
This web application was developed as part of the **Digital Skills Lab course at LUISS Guido Carli University**. It is a fully functional Django-based platform that allows users to browse books, view details, and read user-submitted reviews — designed to simulate a real-world data-driven web product.


## Objectives
- Practice full-stack web development using Django
- Implement CRUD functionality and manage dynamic content
- Structure a scalable backend using Django models, views, and templates
- Integrate user-generated media and apply frontend styling
- Demonstrate deployment-ready design principles and clean code organization


## Tech Stack
- Language: Python 3.13          
- Framework: Django    
- Database: SQLite3              
- Frontend: HTML, CSS 


## Features
- **Book Listings** – View book titles, authors, genres, and cover images  
- **Review Pages** – Each book has a detailed view with user-submitted reviews  
- **Media Uploads** – Upload and display book covers using Django’s media handling  
- **Dynamic Templates** – Templates render data using Django’s context system  
- **Clean Routing** – URLs and views are structured using Django best practices  
- **Local Deployment** – Runs seamlessly with SQLite and Django’s built-in dev server  


## Screenshots
| Book List Page | Book Detail | Reviews |
|----------------|-------------|---------|
| <img width="1710" height="1112" alt="Screenshot 2025-07-31 at 09 52 34" src="https://github.com/user-attachments/assets/a5b0f3ff-1c26-4576-babe-a21c78967c66" /> | <img width="1710" height="1112" alt="Screenshot 2025-07-31 at 09 52 46" src="https://github.com/user-attachments/assets/0fa81016-4947-476b-bfe5-711104501938" /> | <img width="1710" height="1112" alt="Screenshot 2025-07-31 at 09 53 00" src="https://github.com/user-attachments/assets/3f6cdf42-b9ba-4a68-8daa-e74b5e6e7342" /> |


## Getting Started
### Clone and Run Locally:
```bash
git clone https://github.com/berencay/book-review-app.git
cd book-review-app
pip install -r requirements.txt  # (if you added one)
python manage.py runserver
