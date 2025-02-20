from ..fpcli_settings import config_folder
def get_init_content():
    return f'''from {config_folder}.database import Database
database= Database()
db=database.get_db
'''