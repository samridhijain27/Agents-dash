#region Import
import pandas as pd
import sqlite3,sys
#endregion

#region Arguments
filepath = '/Users/samridhijain/Documents/Programming/Assignment/DataSet.csv'
dbfilepath = '/Users/samridhijain/Documents/Programming/Assignment/BCG_assignment/db.sqlite3'
#endregion

#region variables
con = cur = None
#endregion

#region Helper Methods
def populate_insurance(df):
    """Populate insurance table

    Args:
        df ([dataframe]): [csv file data]
    """
    
    for index, row in df.iterrows():
        query=r'insert into insurance_insurance values('
        query += str(row['Policy_id'])+',"'
        query += row['Fuel']+'","'
        query += row['VEHICLE_SEGMENT']+'",'
        query += str(row['Premium'])+','
        query += str(row['bodily injury liability'])+','
        query += str(row[' personal injury protection'])+','
        query += str(row[' property damage liability'])+','
        query += str(row[' collision'])+','
        query += str(row[' comprehensive'])+')'
        print(query)
        cur.execute(query)
    con.commit()

def populate_customer(df):
    """Populate customer table

    Args:
        df ([dataframe]): [csv file data]
    """
    count=0
    for index, row in df.iterrows():
        count +=1
        query=r'insert into insurance_customer values('
        query += str(count)+','
        query += str(row['Customer_id'])+',"'
        query += row['Customer_Gender']+'","'
        query += row['Customer_Income group']+'","'
        query += str(row['Customer_Region'])+'",'
        query += str(row['Customer_Marital_status'])+', 1)'
        
        # print(query)
        cur.execute(query)
    con.commit()
    print("Done for cust")

def populate_insurance_customer(df):
    """Populate insurance_customer table

    Args:
        df ([dataframe]): [csv file data]
    """
    count=0
    for index, row in df.iterrows():
        count +=1
        query=r'insert into insurance_customer_insurance values('
        query += str(count)+',"'
        
        data= row['Date of Purchase'].strip().split(r'/')
        month=data[0]
        i_date=data[1]
        if(len(month) == 1):
            month = f'0{month}'
        if len(i_date) ==1:
            i_date=f'0{i_date}'    
        date_of_purchase=f'{data[2]}-{month}-{data[1]}'
        query += date_of_purchase+'",'
        query += str(row['Customer_id'])+','
        query += str(row['Policy_id']) + ')'
        
        cur.execute(query)
    con.commit()
    print("Done for cust_ins")
#endregion

#region Main
if __name__=='__main__':
    try:
        con = sqlite3.connect(dbfilepath)
        cur = con.cursor()
        print(cur)
        df = pd.read_csv(filepath)
       # populate_insurance(df)    
       # populate_customer(df)
        populate_insurance_customer(df)
    except Exception as ex:
        print(ex)
    finally:
        con.close()
#endregion
