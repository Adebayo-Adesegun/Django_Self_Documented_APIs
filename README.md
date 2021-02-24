# Building Self Documenting REST APIs with Django

## Complete project


### How do I get set up on windows? ###

* Navigate to the root directory of "django_project_smashing"
* Create a new virtual environment using  "python -m venv env" on the command line
* Activate the virtual environment using  "& .\env\scripts\activate"
* Run pip install -r requirements.txt to install all required dependencies on the activated virtual environment from the requirements text file
* Run the following "cd django_library_management" to navigate to the djnago project directory
* Run "python manage.py runserver" to run the project, the project runs on http://127.0.0.1:8000/
* Go to your browser and navigate to "http://127.0.0.1:8000/swagger" to view the swagger doc or "http://127.0.0.1:8000/redoc" for redoc



### How do I get set up on linux/mac? ###

* Navigate to the root directory of "django_project_smashing"
* Create a new virtual environment using  "python3 -m venv env"
* Activate the virtual environment using  "source env/bin/activate"
* Run pip3 install -r requirements.txt to install all required dependencies on the activated virtual environment from the requirements text file
* Run the following "cd django_library_management" to navigate to the djnago project directory
* Run "python3 manage.py runserver" to run the project, the project runs on http://127.0.0.1:8000/
* Go to your browser and navigate to "http://127.0.0.1:8000/swagger" to view the swagger doc or "http://127.0.0.1:8000/redoc" for redoc
