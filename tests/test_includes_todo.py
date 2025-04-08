#import function
from lib.includes_todo import includes_todo
# Check to see if it returns empty string
def test_empty_string():
    assert includes_todo("") == False

#test if #TODO at beginning of line returns True
def test_todo_at_start_return_as_true():
    assert includes_todo("#TODO buy milk") == True

#test if no #TODO returns False
def test_no_todo_return_as_false():
    assert includes_todo("drink tea") == False

#test if #TODO at end of line returns True
def test_todo_at_the_end_return_as_true():
    assert includes_todo("learn to test-drive my code #TODO") == True

#test if lowercase #todo returns False
def test_if_lower_return_as_false():
    assert includes_todo("learn to test-drive my code #todo") == False

#test if no hash with todo returns False
def test_if_no_hash_before_todo_return_as_false():
    assert includes_todo("learn to test-drive my code todo") == False