import ast

import numpy as np
import pandas as pd
from globals.globals import GLOBALS
import os


class DBApi:

    def __init__(self, file_name: str, columns_names: list):
        print("the first column is the index column. e.g. - type_name")
        self.file_name = file_name
        self.columns_names = columns_names
        self.index_column = columns_names[0]
        self.db_path = str(os.path.join(GLOBALS.project_directory, self.file_name))
        self.df = None
        self.init_df()

    def init_df(self) -> None:
        try:
            self.df = pd.read_csv(self.db_path)
            self.df = self.df.map(self.parse_value)
        except:
            self.df = pd.DataFrame(columns=self.columns_names)
            self.save_db()

    def get_col(self, col_name):
        return self.df[col_name].tolist()

    def get_row(self, row_name):
        return self.df[self.df[self.index_column] == row_name]

    def get_index(self, indexes):
        row_name, col_name = indexes
        return self.df[self.df[self.index_column] == row_name][col_name].iloc[0]  # .tolist()[0]

    def set_row(self, row_values: dict):
        if row_values[self.index_column] in self.get_col(self.index_column):
            self.df.loc[self.df['type_name'] == row_values[self.index_column], list(row_values.keys())] = list(row_values.values())
        else:
            self.df = pd.concat([self.df, pd.DataFrame([row_values])], ignore_index=True)
        self.save_db()

    def save_db(self):
        self.df.to_csv(self.db_path, index=False)

    def methods(self, method: str, values: dict = None):
        methods_dict = {
            "get_col": self.get_col,
            "get_row": self.get_row,
            "get_index": self.get_index,
            "set_row": self.set_row,
            "save_db": self.save_db
        }
        response = {"value": methods_dict[method](values)}
        return response

    def parse_value(self, value):
        try:
            # Attempt to parse the value using literal_eval
            parsed_value = ast.literal_eval(value)
            # Convert lists to NumPy arrays
            if isinstance(parsed_value, list):
                return np.array(parsed_value)
            # Return dictionaries as is
            elif isinstance(parsed_value, dict):
                return parsed_value
            else:
                return value  # Return the value unchanged if not a list or dict
        except (ValueError, SyntaxError):
            # If parsing fails, return the original value
            return value
