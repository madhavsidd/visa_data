
#!/bin/bash
#scp -i ~/gcp_key.pem -r ./src/* maddy@34.30.156.114:/home/maddy
#ssh -i gcp3 -r ./src/*  maddy@34.30.156.114:/home/maddy
scp -i /home/madhav/gcp3 -r ./src/* maddy@34.30.156.114:/home/maddy
