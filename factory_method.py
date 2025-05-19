from abc import ABC, abstractmethod
import sqlite3
import datetime

#logger interface for all loggers
class logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

#Concrete Logger -logs message to console
class console_logger(logger):
    def log(self, message: str):
        print(f"[Console] {message}")

#Concrete Logger - logs message to a text file
class file_logger(logger):
    def __init__(self, filename="log.txt"):
        self.filename = filename

    def log(self, message: str):
        with open(self.filename, 'a') as f:
            f.write(f"[File] {message}\n")

#Concrete Logger - logs message to a database
class database_logger(logger):
    def __init__(self, db_name="logs.db"):
        self.conn = sqlite3.connect(db_name)
        self._create_table()

    def _create_table(self): #create table if one does not already exist
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    message TEXT
                )
            ''')

    def log(self, message: str): #added timestamp to database log
        timestamp = datetime.datetime.now().isoformat()
        with self.conn:
            self.conn.execute("INSERT INTO logs (timestamp, message) VALUES (?, ?)", (timestamp, message))

#Factory Method - factory chooses which logger to ceate based on input
class logger_factory:
    @staticmethod
    def create_logger(output_type: str) -> logger:
        if output_type == "console":
            return console_logger()
        elif output_type == "file":
            return file_logger()
        elif output_type == "database":
            return database_logger()
        else:
            raise ValueError(f"Unknown logger type: {output_type}")


if __name__ == "__main__":
    logger_type = "file"  
    logger_instance = logger_factory.create_logger(logger_type)
    logger_instance.log("This is a factory-created log message.")


