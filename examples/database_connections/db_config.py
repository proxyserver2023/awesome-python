import examples.database_connections.config as config


class DB:
    __connection = None
    __cursor = None

    def __init__(self, database=config.DATABASE):
        self.__connection = self.get_connection(database)
        self.__cursor = self.__connection.cursor()

    def get_connection(self, database):
        __db_config = config.CONFIG[database]
        __db = None

        if database == config.MYSQL:
            try:
                import mysql.connector
                from mysql.connector import errorcode

                try:
                    __db = mysql.connector.connect(**__db_config)
                except mysql.connector.Error as err:
                    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                        print("Something is wrong with your user name or password")
                    elif err.errno == errorcode.ER_BAD_DB_ERROR:
                        print("Database does not exist")
                    else:
                        print("Problem in Database Connection")
            except Exception as e:
                print(f'Could not import the {database} package.\n{e}')

        return __db

    def query(self, query, params=None):
        self.__cursor.execute(query, params)
        return self.__cursor

    def close(self):
        self.__connection.close()


# Examples
if __name__ == "__main__":

    class UserDAO(object):
        __db = None

        def __init__(self):
            self.__db = DB()

        def get_users(self):
            return self.__db.query(
                f"""
                SELECT * FROM `users`
                """
            ).fetchall()

    user = UserDAO()
    users = user.get_users()