import sqlite3

file_name = 'data.db'


class DatabaseConnection:
    def __int__(self):
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(file_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb or exc_val or exc_type:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()