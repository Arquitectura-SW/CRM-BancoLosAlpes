from dotenv import load_dotenv
import os

load_dotenv()
POSTGRESS_HOST=os.getenv('POSTGRESS_HOST')
POSTGRESS_PORT=os.getenv('POSTGRESS_PORT')
POSTGRESS_DB_NAME=os.getenv('POSTGRESS_DB_NAME')
POSTGRESS_USER=os.getenv('POSTGRESS_USER')
POSTGRESS_PASSWORD_USER=os.getenv('POSTGRESS_PASSWORD_USER')
