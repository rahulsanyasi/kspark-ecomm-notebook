# repo

kspark-ecomm-notebook

# create virtual environment

python -m venv .venv

# activate virtual environment

.venv\Scripts\activate

# install requirements.txt

pip install -r requirements.txt

# to run uvicorn server
uvicorn notebook-app:app --reload

# Install pytest:
python -m pip install pytest

# Execute the tests:
python -m pytest

pip install requests