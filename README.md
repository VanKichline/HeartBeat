# HeartBeat
An IoT project to update a central site with process status

To enable:

 - Edit hb.py with appropriate system info
 - sudo cp hb.py /usr/local/bin/hb
 - See: http://www.stuffaboutcode.com/2012/06/raspberry-pi-run-program-at-start-up.html
 - sudo cp hb_service /etc/init.d/
 - sudo chmod 755 /etc/init.d/hb_service
 - sudo /etc/init.d/hb_service start
 - sudo /etc/init.d/hb_service stop
 - sudo update-rc.d hb_service defaults
 - sudo reboot
 - To remove: sudo update-rc.d -f hb_service remove

