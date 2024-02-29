# pip install psycopg2
import psycopg2
from .__cls_aide_rst_base__ import __cls_aide_rst_base
from .__cls_aide_sql_pgs__ import __cls_aide_sql_pgs


class __cls_conn(__cls_aide_rst_base, __cls_aide_sql_pgs):
    # noinspection PyMissingConstructor
    def __init__(self, host=None, port=None, database=None, user=None, password=None):
        self.db_type = "pgs"

        self.rst = self._cls_aide_rst_base(self.db_type)

        self.__dirt_connection_info = {"host": None,
                                       "port": None,
                                       "database": None,
                                       "user": None,
                                       "password": None,
                                       "connected": None,
                                       "connected_time": None,
                                       "SQL": None}

        self.conn = None

        if database is None:
            pass
        else:
            self.set_host(host)
            self.set_port(port)
            self.set_database(database)
            self.set_user(user)
            self.set_password(password)

            self.connect()

    @property
    def connection_info(self):
        return self.__dirt_connection_info

    @property
    def host(self):
        return self.__dirt_connection_info["host"]

    def set_host(self, new_value):
        self.__dirt_connection_info["host"] = new_value

    @property
    def port(self):
        return self.__dirt_connection_info["port"]

    def set_port(self, new_value):
        self.__dirt_connection_info["port"] = new_value

    @property
    def database(self):
        return self.__dirt_connection_info["database"]

    def set_database(self, new_value):
        self.__dirt_connection_info["database"] = new_value

    @property
    def user(self):
        return self.__dirt_connection_info["user"]

    def set_user(self, new_value):
        self.__dirt_connection_info["user"] = new_value

    @property
    def password(self):
        return self.__dirt_connection_info["password"]

    def set_password(self, new_value):
        self.__dirt_connection_info["password"] = new_value

    @property
    def connected(self):
        return self.__dirt_connection_info["connected"]

    def set_connected(self, new_value):
        if new_value is None:
            new_value = False
        else:
            pass

        self.__dirt_connection_info["connected"] = new_value

    @property
    def connected_time(self):
        return self.__dirt_connection_info["connected_time"]

    def set_connected_time(self, new_value):
        self.__dirt_connection_info["connected_time"] = new_value

    @property
    def SQL(self):
        return self.__dirt_connection_info["SQL"]

    def set_SQL(self, new_value):
        self.__dirt_connection_info["SQL"] = new_value

    def connect(self):
        self.rst.set_process("connect")

        if self.database is None:
            self.rst.set(False,
                         f'database name missing!',
                         self.host)
        else:
            try:
                self.set_connected(False)
                self.conn = psycopg2.connect(host=self.host, database=self.database, port=self.port, user=self.user,
                                             password=self.password)

                self.set_connected(True)

                self.rst.set(self.connected,
                             f'Connected! Cost:{self.rst.dur}',
                             self.host)
            except Exception as e:

                if e:
                    self.rst.set(False,
                                 f'Exception:Connection failed! Cost:{self.rst.dur}',
                                 e.__str__())
                else:
                    self.rst.set(False,
                                 f'DB ERROR:Connection failed! Cost:{self.rst.dur}',
                                 f'DB error_log:######################')

    def disconnect(self):
        if self.connected is True:
            if self.connected is True:
                self.conn.close()
                self.set_connected(False)

    def __execute_sql_base__(self, sql, sql_type):
        self.rst.set_process(f"{sql_type}.{self.rst.process}")
        self.set_SQL(sql)

        if self.connected is True:
            pass
        else:
            self.connect()
            if self.rst.state is False:
                return None

        self.rst.set(False, None)

        cur = self.conn.cursor()

        try:
            cur.execute("BEGIN" + ";")

            sql = self.SQL

            if sql[-1:] == ";":
                pass
            else:
                self.set_SQL(f"{sql};")

            cur.execute(self.SQL)

            self.conn.commit()

            if sql_type == "SELECT":
                data = cur.fetchall()
                data_desc = cur.description
                data_header = [desc[0] for desc in data_desc]
                data_with_header = {i: dict(zip(data_header, row)) for i, row in enumerate(data)}
                data = data_with_header
            else:
                data = cur.statusmessage

            self.rst.set(True,
                         f'{sql_type} successful!Cost:{self.rst.dur}',
                         data)
        except Exception as e:
            self.conn.rollback()
            if e:
                self.rst.set(False,
                             'Exception:' + e.__str__().replace("'", "") + f',Cost:{self.rst.dur}',
                             sql)
            else:
                self.rst.set(False,
                             'DB ERROR:' + self.conn.stmt_errormsg() + f',Cost:{self.rst.dur}',
                             sql)
        finally:
            cur.close()

        return self.rst.state

    def __execute_sql(self, sql, sql_type):
        sql = sql.strip()
        if sql[0:6].upper() == sql_type.upper():
            self.__execute_sql_base__(sql, sql_type)
        else:
            self.rst.set(False, f'Only {sql_type} SQL can be execute!,Cost:{self.rst.dur}', sql)

    def select(self, sql):
        self.__execute_sql(sql, sql_type='SELECT')

    def insert(self, sql):
        self.__execute_sql(sql, sql_type="INSERT")

    def update(self, sql):
        self.__execute_sql(sql, sql_type='UPDATE')

    def delete(self, sql):
        self.__execute_sql(sql, sql_type='DELETE')

    def creat(self, sql):
        self.__execute_sql(sql, sql_type="CREATE")

    def load_activity_count(self):
        self.rst.set_process("load_activity_count")

        sql = self._sql_list_activity_count

        self.select(sql)

    def load_schemas(self, no_system_schemas: bool = True):
        self.rst.set_process("load_schemas")

        sql = self._sql_list_schemas(no_system_schemas=no_system_schemas)

        self.select(sql)

    def load_tables(self, schema_name):
        self.rst.set_process("load_tables")

        sql = self._sql_list_tables(schema_name=schema_name)

        self.select(sql)

    def load_all_tables(self, split_schema_table: bool = False, no_system_schemas: bool = True):
        self.rst.set_process("load_all_tables")

        sql = self._sql_list_all_tables(split_schema_table=split_schema_table, no_system_schemas=no_system_schemas)

        self.select(sql)

    def load_table_structure(self, table_name):
        self.rst.set_process("load_table_structure")

        sql = self._sql_list_table_structure(table_name=table_name)

        self.select(sql)

    def clone(self):
        pass
