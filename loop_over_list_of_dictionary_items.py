def namelist(names):

# takes a list of hashed items -- i.e. dictionary key-value pairs
# and returns a string of the values (not the keys)
    
    nameArr = []                            #store temp list of all names
    for item in names:
        nameArr.append(item['name'])
    
                                      
    if len(nameArr) < 2:                     
        namestring = ''.join(nameArr)                # returns one or 0 names
        # print(namestring)
        return namestring
    elif len(nameArr) == 2:                    
        namestring = ' & '.join(nameArr)            # return two names separated by &
        # print(namestring)
        return namestring
    elif len(nameArr) > 2:            
        namestring = ', '.join(nameArr[0:-1])           # join all but last name separated by commas
        namestring = namestring + ' & ' + nameArr[-1]     # add '& <last name>' to namestring
        # print(namestring)
        return namestring

    
n = [{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]

namelist(n)




# def namelist(names):

# same function as above, but tighter and more refined

#     if len(names) > 1:
#         return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),           # '{} & {}'.format('Ken','Sarah')
#                                 names[-1]['name'])                                        # returns  ---  'Ken & Sara'
#     elif names:
#         return names[0]['name']
#     else:
#         return ''