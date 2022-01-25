from typing import Dict,List

def readContacts(fname:str) -> Dict[str,Dict[str, str]]:
    contacts:Dict[str,Dict[str, str]] = {}
    with open(fname, 'r') as infile:
        lineList:List[str] = infile.readlines()
        # First line is field names
        fieldnames:List[str] = lineList[0].split(',')
        # Get rid of extra white space in the field names
        for i in range(len(fieldnames)):
            fieldnames[i] = fieldnames[i].strip()

        # All the lines after the first one
        for line in lineList[1:]:
            # Assume len(fields) == len(fieldnames)
            fields:List[str] = line.split(',')
            record:Dict[str, str] = {}
            for i in range(len(fieldnames)):
                # Store the field into the person's record (dictionary)
                record[fieldnames[i]] = fields[i].strip()
            key:str = record['lastname'] + ', ' + record['firstname']
            # Stores the record dictionary into the contacts dictionary
            contacts[key] = record
    return contacts

def main(args:List[str]) -> int:
    contacts:Dict[str, Dict[str, str]] = readContacts('userids.csv')
    keys:List[str] = list(contacts.keys())

    # Add a new field, based on the old ones
    for k in keys:
        contacts[k]['email'] = contacts[k]['userid'] + '@converse.edu'

    # Print entries in contacts
    for k in keys[:20]:
        print(k, contacts[k])

    # Extract a particular field in the contact record for each person
    print()
    for k in keys[:20]:
        print('{0:30}{1}'.format(k, contacts[k]['email']))

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)