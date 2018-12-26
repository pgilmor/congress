import os
import subprocess
#import mysql.connector


#cnx = connection.MySQLConnection(user=os.environ['DBUSERNAME'], 
#                                 password=os.environ['DBPASSWORD'],
#                                 host=os.environ['DBHOST'],
#                                 database=os.environ['DBNAME'])


print os.environ['NAME']
name = os.environ['NAME']
email = os.environ['EMAIL']
githubUser = os.environ['USERNAME']
token = os.environ['TOKEN']

gitBashCommand = "git init | git config user.name {} | git config user.email {} | git config github.user {} | git config github.token {} | git remote add heroku https://github.com/pgilmor/congress.git".format(name, email, githubUser, token)
govinfoBashCommand = "./run govinfo --bulkdata=BILLSTATUS --congress=115 --debug"
govinfo = govinfoBashCommand.split(" ")
billsBashCommand = "./run bills --congress=115 --debug"
bills = billsBashCommand.split(" ")
votesBashCommand = "/run votes --congress=115 session=2018 --force --debug"
votes = votesBashCommand.split(" ")
commitBashCommand ="git add . | git commit -m 'Update' | git push heroku master"
commit = commitBashCommand.split(" ")

subprocess.call(gitBashCommand, shell=True)
#subprocess.call(govinfo)
#subprocess.call(bills)
subprocess.Popen(votes, cwd="/")
subprocess.call(commitBashCommand, shell=True)


#cnx.close()
