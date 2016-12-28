bin/run.py
    Program entrance.
bin/GeneralSetting.py
    Add the path to os.path
conf/menu
    Menus
db:
    All accounts' information are in the folder. The informatin of admin is saved as XML, the others' information are
    saved as pickle.
modules:
    admin.py: The functions which are provided to admin to add teacher, student and unit accounts is in the file. It
    also provides a function to check the units' status.

    identify.py: This file is used to identify the login username and password.

    role: It includes the classes of all kinds of accounts. The functions for different types of accounts are also
    defined in the file.

    run: The main logic file.