Capstone

Setting up virtual environment (VENV)

git clone [Your-Repo-URL]
cd [Your-Repo-Directory]

python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver

Using Docker

docker build -t [your-app-name] .
docker run -p 8000:8000 --env-file .env [your-app-name]
The application will be available at http://localhost:8000