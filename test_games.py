import games as g

def test_auth_exists():
    assert g.auth('user1') != ''


def test_auth_not_exists():
    assert g.auth('uzvr1') == ''


def test_valid_command_1():
    assert g.isValidCommand('sales')


def test_valid_command_2():
    assert g.isValidCommand('author')


def test_valid_not_command():
    assert not g.isValidCommand('qwer')


def test_create_sales():
    g.create('user1', 'sales', 'newsales')
    with open('salesList', 'r') as file:
        assert 'newsales' in file.read().split('\n')[-1]


def test_create_author():
    g.create('user1', 'author', 'newauthor')
    with open('authorList', 'r') as file:
        assert 'newauthor' in file.read().split('\n')[-1]