from openean.OpenEAN import OpenEAN
from pprint import pprint

userID = "400000000"  # user your own id here
openean = OpenEAN(userID)
example_ean = "4008233133614"


def get_ean():
    ean = input('EAN eingeben oder scannen: ')
    if ean == '':
        ean = example_ean
    return ean


def request(ean):
    items = openean.parse(ean)
    #items is a list of possible products associated with the code
    # the properties of each item are described here https://opengtindb.org/api.php
    return items


def get_title_from_answer(items):
    toret = ''
    iterated_items = 0
    for item in items:
        '''
        print(type(item))
        for key in item.keys():
            if key == 'name':  # key 'name' found
                if key is not None:
                    print('Name is: ', key)
                    toret = key
                else:  # if 'name' is empty look for 'detailname'
                    for key2 in item:
                        if key2 == 'detailname' and key2 is not None:
                            print('Detailname is: ', key2)
                            toret = key2
        '''
        if item.name:
            toret = item.name
        elif item.detailname:
            toret = item.detailname
        #print(item.name)
        #print(item.detailname)
        iterated_items += 1
    if toret == '' or iterated_items != 1:
        toret = input('No unambiguously title found!\nInput manually: ')
    return toret


def print_answer_complete(items):
    for item in items:
        pprint(vars(item))


if __name__ == "__main__":
    my_ean = get_ean()
    my_items = request(my_ean)
    print_answer_complete(my_items)
    my_title = get_title_from_answer(my_items)
    print(my_title)
