Project Management System made with django
Includes:
    -Student CRUD
    -Staff CRUD
    -Creating and assigning of projects
    -Grading of projects
    -Managing finances

LOGIN:
    username: admin
    password: admin123

USAGE:
    Install in a Virtual Environment. Once you have set up a VE, clone this project.
    ```bash
    git clone https://github.com/kauskz1/Project-Management-System
    ```

    Run
    ```python
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    ```
    Then go to http://172.0.0.1:8000 on your browser.