
from utils import utils as u

class Load():
    def __init__(self) -> None:
        self.process = 'Load Process'

    def load_mysql(self, df, db_tbl_name):
        
        u.df_to_mysql(df, u.mysql_engine(), db_tbl_name)