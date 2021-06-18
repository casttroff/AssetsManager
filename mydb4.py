
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from snipe  import get_assets
from datetime import datetime
import sys
import json
import logging
import logging.config
import uuid


def insert_daily(serial_number,user_name,id_status,cursor,timestamp,logger,reference_id):

    try:
        creation_date = timestamp
        initial_date = timestamp
        if id_status == "1":
            db_sn = cursor.execute("SELECT EXISTS (SELECT id_status from assets_daily WHERE serial_number = %s and id_status = %s)" \
                    ,(serial_number,id_status,))
            db_sn = cursor.fetchone()
            if db_sn[0] == 0:
                query = "INSERT INTO assets_daily(serial_number,user_name,id_status,creation_date,initial_date) " \
                    "VALUES(%s,%s,%s,%s,%s)"
                args = (serial_number,user_name,id_status,creation_date,initial_date,)
                cursor.execute(query, args)
            else:
                print ("Ya existe el registro")

        if id_status == "2" or id_status == "3":
            previous_status = "1"
            db = cursor.execute("SELECT EXISTS (SELECT id_assets_daily from assets_daily WHERE serial_number = %s and id_status = %s)" \
                        ,(serial_number,previous_status,))
            db = cursor.fetchone()
            print (db[0])
            if db[0] == 1:
                db_id = cursor.execute("SELECT id_assets_daily from assets_daily WHERE serial_number = %s and id_status = %s" \
                        ,(serial_number,previous_status,))
                db_id = cursor.fetchone()
                cursor.execute("UPDATE assets_daily set id_status = %s, finish_date = %s, user_name_finish = %s WHERE id_assets_daily = %s" \
                    ,(id_status,timestamp,user_name,db_id[0],))
                db_id = cursor.execute("SELECT * from assets_daily WHERE id_assets_daily = %s" \
                    ,(db_id[0],))
                db_id = cursor.fetchone()
                #print(db_id)
                print("kk")

    except ValueError:
            raise ("Error")

def check_assets(serial_number,user_name,cursor,timestamp,logger,reference_id):
    try:
        creation_date = timestamp
        logger.info (str(reference_id) + " - Chequeando " + serial_number + " en Snipe")
        get_assets(serial_number)
        db_sn = cursor.execute("SELECT EXISTS (SELECT id_assets from assets WHERE serial_number = %s)" \
            ,(serial_number,))
        db_sn = cursor.fetchone()
        if (db_sn[0] == 0):
            print( 'Insertar SN')
            logger.info (str(reference_id) + " - Insertando " + serial_number + " en DB")
            val = get_assets(serial_number)
            print (val)
            model = val[0]
            manufacturer = val[1]
            macaddress = val[2]
            query1 = "INSERT INTO assets(serial_number,model,manufacturer,macaddress,creation_date) " \
                "VALUES(%s,%s,%s,%s,%s)"
            args1 = (serial_number,model,manufacturer,macaddress,creation_date,)
            cursor.execute(query1, args1)
            logger.info (str(reference_id) + " - Se insertó " + serial_number + " " +\
                 manufacturer + " " + macaddress + " en DB")
        db_user = cursor.execute("SELECT EXISTS (SELECT id_user from users WHERE user_name = %s)" \
            ,(user_name,))
        db_user = cursor.fetchone()
        if (db_user[0] == 0):
            print( 'Insertar USER')

            query2 = "INSERT INTO users (user_name,creation_date) " \
                "VALUES(%s,%s)"
            args2 = (user_name,creation_date,)
            cursor.execute(query2, args2)

    except ValueError:
            raise ("Error")

    #insert_assets(serial_number,user_name,id_status,insert)
    #print (insert)

def ll(serial_number,user_name,id_status):

    #Generate Unique ID
    reference_id = uuid.uuid4()
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

    #if len (sys.argv) != 4 :
    #    print ("Cantidad de Argumentos")
    #    logger.error (str(reference_id) + " - Cantidad de Argumentos Erróneos")
    #    sys.exit (1)
    #else:
    #    arguments = sys.argv[1:]
    #    serial_number = sys.argv[1]
    #    user_name = sys.argv[2]
    #    id_status = sys.argv[3]
    #    count = len(arguments)
    #    print (serial_number,user_name,id_status)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        #conn.autocommit = false
        cursor = conn.cursor()
        logger.info (str(reference_id) + " - Conexión DB")
        #check_assets('serial_number','user_name')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        initial_date = timestamp
        finish_date = timestamp
        logger.info (str(reference_id) + " - Chequeando Assets")
        check_assets(serial_number,user_name,cursor,timestamp,logger,reference_id)
        #insert_daily(serial_number,user_name,id_status,check_assets)
        insert_daily(serial_number,user_name,id_status,cursor,timestamp,logger,reference_id)
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




#if __name__ == '__main__':
#    main()