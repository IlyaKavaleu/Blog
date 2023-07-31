<h1>Blog</h1>
How started my project on your local server?
The project for study Django.

<h3>Stack:</h3>
- Python - PostgreSQL - Local Developing All actions should be executed from the source directory of the project and only after installing all requirements.

<h3>Firstly, create and activate a new virtual environment:</h3>
python3.11.3 -m venv ../venv source ../venv/bin/activate

<h3>Install packages:</h3>
pip install --upgrade pip

pip install -r requirements.txt

<h3>Run project dependencies, migrations, fill the database with the fixture data etc.:</h3>
./manage.py migrate ./manage.py loaddata <path_to_fixture_files>


<h3>After completing the steps follow the link -- http://127.0.0.1:8000/</h3>

<h1>ToDoWoo for tasks.</h1>
