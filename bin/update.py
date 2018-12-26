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

gitBashCommand = "git init" 
configBashCommand = "git config user.name {} | git config user.email {} | git config github.user {} | git config github.token {} | git remote add heroku https://github.com/pgilmor/congress.git".format(name, email, githubUser, token)
git = gitBashCommand.split(" ")
config = configBashCommand.split(" ")
govinfoBashCommand = "./run govinfo --bulkdata=BILLSTATUS --congress=115 --debug"
govinfo = govinfoBashCommand.split(" ")
billsBashCommand = "./run bills --congress=115 --debug"
bills = billsBashCommand.split(" ")
votesBashCommand = "/run votes --congress=115 session=2018 --force --debug"
votes = votesBashCommand.split(" ")
commitBashCommand ="git add . && git commit -m 'Update' && git push heroku master"
commit = commitBashCommand.split(" ")

subprocess.call(git)
subprocess.call(configBashCommand, shell=True)
#subprocess.call("git","config", "user.email", os.environ['EMAIL'])
#subprocess.call("git","config", "github.user", os.environ['USERNAME'])
#subprocess.call("git","config", "github.token", os.environ['GITHUB'])
#subprocess.call("git","remote","add","https://github.com/pgilmor/congress.git")
#subprocess.call(govinfo)
#subprocess.call(bills)
subprocess.call(votes)
subprocess.call(commit)
#subprocess.call("git","commit","-m","'data update'")
#subprocess.call("git","push","heroku","master")

#cnx.close()
