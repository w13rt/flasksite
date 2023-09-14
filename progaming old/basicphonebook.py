def add():
    name = input("name: ")
    phone_number = input("phone number: ")
    return name + ":" + phone_number


def list(entries):
    for lines in entries:
        print(lines)

entries = []

while True:
    print( 
        '1. List all enrties',
        '2. Add entrie',
        '3. exit',
        sep='\n'

    )
    selection = input("What do ")

    if selection == '1':
        list(entries)
    elif selection == '2':
        entries.append(add())
    elif selection == '3':
        print("exiting...")
        exit()
    else: print("idk 1. 2. 3. seem like valid optionss...")