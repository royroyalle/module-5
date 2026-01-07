class Employee:
    def __init__(self):
        print('Employee Created')

    def __del__(self):
        print('Detructer called')

def Create_obj():
        print('Making Object')
        obj = Employee()
        print('function ended')
        return obj
print('calling create obj function')
obj = Create_obj()
print('Program end')

