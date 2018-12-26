import os
import subprocess
#import mysql.connector


#cnx = connection.MySQLConnection(user=os.environ['DBUSERNAME'], 
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

subprocess.call("git","init")
subprocess.call("git","config", "user.name", os.environ['NAME'])
subprocess.call("git","config", "user.email", os.environ['EMAIL'])
subprocess.call("git","config", "github.user", os.environ['USERNAME'])
subprocess.call("git","config", "github.token", os.environ['GITHUB'])
subprocess.call("git","remote","add","https://github.com/pgilmor/congress.git")
#subprocess.call(govinfo)
subprocess.call(bills)
#subprocess.call(votes)
subprocess.call("git","add",".")
subprocess.call("git","commit","-m","'data update'")
subprocess.call("git","push","heroku","master")

#cnx.close()
