USERNAME="USER"
PASSWORD="PASSWORD"
HOSTNAME="HOSTNAME"
PORT="8083"
AUTHURL="http://" + HOSTNAME + ":" + PORT + "/ZAutomation/api/v1/login"
BASEURL="http://" + HOSTNAME + ":" + PORT + "/ZAutomation"
DEVICESURL="/api/v1/devices"
#LISTENIP='IP'

# Each entry is a list with the following elements:
#
# name of the virtual switch
# device id
# port # (optional; may be omitted)
FAUXMOS = [
    ['office lights', 'ZWayVDev_zway_11-0-37']
]
