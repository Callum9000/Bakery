import pandas as pd
from sqlalchemy import false

class account:
    #Temp create csv file or dictonary with data of names
    Name = "Steve"
    Address = "10 CloverField Lane"
    # add error checking for email
    Email =  "SteveCL@gmail.com"
    is_staff = false
    
def change_details():
    
    account.Email 