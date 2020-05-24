from user import User
from admin import Admin, Privileges

privileges = Privileges('can add a post', 'can delete a post')
admin = Admin("Davi", "Carvalho", 23, privileges)
print(admin.privileges.show_privileges())