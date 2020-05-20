
def auth(login):

    list_users = open('registeredUsers', 'r').read().split('\n')
    if login in list_users:
        print('Choose command: create, edit, show, exit')
        return login
    else:
        print('Incorrect Login! Check and try again!')
        return ''


def isValidCommand(command):
    return command in ['sales', 'author']


def create(currentUser, command, note):
    fileName = f'{command}List'
    with open(fileName, 'r+') as file:
        listOfSales = file.read().split('\n')
        file.write(f'\n{len(listOfSales) + 1} {currentUser} {note}')
        return True


if __name__ == "__main__":
    currentUser = ''
    while True:
        if currentUser == '':
            login = input('Enter login\n')
            currentUser = auth(login)
        command = input('Enter command\n')
        if command == 'create':
            word = input('Please choose what you want to create sales or author\n')

            if not isValidCommand(word):
                print('Incorrect command')
                continue
            note = input(f'Please enter a {command} note\n')
            create(currentUser, word, note)
        if command == 'exit':
            break

        # salesList = open('salesList', 'a')
        # registeredUsersList = open(' registeredUsers', 'r')
        # user = input()

