import json

from tests.pages.userId import UsersId

user_information = json.load(open('tests/fixtures/user_information.json'))

def test_retrieve_data_from_existing_user():
    status_code, user_data = UsersId().get_user_data(1)
    assert status_code == 200
    assert user_data == user_information["user_1"]["data"]

def test_retrieve_empty_data_from_non_existing_user():
    status_code, user_data = UsersId().get_user_data(0)
    assert status_code == 404
    assert user_data == {}

def test_matching_algorithm():
    opposite = {
        "{" : "}",
        "(" : ")",
        "[" : "]"
    }
    string = "(a[b]c)" # input the string here
    stack = []
    for i in string:
        if i in opposite:
            stack.append(i)
        else:
            if i in opposite.values():
                try:
                    if opposite[stack[len(stack) - 1]] == i:
                        stack.pop()
                except:
                    assert False
    assert len(stack) == 0


