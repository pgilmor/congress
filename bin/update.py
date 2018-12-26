import os
import subprocess
import mysql.connector
from mysql.connector import errorcode

try:
  cnx = connection.MySQLConnection(user=os.environ['DBUSERNAME'], 
                                 password=os.environ['DBPASSWORD'],
                                 host=os.environ['DBHOST'],
                                 database=os.environ['DBNAME']
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:

print os.environ['NAME']
govinfoBashCommand = "./run govinfo --bulkdata=BILLSTATUS --congress=115 --debug"
govinfo = govinfoBashCommand.split(" ")
billsBashCommand = "./run bills --congress=115 --debug"
bills = billsBashCommand.split(" ")
votesBashCommand = "/run votes --congress=115 session=2018 --force --debug"
votes = votesBashCommand.split(" ")

# subprocess.call(govinfo)
# subprocess.call(bills)
# subprocess.call(votes)

  cnx.close()
