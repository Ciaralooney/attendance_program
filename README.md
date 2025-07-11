# Module Attendance Record Programme

The programme will allow a user do the following tasks

• Record the attendance of a student for a class session in a particular modules (present/absent)

• View statistical data about the average attendance of each module

The user will logon to the system with a username and password. Once the user has successfully logged on they will choose which task they wish to undertake.
If they choose to record attendance, they will be shown a list of modules and asked to choose a module. They will then be given an opportunity to mark each student enrolled as either present or absent. The system will update the relevant text file with this information.

## Statistics
If the user chooses to generate statistics the average attendance is calculated for each module. The following information is then displayed on the screen and written to a file.
1. The name, module code and the average attendance for every module.
2. A bar chart to illustrate the average attendance across modules.
3. The module with the best average attendance.
4. A list is displayed of all modules where the average attendance is below 40%.

The file name includes the current date

## Files Required
The following files will be required by the program

### Login
This stores the username and password for the user.
A sample ```login.txt``` file for a user named 'Ciara' with a password '12345' would be as follows
```
Ciara:12345
```
### Module
A file is needed to hold the details of the modules taught by one lecturer. Each line in the file has a module code and module name.

A sample file for ```module.txt``` would be as follows
```
SOFT_6018,Programming Fundamentals
SOFT_6017,Modular Programming
```
### Module Specific Files
Each module that is listed in modules.txt will have an associated file (e.g. SOFT_6017.txt)

Each line in the file has a student's name, number of days present and the number of absences. 
A sample ```SOFT_6017.txt``` file would be as follows
```
Mary Martin, 10,0
Alan Wilson, 9,1
Alan Lowe,5,5
```
