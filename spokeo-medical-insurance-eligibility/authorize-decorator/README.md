# User Permissions Program

This project is a Python program using closures to manage and retrieve user permissions for different roles (admin, editor, viewer) and define their allowed actions. Additionally, a decorator is implemented to ensure that a user has the correct permissions to execute specific functions based on their role and the required action.

## Role-Based Permissions

- **Admins**: Can read, write, and delete.
- **Editors**: Can read and write.
- **Viewers**: Can only read.

## Function Descriptions

### `permission_closure()`
- Defines a closure function to manage permissions for different roles.
- **Returns**: A function `check_permission(user_role, action)` that verifies if a given action is allowed for a specified user role based on predefined permissions.

### `authorize(func)`
- A decorator function that authorizes actions for a user role.
- **Parameters**: `func` - the function to be wrapped and checked for authorization.
- **Returns**: A wrapper that either executes the action or raises a `PermissionError` if authorization fails.

### Return Messages by Function
- For `read`: Returns `"Data is: {data}"`.
- For `write`: Returns `"Data updated"`.
- For `delete`: Returns `"Data deleted"`.
- If authorization is denied: Returns `"Permission denied for {user_role} to perform {action} action."`

## Constraints
- \(1 \leq n \leq 50\)

## Input Format for Custom Testing
1. The first line is the number of user permission tests.
2. The user name and role, and the action type with detail, are repeated afterward.

## Sample Cases

### Sample Case 0

**Input:**
```
2
person1:admin
write:hello world 
person2:viewer
read
```
**Output:**
```
Data updated 
Data is: hello world
```

**Explanation:**
- The number of user permission tests is 2.
- The first user (`person1`) is an admin, and the action is to write.
- The second user (`person2`) is a viewer, and the action is to read.

### Sample Case 1

**Input:**
```
1
person1:viewer
delete:5
```

**Output:**
```
Permission denied for viewer to perform delete action
```

**Explanation:**
```
Here the user person1's role is viewer. The action is to delete the last 5 characters of data.
Permission is denied because only admins can delete text.
```

---------------------------------------------------------------------------------------------------------------------------------------------------------------
## @authorize
The @authorize is called a decorator in Python. It's a powerful design pattern that allows you to modify or enhance the behavior of functions or methods without directly changing their code.

- @authorize is a decorator that checks permissions before executing the actual method (read, write, or delete). Here's how it works:

The output file shows exactly what we expect from the test case:

1. First line "Data updated" - from when person1 (admin) wrote "hello world"
2. Second line "Data is: hello world" - from when person2 (viewer) read the data

This matches the expected behavior from the original requirements:
- For write operation returns: "Data updated"
- For read operation returns: "Data is: {data}"

Let's try another test case to verify other functionality. For example, try:
```
Enter number of operations: 1
Enter name:role: person1:viewer
Enter action (or action:detail): delete:5
```

This should produce a permission denied message in the output file since viewers can't delete data.

Or test the editor role:
```
Enter number of operations: 2
Enter name:role: person1:editor
Enter action (or action:detail): write:test
Enter name:role: person1:editor
Enter action (or action:detail): read
```


