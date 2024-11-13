import os
import sys

def permission_closure():
    permissions = {
        'admin': ['read', 'write', 'delete'],
        'editor': ['read', 'write'],
        'viewer': ['read']
    }
    return permissions

def authorize(func):
    def wrapper(self, detail, data):
        permissions = permission_closure()
        action = func.__name__
        if action in permissions.get(self.role, []):
            return func(self, detail, data)
        else:
            raise PermissionError(f"Permission denied for {self.role} to perform {action} action.")
    return wrapper

class AuthorizedActions:
    def __init__(self, role):
        self.role = role

    @authorize
    def read(self, detail, data):
        fptr.write(f"Data is: {data}\n")
        return data

    @authorize
    def write(self, text, data):
        data += text
        fptr.write("Data updated\n")
        return data
        
    @authorize
    def delete(self, length, data):
        if int(length) > len(data):
            data = ""
        else:
            data = data[:-int(length)]
        fptr.write("Data deleted\n")
        return data

if __name__ == "__main__":
    data = ""
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    num = int(input("Enter number of operations: "))
    
    for i in range(num):
        name_role = input("Enter name:role: ")
        name, role = name_role.split(':')
        
        action_input = input("Enter action (or action:detail): ")
        
        detail = ''
        action = action_input
        if action != "read":
            action, detail = action_input.split(':')
            
        authorized_actions = AuthorizedActions(role=role)
        actions = {
            "read": authorized_actions.read,
            "write": authorized_actions.write,
            "delete": authorized_actions.delete
        }
        
        try:
            data = actions.get(action)(detail, data)
            
        except PermissionError as e:
            fptr.write(f"{str(e)}\n")
            
    fptr.close()
