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

key = '9db83dae13c7e59a07e131d4ed2a3c9b'
b64secret = 'ZboNNE/esWGreKU1/Y7CIWlSo36hwO6Gk6e4uwkfPY1lOsSnF8nK67Sg2wTFEA7f6V/dFjdFifgiAg1U+Y0WOw=='
passphrase = '4arsa9zrqkbs'

auth_client = gdax.AuthenticatedClient(key, b64secret, passphrase)
