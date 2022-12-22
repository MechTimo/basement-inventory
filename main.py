from openean.OpenEAN import OpenEAN
from pprint import pprint

userID = "400000000"  # user your own id here

openean = OpenEAN(userID)

barcode_num = "4008233133614"  # number of you product

items = openean.parse(barcode_num)
#items is a list of possible products associated with the code
# the properties of each item are described here https://opengtindb.org/api.php

for item in items:
    pprint(vars(item))
