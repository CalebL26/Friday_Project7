# Friday_Project7

## Files that run sign up and sign in user interfaces. 

1. designFile.py: This file gives the user the ability to interact with the Nike website to sign up for an account. The user has to enter a valid email adress and the same password twice. The purpose of the two entry password is to make sure the user 100 percent knows what there password is. After entering correct info, information gets transported to a user.db file where the informatuin is stored for later use. 

2. users.db: Stores the info of the user such as email and password. Allows signInPage.py to work properly. 

3. signInPage.py: Allows user to sign into Nike account they created previously by pulling data from the database file. If incorrect login information it displays a red text telling you it's incorrect. Although, if correct displays green message of login successful. 
