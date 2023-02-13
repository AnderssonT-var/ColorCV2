import pyodbc

class con():

    url_BDD = 'JEROME'
    name_BDD = 'colores'
    name_user = 'sa'
    password = '0959133066'
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                            url_BDD+';DATABASE='+name_BDD+';UID='+name_user+';PWD=' + password)
        print("conexion exitosa")
    except Exception as e:
        print("error al conectar a la base", e)