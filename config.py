import os

# EDIT
USERNAME = 'temp@abc.com'
PASSWORD = 'JatinPatel'
COURSES = [
    'l-essentiel-de-power-bi-2',
]

COLLECTIONS = [
    '6686199457681301504'
]

# EDIT IF YOU NEED TO
BASE_DOWNLOAD_PATH = os.path.join(os.path.dirname(__file__), "downloads")
USE_PROXY = False
PROXY = "http://127.0.0.1:8888" if USE_PROXY else None
