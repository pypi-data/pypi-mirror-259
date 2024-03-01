from .__cls_aide_dao_model_column__ import __cls_aide_dao_model_column__
from .__cls_aide_dao_db_types__ import __cls_aide_dao_db_types__


class __cls_aide_dao_model_main__:
    # noinspection PyMissingConstructor
    def __init__(self, new_dbc):
        self.dbc = new_dbc

        self.__dict_all = {}

        self.__db_type = None

        self.schema_name = None

        self.table_name = None

        self.table = f'{self.schema_name}.{self.table_name}'

        self.all_columns = f"{self.table}.*"

        self.dbc = new_dbc

        self._dict_select = {}

        self._dict_create_insert_update = {}

        self._sql_where = ""

        self.sql_type = None

        # self.actions = __cls_aide_dao_action__(new_table=self.table, new_db_type=self.__db_type)

    def set_base(self, db_type, schema_name, table_name):
        self.__dict_all = {}

        self.set_db_type(db_type)

        self.schema_name = f'"{schema_name}"'

        self.table_name = f'"{table_name}"'

        self.table = f'{self.schema_name}.{self.table_name}'

        self.all_columns = f"{self.table}.*"

        # self.actions.set(new_db_type=self.__db_type, new_table=self.table)

    @property
    def db_type(self):
        return self.__db_type

    def set_db_type(self, db_type: str):
        self.__db_type = __cls_aide_dao_db_types__.get_db_type(db_type)

    def new_column(self, new_pure_col_name: str,
                   new_mask_name: str = None,
                   new_map_code: str = None,
                   new_value=None,
                   new_default_value=None,
                   is_key: bool = False,
                   not_null: bool = False, ):
        return __cls_aide_dao_model_column__(new_pure_schema_name=self.schema_name,
                                             new_pure_table_name=self.table_name,
                                             new_pure_col_name=new_pure_col_name,
                                             new_mask_name=new_mask_name,
                                             new_map_code=new_map_code,
                                             new_value=new_value,
                                             new_default_value=new_default_value,
                                             is_key=is_key,
                                             not_null=not_null,
                                             dict_all=self.__dict_all,
                                             new_db_type=self.__db_type)

    @property
    def all(self):
        return self.__dict_all

    @property
    def dict_map_code(self):
        return {self.__dict_all[column_name]["map_code"]: column_name for column_name in self.__dict_all
                if self.__dict_all[column_name]["map_code"] is not None}

    # # 动态添加属性,可行，但是在IDE里无法自动提示和补全还有检测
    # def add_column(self, column_name):
    #     column = column_model(self.table, column_name, db_type=self.db_type)
    #     setattr(cls_dao_model_base, column_name, column)

    # actions
    @staticmethod
    def chk_col(col: str):
        col = col.replace('"', '')
        col = f'"{col}"'
        col = col.replace('.', '"."')
        col = col.replace('"*"', '*')
        return col

    def get_value(self, key):
        return self._dict_create_insert_update[key]

    def where(self, _sql_where):
        self._sql_where = " WHERE " + _sql_where

    def and_where(self, _sql_where):
        self._sql_where = self._sql_where + " AND " + _sql_where

    def or_where(self, _sql_where):
        self._sql_where = self._sql_where + " OR " + _sql_where

    @staticmethod
    def order_by(col_name_db):
        return f"ORDER BY {col_name_db} DESC"

    @staticmethod
    def limit(number):
        return f"LIMIT {number}"

    # Select
    def select(self, data: str, new_value: str = None):
        self.sql_type = "SELECT"

        column = data

        if isinstance(new_value, int):
            pass
        elif new_value is None:
            new_value = None
        else:
            new_value = new_value.replace("'", "''")
            new_value = f"'{new_value}'"

        value = new_value

        self._dict_select[column] = value

    @property
    def SQL_select(self):
        sql_select_item = None

        for key in self._dict_select:

            value = self._dict_select[key]

            column = self.chk_col(key)

            if value in [None, '', ]:
                pass
            else:
                column = f'{column} AS "{value}"'

            if sql_select_item is None:
                sql_select_item = column
            else:
                sql_select_item = f'{sql_select_item},{column}'

        sql = f"SELECT {sql_select_item}" \
              + f" FROM {self.table}" \
              + self._sql_where

        self._dict_select = {}

        return sql

    # Insert
    def add(self, data: str, new_value: str = None):
        self.sql_type = "INSERT"

        if data.find("=") > 0:
            split_index = data.find("=")
            column = data[:split_index]
            value = data[split_index + 1:]
        else:
            column = data
            if isinstance(new_value, int):
                pass
            elif new_value is None:
                new_value = 'NULL'
            else:
                new_value = new_value.replace("'", "''")
                new_value = f"'{new_value}'"

            value = new_value

        self._dict_create_insert_update[column] = value

    @property
    def SQL_add(self):

        sql_columns = None

        sql_values = None

        for key in self._dict_create_insert_update:

            value = self._dict_create_insert_update[key]

            column = self.chk_col(key)

            if sql_columns is None:
                sql_columns = column
                sql_values = value
            else:
                sql_columns = f'{sql_columns},{column}'
                sql_values = f"{sql_values},{value}"

        sql = f"INSERT " \
              + f" INTO {self.table}" \
              + f" ({sql_columns}) VALUES ({sql_values})"

        self._dict_create_insert_update = {}

        return sql

    # Update
    def update(self, data: str, new_value: str = None):
        self.sql_type = "UPDATE"
        self.add(data=data, new_value=new_value)

    @property
    def SQL_update(self):
        sql_update_item = None

        for key in self._dict_create_insert_update:

            value = self._dict_create_insert_update[key]

            column = self.chk_col(key)

            if sql_update_item is None:
                sql_update_item = f"{column}={value}"
            else:
                sql_update_item = f'{sql_update_item},f"{column}={value}"'

        sql = f"UPDATE " \
              + f" {self.table} SET {sql_update_item}" \
              + self._sql_where

        self._dict_create_insert_update = {}

        return sql

    def create(self, new_col_name: str,
               col_type: [__cls_aide_dao_db_types__.dict_col_type.keys()],
               not_null: bool = False,
               default_value: str = None,
               primary_key: bool = False,
               auto_increase: bool = False):

        col_name = self.chk_col(new_col_name)

        col_type = __cls_aide_dao_db_types__.dict_col_type[col_type][self.db_type]

        if not_null or primary_key:
            col_type += " NOT NULL "
        else:
            pass

        if primary_key and auto_increase:
            col_type += __cls_aide_dao_db_types__.dict_TYPE_primary_and_auto[self.db_type]
        elif primary_key and not auto_increase:
            col_type += __cls_aide_dao_db_types__.dict_TYPE_primary_key[self.db_type]
        elif not primary_key and auto_increase:
            col_type += __cls_aide_dao_db_types__.dict_TYPE_auto_increase[self.db_type]
        else:
            pass

        if default_value is not None:
            col_type += f"'{default_value}'"
        else:
            pass

        self._dict_create_insert_update[col_name] = col_type

    def SQL_creat(self):
        sql_create_item = None

        for key in self._dict_create_insert_update:

            value = self._dict_create_insert_update[key]

            column = self.chk_col(key)

            if sql_create_item is None:
                sql_create_item = f"{column} {value}"
            else:
                sql_create_item += f',{column} {value}'

        sql = f"CREATE TABLE {self.table}" \
              + f" ({sql_create_item})"

        return sql
