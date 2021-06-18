from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import sys
import logging
import logging.config
import json

def main():

    #Load Logger File
        LOG_CONFIG_FILE = "logging.json"
        try:
                with open(LOG_CONFIG_FILE) as f:
                        config = json.load(f)
                        logging.config.dictConfig(config)
                        logger = logging.getLogger(__name__)
        except Exception as e:
                logger = logging.getLogger(__name__)
                logger.error("FATAL ERROR: %s", e)
                sys.exit(1)

        if len (sys.argv) != 1 :
                print ("Cantidad de Argumentos")
                logger.error ("Cantidad de Argumentos Erróneos")
                sys.exit (1)
        else:

                try:
                        db_config = read_db_config()
                        conn = MySQLConnection(**db_config)
                        #conn.autocommit = false
                        cursor = conn.cursor()
                        cursor.execute("SELECT * from assets_daily")
                        for row in cursor:
                                print(row)
                        #print (db_sn)
                        conn.commit()

                except Error as error:
                        print("Failed to update record to database rollback: {}".format(error))
                        #reverting changes because of exception
                        conn.rollback()

                finally:
                        #closing database connection.
                        if(conn.is_connected()):
                                cursor.close()
                                conn.close()
                                print("connection is closed")

if __name__ == '__main__':
        main()
