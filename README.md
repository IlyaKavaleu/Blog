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

<h1>Blog</h1>

Educational project for fixing material with PostgreSQL database, fixtures, CSS, HTML, Python, Django, Bootstrap.
![mainpage_1](https://github.com/IlyaKavaleu/Blog/assets/97099564/47437ded-4bb6-4c23-8f54-d9b0fd7c0871)

The ability to see my cv, go and check out my GitHub, so the ability to navigate through sections and view posts with cars.
