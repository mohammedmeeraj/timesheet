# import mysql.connector
# from mysql.connector import pooling

# class DatabasePool:
#     _instance = None  # Class-level variable to store the singleton instance

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(DatabasePool, cls).__new__(cls)
#             cls._instance._initialize_pool()
#         return cls._instance

#     def _initialize_pool(self):
#         db_config = {
#             "host": "10.95.136.128",
#             "user": "app_user",
#             "password": "Mohammed&meeraj786",
#             "database": "timesheet"
#             # "host": "localhost",
#             # "user": "fabuser",
#             # "password": "fabuser&123",
#             # "database": "fab"
#         }
#         self.db_pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=50, **db_config)

#     def get_db_connection(self):
#         return self.db_pool.get_connection()

import mysql.connector
from mysql.connector import pooling
from contextlib import contextmanager

class DatabasePool:
    _read_instance = None  # Singleton instance for read pool
    _write_instance = None  # Singleton instance for write pool

    def __new__(cls, pool_type="read"):
        if pool_type == "read":
            if cls._read_instance is None:
                cls._read_instance = super(DatabasePool, cls).__new__(cls)
                cls._read_instance._initialize_pool(pool_type)
            return cls._read_instance
        elif pool_type == "write":
            if cls._write_instance is None:
                cls._write_instance = super(DatabasePool, cls).__new__(cls)
                cls._write_instance._initialize_pool(pool_type)
            return cls._write_instance

    def _initialize_pool(self, pool_type):
        db_config = {
            "host": "10.95.136.128",
            "user": "app_user",
            "password": "Mohammed&meeraj786",
            "database": "timesheet"
        }

        pool_size = 20 if pool_type == "read" else 25  # More connections for reads
        pool_name = "read_pool" if pool_type == "read" else "write_pool"

        self.db_pool = pooling.MySQLConnectionPool(pool_name=pool_name, pool_size=pool_size,pool_reset_session=True, **db_config)
    # @contextmanager
    # def get_db_connection(self):
    #     # return self.db_pool.get_connection()
    #     conn=self.db_pool.get_connection()
    #     try:
    #         yield conn
    #     finally:
    #         conn.close()
    
    @contextmanager
    def get_db_connection(self):
        if self.db_pool is None:
            raise ConnectionError("Database pool is not initialized")

        conn = None
        try:
            conn = self.db_pool.get_connection()
            yield conn
        except mysql.connector.Error as err:
            print("Error getting database connection:", err)
        finally:
            if conn:
                conn.close()

