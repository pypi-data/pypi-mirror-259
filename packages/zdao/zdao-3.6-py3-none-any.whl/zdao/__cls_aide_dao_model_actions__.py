


class __cls_aide_dao_action__:
    def __init__(self, new_table: str, new_dbc=None, new_db_type: str = None):
        self._table = new_table

        if new_db_type is None:
            if hasattr(new_dbc, 'db_type'):
                new_db_type = new_dbc.db_type
            else:
                new_db_type = "pgs"
        else:
            pass


        self._db_type = new_db_type

        self.dbc = new_dbc

        self._dict_select = {}
        self._dict_create_insert_update = {}

        self._sql_where = ""

        self.sql_type = None


