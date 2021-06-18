def add_assets(serial_number,user_name,id_status,res)
            if res == 1:

                        query = "INSERT INTO assets(serial_number,model,manufacturer) " \
                            "VALUES(%s,%s,%s)"
                        args = (serial_number,model,manufacturer,)

                        query2 = "INSERT INTO users (user_name) " \
                            "VALUES(%s)"
                        args2 = (user_name,)

                        query3 = "INSERT INTO assets_daily(serial_number,user_name,id_status,creation_date,initial_date) " \
                            "VALUES(%s,%s,%s,%s,%s)"
                        args3 = (serial_number,user_name,id_status,creation_date,initial_date,)

            elif res == 2:

                        query = "INSERT INTO assets(serial_number,model,manufacturer) " \
                            "VALUES(%s,%s,%s)"
                        args = (serial_number,model,manufacturer,)

                        query2 = "INSERT INTO users (user_name) " \
                            "VALUES(%s)"
                        args2 = (user_name,)

                        query3 = "INSERT INTO assets_daily(serial_number,user_name,id_status,creation_date,initial_date) " \
                            "VALUES(%s,%s,%s,%s,%s)"
                        args3 = (serial_number,user_name,id_status,creation_date,initial_date,)

            elif res == 3:

                        query = "INSERT INTO assets(serial_number,model,manufacturer) " \
                            "VALUES(%s,%s,%s)"
                        args = (serial_number,model,manufacturer,)

                        query2 = "INSERT INTO users (user_name) " \
                            "VALUES(%s)"
                        args2 = (user_name,)

                        query3 = "INSERT INTO assets_daily(serial_number,user_name,id_status,creation_date,initial_date) " \
                            "VALUES(%s,%s,%s,%s,%s)"
                        args3 = (serial_number,user_name,id_status,creation_date,initial_date,)

            else:

                        query = "INSERT INTO assets(serial_number,model,manufacturer) " \
                            "VALUES(%s,%s,%s)"
                        args = (serial_number,model,manufacturer,)

                        query2 = "INSERT INTO users (user_name) " \
                            "VALUES(%s)"
                        args2 = (user_name,)

                        query3 = "INSERT INTO assets_daily(serial_number,user_name,id_status,creation_date,initial_date) " \
                            "VALUES(%s,%s,%s,%s,%s)"
                        args3 = (serial_number,user_name,id_status,creation_date,initial_date,)

            try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        #conn.autocommit = false

        cursor = conn.cursor()
        cursor.execute(query, args)
        print ("Record Updated successfully ")

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        cursor.execute(query2, args2)
        print ("Record Updated successfully ")

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        cursor.execute(query3, args3)
        print ("Record Updated successfully ")

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

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