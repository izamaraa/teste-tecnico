from utils.database import insertTables

from utils.read import read_file

import os.path

python_file= "db.sqlite3"
file_path= os.path.isfile(python_file)

FILEPATH= "teste.txt"

if file_path == True:
    try:
        data= read_file(FILEPATH)
        insertTables(data)
        print("arquivo encontrado com sucesso")
    except(FileNotFoundError):
        print("arquivo nao enocontrado")


