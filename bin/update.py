import os
import subprocess
import mysql.connector

try:
  cnx = connection.MySQLConnection(user=os.environ['DBUSERNAME'], 
                                 password=os.environ['DBPASSWORD'],
                                 host=os.environ['DBHOST'],
                                 database=os.environ['DBNAME'])


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
