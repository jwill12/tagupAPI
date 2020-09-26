from datetime import datetime

time = datetime.today()

def create(id_num, string, num, bool):
    dict_data = {}
    dict_data['id'] = id_num
    dict_data['timestamp'] = time.utcnow().isoformat(sep=' ',
                                                     timespec='milliseconds')
    dict_data['value1'] = string
    dict_data['value2'] = num
    dict_data['value3'] = bool
    dict_data['creationDate'] = time.utcnow().isoformat(sep=' ',
                                                        timespec='milliseconds')
    dict_data['lastModificationDate'] = time.utcnow().isoformat(sep=' ',
                                                                timespec='milliseconds')
    return(dict_data)

def list(dictionary):
    exposed_data = {}
    exposed_data["id"] = dictionary["id"]
    exposed_data['timestamp'] = time.utcnow().isoformat(sep=' ',
                                                     timespec='milliseconds')
    exposed_data["value1"] = dictionary["value1"]
    exposed_data["value2"] = dictionary["value2"]
    exposed_data["value3"] = dictionary["value3"]
    print(exposed_data)


def read(dictionary, match_id):
    read_dict = {}
    if dictionary['id'] == match_id:
        read_dict["id"] = dictionary["id"]
        read_dict['timestamp'] = time.utcnow().isoformat(sep=' ',
                                                            timespec='milliseconds')
        read_dict["value1"] = dictionary["value1"]
        read_dict["value2"] = dictionary["value2"]
        read_dict["value3"] = dictionary["value3"]
        print(read_dict)
        print('\n')
    else:
        print('No matching records')

def delete(dictionary, match_id):
    if dictionary['id'] == match_id:
        del dictionary['id']
        return dictionary.clear()

def update(dictionary, match_id):
    update_dict = {}
    update_dict["id"] = match_id
    update_dict['timestamp'] = time.utcnow().isoformat(sep=' ',
                                                     timespec='milliseconds')
    return update_dict

def run_API():
    print('API, that will Create, Read, Update, and Delete a Record.\n')

    #
    # -- Create
    # creates two records
    #
    print('Enter two records to place in database. \n')

    id1, id2 = input('Enter two ids: ').split()
    string1, string2 = input('Enter two strings: ').split()
    float1, float2 = input('Enter two floats: ').split()
    bool1, bool2 = input('Enter two boolean values: ').split()
    print('\n')


    # create the two list ... demo before saving to memory
    # print the two list

    list(create(id1,string1,float1,bool1))
    list(create(id2,string2,float2,bool2))

    print('\n')

    print('--- Three choices ---\n'
          'r1 - record1, r2 - record 2, n - NO\n'
          '---               ---\n')

    #
    # -- Read
    # read a specific record
    # save to memory

    rec1 = create(id1,string1,float1,bool1)
    rec2 = create(id2,string2,float2,bool2)

    record = input('Choose a record to read (r1/r2/n)? ')

    if record == 'r1':
        read(rec1,rec1['id'])
    if record == 'r2':
        read(rec2,rec2['id'])
    if record == 'n':
        pass
        print('\n')


    #
    # - Update
    # update a record
    #

    # update one of the records
    # print out the updated record
    print("Update the id for record 1.")
    id1 = input("Enter a different id: ")

    print('\n')
    print('Records are updated!')

    # printing out the change
    list(create(id1, string1, float1, bool1))


    # update
    # save to memory
    rec1 = update(rec1,id1)
    print('\n')


    #
    # -- Delete
    # delete a record
    #

    delete_record = input('Choose a record to delete (r1/r2/n)? ')

    if delete_record == 'r1':
        delete(rec1,rec1['id'])
        print('Record Deleted.\n')
    if delete_record == 'r2':
        delete(rec2, rec2['id'])
        print('Record Deleted.\n')
    if delete_record == 'n':
        print('No deletes, records still in Database.\n')
        pass
        print('\n')


    #
    # Final demo
    # printing both records after crud process
    #

    if rec1 == {} and rec2 == {}:
        print('Both records are empty')
    elif rec1 == {}:
        print('record1 is empty, but record2 is not.')
        list(create(id2, string2, float2, bool2))
    elif rec2 == {}:
        print('record1 is not empty, but record2 is empty.')
        list(create(id1, string1, float1, bool1))
    else:
        print("Printing both records!")
        list(create(id1, string1, float1, bool1))
        list(create(id2, string2, float2, bool2))

run_API()

