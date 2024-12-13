import polars as pl
from core.base import Base
from db_directory.csv_db_api import DBApi


def db_apply(self, params):
    inputs = params[-1]
    case = 0
    value = self.db_api.methods(method=inputs["method"], values=inputs["values"])
    return case, value


class CsvDB(Base):

    def __init__(self, file_name, columns_names, func=db_apply, object_name: str = None):
        super().__init__(func, object_name)
        self.db_api = DBApi(file_name, columns_names)
