#!/bin/bash
cd /home/ec2-user/frontend/src
sudo serve -s build -l 8080
pm2 start npm --name "DietTracker" -- start
pm2 startup
pm2 save
pm2 restart all
