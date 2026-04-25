# MyBlog

A personal blog web application built with Python and Django as a portfolio project to demonstrate backend web development skills.

## Live Demo
- https://gongzuodk.pythonanywhere.com/ 

## Screenshots  
- Website on PC:  
<img width="952" height="908" alt="Screenshot 2026-04-25 161743" src="https://github.com/user-attachments/assets/1b565d85-3178-4272-9633-bf6b2c28e081" />  
  
- Website on a Phone:  
<img width="1080" height="2124" alt="67658_5188030074314686720_n" src="https://github.com/user-attachments/assets/368a3347-5f38-47d4-9825-e68a647bce43" />


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
- Python 3.13
- Django 6.0
- SQLite
- HTML/CSS
- Simple.css
- Whitenoise (static files in production)
- python-decouple (environment variables)

## Getting Started

### Prerequisites
- Python 3.13 installed
- pip installed

### Installation

1. Clone the repository:  
git clone https://github.com/Gongzuo-Dk/myblog-test_project.git cd myblog-test_project

2. Create and activate a virtual environment:  
python -m venv .env  
.env\Scripts\activate        # Windows  
source .env/bin/activate     # Mac/Linux

3. Install dependencies:  
pip install -r requirements.txt

4. Create settings.ini in the project root  
In it goes:  
[settings]  
SECRET_KEY=your secret key  
DEBUG=True  
ALLOWED_HOSTS=your allowed host

5. Run migrations:  
python manage.py migrate

6. Create admin superuser:  
python manage.py createsuperuser

7. Start development server:  
python manage.py runserver

## Deployment
Deployed on PythonAnywhere at:
https://gongzuodk.pythonanywhere.com/

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
Daniel K  
GitHub: https://github.com/Gongzuo-Dk  
LinkedIn: https://www.linkedin.com/in/danylo-kulynych/
