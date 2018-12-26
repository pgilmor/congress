import os
import subprocess
print os.environ['NAME']
govinfoBashCommand = "./run govinfo --bulkdata=BILLSTATUS --congress=115 --debug"
govinfo = govinfoBashCommand.split(" ")
billsBashCommand = "./run bills --congress=115 --debug"
votesBashCommand = "/run votes --congress=115 session=2018 --force --debug"

subprocess.call(govinfo)
