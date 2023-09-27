import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass",
    database="MBTAdb"
    )

    mycursor = mydb.cursor()
    #complete the following line to add all the fields from the table

    sql = "insert into mbta_buses (id, latitude, longitude, direction_id, occupancy_status, current_status, current_stop_sequence, bearing, updated_at) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for mbtaDict in mbtaList:
        #complete the following line to add all the fields from the table
        val = (mbtaDict['id'], mbtaDict['latitude'], mbtaDict['longitude'], mbtaDict['direction_id'], mbtaDict['occupancy_status'], mbtaDict['current_status'], mbtaDict['current_stop_sequence'], mbtaDict['bearing'], mbtaDict['updated_at'])
        mycursor.execute(sql, val)

    mydb.commit()