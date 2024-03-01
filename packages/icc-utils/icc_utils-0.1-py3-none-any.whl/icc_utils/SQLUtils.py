#!/usr/bin/env python
__author__ = "Jordan Bradley"
__copyright__ = "Copyright 2023, International Cybernetics"
__credits__ = [""]
__license__ = ""
__version__ = "1.1.1"
__maintainer__ = "Jordan Bradley"
__email__ = "jbradley@internationalcybernetics.com"
__status__ = "Released"
__network_repository__ = "//icc-proc-vsf003/shares$/Services/Connect/ProcessingPlayground/icc_repo/pythonprojects"


import os
import configparser
from sqlalchemy.engine import URL
from sqlalchemy import create_engine, text


class SQLUtils:
    def __init__(self, config):
        config = configparser.ConfigParser()
        self.config_path = os.path.join(os.path.dirname(__file__), config)
        config.read(self.config_path)

        self.db_server = config['SQL AUTH']['SERVER']
        self.db_username = config['SQL AUTH']['USERNAME']
        self.db_password = config['SQL AUTH']['PASSWORD']

    def create_sql_engine(self, database):
        """
        Establishes a connection to the SQL Server database using SQLAlchemy.

        Returns:
        - engine: The database engine instance.
        """
        conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.db_server + ';DATABASE=' + database + ';UID=' + self.db_username + ';PWD=' + self.db_password
        conn_url = URL.create("mssql+pyodbc", query={"odbc_connect": conn_string})
        engine = create_engine(conn_url)
        return engine

    def fetch_all_databases(self):
        master_engine = self.create_sql_engine('master')
        with master_engine.connect() as conn:
            result = conn.execute(text("SELECT name FROM sys.databases"))
            database_list = [row[0] for row in result]
        return database_list
