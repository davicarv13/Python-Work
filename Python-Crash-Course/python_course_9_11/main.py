from users import User, Privileges, Admin

privileges = Privileges('can add a post', 'can delete a post')
admin = Admin("Davi", "Carvalho", 23, privileges)
print(admin.privileges.show_privileges())