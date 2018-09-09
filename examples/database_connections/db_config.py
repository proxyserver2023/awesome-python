import examples.database_connections.config as config


def get_mysql_connection():
    db = ""
    return db


def get_database_connection(database_name):
    return {
        config.MYSQL: get_mysql_connection()
    }[database_name]

