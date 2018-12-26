import os
import subprocess
print os.environ['NAME']
govinfoBashCommand = "./run govinfo --bulkdata=BILLSTATUS --congress=115 --debug"
billsBashCommand = "./run bills --congress=115 --debug"
votesBashCommand = "/run votes --congress=115 session=2018 --force --debug"

subprocess.Popen("git init", shell=True)
