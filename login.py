import gdax

###########################################################
##                                                       ##
##  This section is for connecting to your GDAX account  ##
##                                                       ##
###########################################################

# 3 inputs needed that is generated under the GDAX API webpage
# key = API key
# b64secret = API secret key
# passphrase = passphrase from GDAX

key = 
b64secret = 
passphrase = 

auth_client = gdax.AuthenticatedClient(key, b64secret, passphrase)
