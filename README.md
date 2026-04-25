# MyBlog

A personal blog web application built with Python and Django as a portfolio project to demonstrate backend web development skills.

## Live Demo
- https://gongzuodk.pythonanywhere.com/ 

## Screenshots
**

## Features
- Dynamic blog posts with images, themes and dates
- Pinned posts section on homepage
- Recent posts grid
- Theme/category filtering
- Full text search with input validation
- Pagination on all posts feed
- Admin panel for full content management
- Responsive custom navbar
- Default image fallback for posts without images

## Technologies Used
- Python 3
- Django
- SQLite
- HTML/CSS
- Simple.css

## Getting Started

### Prerequisites
- Python 3 installed
- pip installed

### Installation

1. Clone the repository:  
git clone https://github.com/Gongzuo-Dk/myblog-test_project.git cd myblog-test_project

2. Create and activate virtual environment:  
python -m venv .env  
.env\Scripts\activate        # Windows  
source .env/bin/activate     # Mac/Linux

3. Install dependencies:  
pip install -r requirements.txt

4. Run migrations:  
python manage.py migrate

5. Create admin superuser:  
python manage.py createsuperuser

6. Start development server:  
python manage.py runserver

7. Visit http://127.0.0.1:8000 :

## Project Structure
myblog/          → Django project settings and main URLs  
blog/            → Main application  
models.py      → Post and Theme models  
views.py       → All page views  
urls.py        → URL routing  
admin.py       → Admin configuration  
templates/       → HTML templates  
static/          → CSS and static images

## Author
Daniel  
GitHub: https://github.com/Gongzuo-Dk  
LinkedIn: https://www.linkedin.com/in/danylo-kulynych/