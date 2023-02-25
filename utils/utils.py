import sqlalchemy as db
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os 

load_dotenv()
myPWD = os.getenv("PWD")
myDB_HOST = os.getenv("DB_HOST")
myDB = os.getenv("DB")
myUSER = os.getenv("USER")
myPORT = os.getenv("PORT")
'''
Create a mapping of df dtypes to mysql data types (not perfect, but close enough)
'''
def dtype_mapping():
    return {'object' : 'TEXT',
        'int64' : 'INT',
        'float64' : 'FLOAT',
        'datetime64' : 'DATETIME',
        'bool' : 'TINYINT',
        'category' : 'TEXT',
        'timedelta[ns]' : 'TEXT'}

'''
Create a sqlalchemy engine
'''
# def mysql_engine_bk(user = 'root', password = '123', host = '127.0.0.1', port = '3306', database = 'db'):
#     engine = create_engine("mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8".format(user, password, host, port, database))
#     return engine

def mysql_engine(user = myUSER, password = myPWD, host = myDB_HOST, port = myPORT, database = myDB):
    engine = create_engine("mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8".format(user, password, host, port, database))    
    return engine
'''
Create a mysql connection from sqlalchemy engine
'''
def mysql_conn(engine):
    conn = engine.raw_connection()
    return conn

'''
Create sql input for table names and types
'''
def gen_tbl_cols_sql(df):
    dmap = dtype_mapping()
    sql = "pi_db_uid INT AUTO_INCREMENT PRIMARY KEY"
    df1 = df.rename(columns = {"" : "nocolname"})
    hdrs = df1.dtypes.index
    hdrs_list = [(hdr, str(df1[hdr].dtype)) for hdr in hdrs]
    for hl in hdrs_list:
        sql += " ,{0} {1}".format(hl[0], dmap[hl[1]])
    return sql

'''
Create a mysql table from a df
'''
def create_mysql_tbl_schema(df, conn, db, tbl_name):
    tbl_cols_sql = gen_tbl_cols_sql(df)
    sql = "USE {0}; CREATE TABLE IF NOT EXISTS {1} ({2})".format(db, tbl_name, tbl_cols_sql)
    cur = conn.cursor()
    cur.execute(sql)
    cur.close()
    conn.commit()

'''
Write df data to newly create mysql table
'''
def df_to_mysql(df, engine, tbl_name):
    df.to_sql(tbl_name, engine, if_exists='replace')