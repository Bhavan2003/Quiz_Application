import mysql.connector as db
con = db.connect(user='root',password = 'Bhavan@2003',host='127.0.0.1',database = 'application')
cur = con.cursor()

def add_question():
    que=input('enter the question:')
    opt1=input('option1:')
    opt2=input('option2:')
    opt3=input('option3:')
    opt4=input('option4:')
    ans=input('ans:')

    sql='insert into question(question,option1,option2,option3,option4,ans)values(%s,%s,%s,%s,%s,%s)'
    cur.execute(sql,(que,opt1,opt2,opt3,opt4,ans))
    con.commit()
    print('Question Added')


def modify_question():
    while True:
        print('if you want to update only question then choice:1\nor all\nchoice:2\nfor exit \nchoice:3')
        a=input('enter the choice:')
        if a=='1' or a=='2':
            qid=input('enter question id to modify:')
            new_q=input('enter new question:')
        if a=='2':
            opt1=input('option1:')
            opt2=input('option2:')
            opt3=input('option3:')
            opt4=input('option4:')
            ans=input('ans:')
        if a=='1':
            sql='update question set question=%s where qid=%s'
            cur.execute(sql,(new_q,qid))
            con.commit()
            print("question updated")
        if a=='2':
            sql='update question set question=%s,option1=%s,option2=%s,option3=%s,option4=%s,ans=%s where qid=%s'
            cur.execute(sql,(new_q,opt1,opt2,opt3,opt4,ans,qid))
            con.commit()
            print("question updated")
        if a=='3':
            break
        else:
            print('enter the correct option')
        
        



def delete_question():
    qid=input("enter the qid:")
    sql="delete from question where qid=%s"
    cur.execute(sql,(qid))
    con.commit()
    print('question deleted')
def view_questions():
    cur.execute('select * from question;')
    data = cur.fetchall()
    for i,j,k,l,m,n,y in data:
        print(i,'',j,)
        print('option1:',k,'','option2:',l,'','option3:',m,'','option4:',n)
        print('answer:',y)
        print('')
    
    

def view_user():
    cur.execute('select * from user;')
    data = cur.fetchall()
    for i,j in data:
        print('user_name:',i,'   ','phone_no:',j)

def admin():
    
    cur.execute('select * from admin;')
    data = cur.fetchall()
    while True:
        print('login choice:1\nexit choice:2')
        o1=input('enter the choice:')
        if o1=='1':
                a=input("Enter the admin_id:")
            
                b=input("enter the password:")
            

                c=0
                for i,j in data:
                    
                    if a==i and b==j:
                        print('sucessfully login')
                        
                        c=1
                        break
                if c!=1:
                    print('*'*4,'enter the login details correctly','*'*4)
                if c==1:
                    while True:
                        print("\nAdmin Menu:")
                        print('1.Add Question\n2.Modify Question\n3.Delete Question\n4.View all Questions\n5.View all User\n6.Back to Main Menu')
                        d=input('enter the option:')
                        if d=='1':
                            add_question()
                        elif d=='2':
                            modify_question()
                        elif d=='3':
                            delete_question()
                        elif d=='4':
                            view_questions()
                        elif d=='5':
                            view_user()
                        elif d=='6':
                            break
                        else:
                            print("Invalid option.Try again")
                            
                    

            #else:
                #print('enter the correct admin_id and password')
        elif o1=='2':
                break
            
                
        else:
                print('enter the correct admin_id and password')
def result(a,b,c):
    
    sql='insert into result(user_name,ph_no,result)values(%s,%s,%s)'
    cur.execute(sql,(a,b,c))
    con.commit()
def top3_results():
    sql = 'SELECT user_name, ph_no, result FROM result ORDER BY result DESC LIMIT 3'
    cur.execute(sql)
    data = cur.fetchall()

    print("\n Top 3 Results ")
    for i, row in enumerate(data, start=1):
        username, ph_no, score = row
        print(f"{i}. {username} ({ph_no}) --> Score: {score}")

    
                
            
def user():
    cur.execute('select * from user;')
    data = cur.fetchall()
    
    a=input('enter the user_name:')
    b=input("enter the phone number:")
    z=0
    for i,j in data:
        if a==i and b==j:
             print('sucessfully login')
             z=1
             break
    if z!=1:
        print('enter the correct login details')
            
    if z==1:
        while True:
            import time
            cur.execute('select * from question;')
            data = cur.fetchall()
            print("Do you want to ?\n ",('*'*5),"Take Quiz" ,('*'*5))
            print('1.Yes\n2.No')
            o=input('enter the choice:')
            if o=='1':
                c=0
                s=time.time()
                for i,j,k,l,m,n,ans in data:
                    print(i,'',j)
                    print('option1:',k,'','option2:',l,'','option3:',m,'','option4',n)
                    output=input('enter the option:')
                    if ans==output:
                        c=c+1
                        #print('c=',c)
                e=time.time()
                
                print(('*'*5),"result=",c,('*'*5))
                print(('#'*5),'Time taken:',round(e-s),'(in sec)',('#'*5))
                result(a,b,c)
                top3_results()
            elif o=='2':
                break
            else:
                print('enter the correct option')
   

def new():
    while True:
        print('You want to creat a new account enter 1 or 2')
        z1=input('enter the choice:')
        
        if z1=='1':
            a=input('enter the user_name:')
            b=input('enter the phone_number:')
            
            if len(b)==10 and b.isdigit() and b[0] in ['6','7','8','9']:
                sql="insert into user (user_name,ph_no) values(%s,%s)"
                cur.execute(sql,(a,b))
                con.commit()
                print("New user login created")
            else:
                print('enter phone number correctly')
        if z1=='2':
            break
    
    
    
    


while True:
    print("\n1.Admin\n2.User\n3.New User\n4.Exit")
    ch=input('enter the option:')
    if ch=='1':
        admin()
        
    elif ch=='2':
        user()
        
    elif ch=='3':
        new()
        
    elif ch=='4':
        print('*'*5,'EXIT','*'*5)
        break
        
    else:
        print('Enter the correct option')
cur.close()
con.close()
