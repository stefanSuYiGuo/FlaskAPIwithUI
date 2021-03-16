# FlaskAPIwithUI
This is a project for practice, which includes the display of usage of Flask API with combination of UI design.


## Notes
> Front-end Notes
1. For front-end, `{% %}`, `extends`, `include` commands can be used with render_template package.
2. `{% if ... %}`, `{% else %}`, `{% endif %}`; `{% include 'navbar.html' %}`; `{% block content %}`, `{% endblock %}`
3. Double direction bind - using `{{ xxx }}`
4. Using `flask_bootstrap` package is productive. (`pip install flask_bootstrap`)
5. Get flash message using `{% with messages = get_flashed_messages(with_categories=True) %}` (ref: flask.pocoo.org/docs/1.0/patterns/flashing/)
6. 

> Back-end Notes
1. Fix circular import problem.
    1. Create a python package folder named as app
    2. In app folder, create two files `__init__.py` and `routes.py`
    3. Copy all codes in `app.py` into `__init__.py` and then Ctrl+X all routes-related codes to `routes.py`
    4. Import necessary packages to correct errors in `routes.py`
    5. In `__init__.py` add one import `from app.routes import *`
    6. Create `run.py` under the project folder
    7. Copy the following code in `run.py`
    ```python
    from app.routes import app
    
    if __name__ == '__main__':
        app.run(debug=True, host='127.0.0.1', port=5000)
    ```
   8. Move templates and static folder under app folder, otherwise, an error TemplateNotFound will arise.
    
2. ...to be continued