#!/usr/bin/bash

/usr/bin/python3 /home/lera/app/main.py

cat /home/lera/app/output.csv | tee /home/lera/VPN_Database/output.csv

cd /home/lera/VPN_Database/

git add .

git commit -m "Build: Add output.csv"

git push


