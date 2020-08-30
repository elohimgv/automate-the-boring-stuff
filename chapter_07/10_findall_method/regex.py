# Import module re
import re

def withSearch():
    # Creating regex object
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no group
    # Search the matching object
    mo = phoneNumRegex.search("Cell: 415-555-9999 Work: 212-555-6666")
    print("Using search() method:" )
    print(mo.group())

def withFindall(grp):
    if grp == 'no group':
        # Creating regex object
        phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no group
        # Search the matching object
        mo = phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-6666")
        print("Using findall() method with no groups:")
        print(mo)
    elif grp == 'group':
        # Creating regex object
        phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has group
        # Search the matching object
        mo = phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-6666")
        print("Using findall() method with groups:")
        print(mo)

# Calling function
withFindall('no group')
withFindall('group')
withSearch()
