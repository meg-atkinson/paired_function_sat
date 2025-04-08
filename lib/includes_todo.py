#File: includes_todo.py

def includes_todo(line):
# if substring is in line, return true else return false
    if "#TODO" in line:
        return True
    return False