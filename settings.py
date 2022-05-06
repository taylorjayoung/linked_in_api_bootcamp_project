from dotenv import load_dotenv
 
## using existing module to specify location of the .env file
from pathlib import Path
import os
 
load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
 
# retrieving keys and adding them to the project
# from the .env file through their key names
ENDPOINT = os.getenv("MYPROJECT_APIENDPOINT")
PW = os.getenv("MYPROJECT_DBPASSWORD")

print('ENDPOINT')
print(ENDPOINT)
print('PW')
print(PW)
