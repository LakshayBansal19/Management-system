import mysql.connector
con=mysql.connector.connect(host='localhost',password='LAKSHAY@123',user='root',database='project')
cursor=con.cursor()
print('*'*114)
print(' '*45,'WELCOME TO THE BANK')
print(' '*43,'(First choice of trust)')
print('*'*114)

def open_account():
        QUERY='select ACCOUNT_NO FROM CUSTOMER_DETAILS'
        cursor.execute(QUERY)
        DATA=cursor.fetchall()
        a=cursor.rowcount
        ano1=105143000001
        if a>0:
            ano=DATA[-1][0]
            ano=ano+1
        else:
            ano=ano1
        name=input('Enter the name of the account holder:')
        fathers_name=input('Enter the Father\'s name of the account holder:')
        mothers_name=input('Enter the Mother\'s name of the account holder:')
        age=int(input('Enter the age of the account holder:'))
        gender=input('Enter the gender of the account holder:')
        mobile=int(input('Enter the mobile number of the account holder:'))
        marital_status=input('Enter the marital status of the account holder(Married/Unmarried):')
        state=input('Enter the state in which the account holder lives:')
        cash_deposit=int(input('Enter the cash to be deposited by the account holder:'))
        dob=input('Enter the date of birth of the account holder(yyyy-m-d):')
        query1='insert into customer_details values({},"{}","{}","{}",{},"{}",{},"{}","{}",{},"{}","{}")'.format(ano,name,fathers_name,mothers_name,age,gender,mobile,marital_status,state,cash_deposit,dob,'EXISISTING CUSTOMER')
        query2='insert into amount values({},"{}","{}","{}",{},"{}",{},"{}","{}",{},"{}")'.format(ano,name,fathers_name,mothers_name,age,gender,mobile,marital_status,state,cash_deposit,dob)
        cursor.execute(query1)
        con.commit()
        cursor.execute(query2)
        con.commit()
        print('account opened successfully...\nYour account no.',ano)
        main()
def show_customer_details():
        ano=int(input('enter account no.'))
        Query="select account_no from customer_details"
        cursor.execute(Query)
        dat=cursor.fetchall()
        for i in dat:
               if i[0]==ano:
                       query='select * from customer_details where ACCOUNT_NO={}'.format(ano)
                       cursor.execute(query)
                       data=cursor.fetchone()
                       print(data)
                       break
        else:
           print('Account not created')
        main()
def cash_withdrawal():
        ano=int(input('enter account no.'))
        Query="select account_no from customer_details"
        cursor.execute(Query)
        dat=cursor.fetchall()
        for i in dat:
               if i[0]==ano:
                       query="select balance from amount where account_no={}".format(ano)
                       cursor.execute(query)
                       data=cursor.fetchone()
                       cash=int(input('enter the cash to be withdrawn'))
                       if data[0]<cash:
                                   print('not enough cash available in account')
                                   main()
                       elif (data[0]-cash)<2000:
                                   print('Minimum required balance:2000')
                                   print('Balance left after cash withdrawan:',data[0]-cash)
                                   main()
                       else:
                            query1="update amount set balance={} where account_no={}".format((data[0]-cash),ano)
                            cursor.execute(query1)
                            con.commit()
                            print('Balance left:',data[0]-cash)
                            print('cash withdrawn')
                            main()
        else:
             print('Account not created')
             main()
        
def cash_deposit():
        ano=int(input('enter account no.'))
        Query="select account_no from customer_details"
        cursor.execute(Query)
        dat=cursor.fetchall()
        for i in dat:
               if i[0]==ano:
                       cash=int(input('enter the cash to be deposited'))
                       query="select balance from amount where account_no={}".format(ano)
                       cursor.execute(query)
                       data=cursor.fetchone()
                       query1="update amount set balance={} where account_no={}".format((data[0]+cash),ano)
                       cursor.execute(query1)
                       con.commit()
                       print('cash Deposited successfully')
                       print('New Balance:',(data[0]+cash))
                       main()
        else:
            print('Account not created')
            main()
def delete_account():
        ano=int(input('enter account no.'))
        Query="select account_no from customer_details"
        cursor.execute(Query)
        dat=cursor.fetchall()
        for i in dat:
               if i[0]==ano:
                       query='UPDATE CUSTOMER_DETAILS SET CUSTOMER_ACTIVITY="ATTRITED CUSTOMER" WHERE ACCOUNT_NO={}'.format(ano)
                       query1='delete from amount where account_no={}'.format(ano)
                       cursor.execute(query)
                       cursor.execute(query1)
                       con.commit()
                       print('Account deleted successfully')
                       main()
        else:
            print('Account not created')
            main()
def show_balance():
        ano=int(input('enter account no.'))
        Query="select account_no from customer_details"
        cursor.execute(Query)
        dat=cursor.fetchall()
        for i in dat:
               if i[0]==ano:
                       query='select CASH_DEPOSIT_INR from CUSTOMER_DETAILS where account_no={}'.format(ano)
                       query1='select balance from amount where account_no={}'.format(ano)
                       cursor.execute(query)
                       data=cursor.fetchone()
                       cursor.execute(query1)
                       data2=cursor.fetchone()
                       print('opening balance:',data[0])
                       print('current balance:',data2[0])
                       main()
        else:
            print('Account not created')
            main()
        
def main():
        print(' '*48,'PUBLIC PORTAL')
        print('MENU \n1:OPEN ACCOUNT \n2:SHOW CUSTOMET DETAILS \n3:CASH WITHDRAWAL \n4:CASH DEPOSIT \n5:SHOW BALANCE \n6:DELTE ACCOUNT \n7:EXIT')
        ch=int(input('Enter you choice'))
        if ch==1:
               open_account()
        elif ch==2:
                show_customer_details()
        elif ch==3:
                cash_withdrawal()
        elif ch==4:
                cash_deposit()
        elif ch==5:
                show_balance()
        elif ch==6:
                delete_account()
        elif ch==7:
                exit()
        else:
                print('wrong choice')
                main()
main()


        

        
    

    
        
    
