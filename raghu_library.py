# Extended library
import random
from twilio.rest import Client

password = 0
student_information = {} #{reg_no:{'Name': name, 'DOB': dob, 'Branch': branch, 'Mobile number': mobile, 'Requested Book Data': book_data_of_student, 'Returned Book Data': books_return_data, 'password': password}}
data = {}  # data={'your_name':{book_data:s.no}
return_data = {} 
list_of_books = {}
names = []  # list of names of students
books = []


def forget_password(your_reg_no):
    while(1):
        your_number=input('Enter the Registered Mobile number:')
        if your_number == student_information[your_reg_no]['Mobile number']:
            account_sid="AC88b93e3bda93cd8dc1b8abaef1731c7a"
            auth_token='2f3e4380b66e31fd5b02fa9ec03db2fd'
            client=Client(account_sid,auth_token)
            msg=client.messages.create(
                body="your password is %s."%student_information[your_reg_no]['password'],
                from_="+16208378238",
                to="+91%s."%your_number
            )
            break;
        else:
            print("Entered number is not correct.so,Please Enter the correct number")


def verification_otp(mobile):
    otp = random.randint(10000,99999)
    account_sid="AC88b93e3bda93cd8dc1b8abaef1731c7a"
    auth_token='2f3e4380b66e31fd5b02fa9ec03db2fd'
    client=Client(account_sid,auth_token)
    msg=client.messages.create(
        body="your OTP is %s."%otp,
        from_="+16208378238",
        to="+91%s."%mobile
    )
    return otp


def student_sign_in():
    global student_information, password, data
    while 1:
        print("-========== STUDENT SIGN IN ========-")
        book_data_of_student = {}
        books_return_data = {}
        reg_no = input('Enter Reg.No:')
        if reg_no not in student_information.keys():
            name = input('Enter Name:')
            dob = input('Enter DOB:')
            branch = input('Enter Branch:')
            mobile=input('Enter Mobile Numnber:')
            password = input("Enter Password:")
            confirm_password = input("Confirm Your password:")
            sended_otp=verification_otp(mobile)
            entered_otp=int(input('Enter the OTP:'))
            if(sended_otp == entered_otp):
                if (password == confirm_password):
                    student_data = {'Name': name, 'DOB': dob, 'Branch': branch, 'Mobile number': mobile, 'Requested Book Data': book_data_of_student, 'Returned Book Data': books_return_data, 'password': password}
                    dict1 = student_information
                    dict2 = {reg_no: student_data}
                    student_information = dict1 | dict2
                    print("Sign in completed")
                    opt = input("Want to Log in(yes/no):")
                    if opt == "yes":
                        student_info()
                        break
                    else:
                        break
                else:
                    print("Please Make Sure that your password and Confirm password should be same")
            else:
                print("Entered OTP is Not correct")
        else:
            print("Your are already Registered")
            break


def student_info():
    global list_of_books, student_information, password, data, names, books
    print("-========== LOGGED IN PAGE =========-")
    your_reg_no = input("Enter your Reg.No:")
    if your_reg_no in student_information.keys():
        fp=input('Did you remember your password(yes/no):')
        if(fp=='no'):
            forget_password(your_reg_no);
        pwd = input("Enter your Password:")
        if pwd == student_information[your_reg_no]['password']:
            print("Student Name:", student_information[your_reg_no]['Name'])
            print("Date of Birth:", student_information[your_reg_no]['DOB'])
            print("Branch:", student_information[your_reg_no]['Branch'])
            print("Mobile Number:", student_information[your_reg_no]['Mobile number'])
            print("Books Requested:", student_information[your_reg_no]['Requested Book Data'])
            print("Books Returned:", student_information[your_reg_no]['Returned Book Data'])
            opt = input("Want to Know about Books in Library(yes/no):")
            if opt == "yes":
                home_f()
            else:
                main_f()
        else:
            print("Enter Correct Password")
            main_f()
    else:
        print("Please Sign In")
        main_f()


def home_f():
    global list_of_books, student_information, password, data, names, books
    print('-========== LIBRARY HOME ===========-')
    print('1.List of Books Available')
    print('2.Requesting Books')
    print('3.Returning Books')
    print('4.Add Books to Library')
    print('5.Books issued data')
    print('6.check weather we issued any books to you')  # search by student name
    print('7.Check weather the book is in library')  # search books
    print('8.Attendance')
    print('9.Exit')
    while 1:
        try:
            print('-------------------------------')
            choice = int(input('Enter your choice:'))
            if choice == 1:  # To check list of books
                print('Number of Subjects of Books Available:', len(list_of_books))
                for book in list_of_books:
                    print('-->', book, ':', len(list_of_books[book]), '\tand \ts.no:', list_of_books[book])
            elif choice == 2:  # requesting books
                your_reg_no = input('Enter your Reg.No.:')
                if your_reg_no in student_information.keys():
                    no_of_books = int(input('Enter number of books you need:'))
                    for i in range(1, no_of_books + 1):
                        book_name = input('Enter the name of the Book:')
                        if book_name in list_of_books.keys() and book_name not in student_information[your_reg_no]['Requested Book Data'].keys():
                            print('s.no:', list_of_books[book_name])
                            number = input('Enter which s.no book you want:')
                            if number in list_of_books[book_name]:            
                                print(book_name, 'with s.no', number, ' are issued to ', your_reg_no)
                                list_of_books[book_name].remove(number)
                                names.append(your_reg_no)
                                books.append(book_name)
                                if your_reg_no not in data.keys():
                                    data[your_reg_no] = {book_name: number}
                                else:
                                    dict1 = data[your_reg_no]
                                    dict2 = {book_name: number}
                                    data[your_reg_no] = dict1 | dict2
                                student_information[your_reg_no]['Requested Book Data'] = data[your_reg_no]
                            else:
                                print(number, "is not in series of ", book_name)
                        else:
                            print(book_name, "is already allocated to you with serial number", data[your_reg_no][book_name])
                            print("       OR          ")
                            print(book_name, 'is not available or it is taken by someone or please wait until he return')
                else:
                    print("Please Sign In")
            elif choice == 3:  # returning books
                your_reg_no = input('Enter your Reg.No.:')
                if your_reg_no in data.keys():
                    no_of_books = int(input('Enter number of books you want to return:'))
                    if len(data[your_reg_no]) >= no_of_books:
                        for i in range(1, no_of_books + 1):
                            book_name = input('Enter the name of the Book:')
                            if book_name in data[your_reg_no].keys():
                                number = input('Enter the series number:')
                                if number == data[your_reg_no][book_name]:
                                    print(book_name, 'with series number', number, 'is returned by', your_reg_no)
                                    list_of_books[book_name].append(number)
                                    if your_reg_no not in return_data.keys():
                                        return_data[your_reg_no] = {book_name: number}
                                    else:
                                        dict1 = return_data[your_reg_no]
                                        dict2 = {book_name: number}
                                        return_data[your_reg_no] = dict1 | dict2
                                    student_information[your_reg_no]['Returned Book Data'] = return_data[your_reg_no]
                                    del data[your_reg_no][book_name]
                                    books.remove(book_name)
                                    if len(data[your_reg_no]) == 0:
                                        data.pop(your_reg_no)
                                else:
                                    print("your are Returning wrong books")
                                    print(book_name, "with serial number", data[your_reg_no][book_name],
                                          "is allocated to you.")
                                    print(number, "is returned by you which is NOT ACCEPTED")
                            else:
                                print(book_name, "is not allocated to you")
                                print(data[your_reg_no], "is allocated to you")
                    else:
                        print("you mentioned more then the books we allocated to you")
                else:
                    print("No books are allocated to", your_reg_no)
            elif choice == 4:  # Appending Books into Library
                no_of_books = int(input('Enter number of subject of books you want to donate:'))
                for i in range(1, no_of_books + 1):
                    book_name = input('Enter the name of the Book:')
                    number = list(map(str, input("Enter the series number separate with ',':").split(',')))   
                    if book_name in list_of_books:
                        for num in number:
                            list_of_books[book_name].append(num)
                    else:
                        sno = []
                        for j in number:
                            sno.append(j)
                        list_of_books[book_name] = sno
                    print(book_name, "is added in the list of books")
            elif choice == 5:  # Data Analysis
                print("Number of books are issued:", len(books))
                if len(data) != 0:
                    for your_reg_no in data:
                        print(data[your_reg_no], 'is issued to', your_reg_no)
                else:
                    print('No books are issued')
            elif choice == 6:
                your_reg_no = input("Enter your Reg.No.:")
                if your_reg_no in data.keys():
                    print("we have issued", len(data[your_reg_no]), "books to you")
                    print(data[your_reg_no])
                else:
                    print(your_reg_no, "is not in list of students")
                    print("NO books are issued to you")
            elif choice == 7:
                book_name = input("Enter the book name:")
                if book_name in list_of_books:
                    print("yes", book_name, "books are available in library")
                    print("Number of", book_name, "books available:", len(list_of_books[book_name]))
                else:
                    print("Sorry,", book_name, "books are not available in library")
            elif choice == 8:
                print("Number of Students Attended:", len(set(names)))
                if len(names) != 0:
                    print("List of Students:")
                    names = set(names)
                    for i in names:
                        print(i)
                    names = list(names)
                else:
                    print("No student is attend to Library")
            elif choice == 9:
                print('Exited')
                break
            else:
                print('Invalid Choice')
        except Exception as e:
            print(e, "is the exception")


def delete_account():
    print("-========= DELETE ACCOUNT =======-")
    while 1:
        your_reg_no = input("Enter your Reg.No:")
        if your_reg_no in student_information.keys():
            pwd = input("Enter your password:")
            if pwd == student_information[your_reg_no]['password']:
                con = input("Are you Sure,You want to Delete your Account(yes/no)")
                if con == "yes":
                    del student_information[your_reg_no]
                    print("YOUR ACCOUNT IS DELETED SUCCESSFULLY")
                    break
                else:
                    print("Your Account is not Deleted")
                    break
        else:
            print("YOU ARE ALREADY DELETED YOUR ACCOUNT OR YOU ARE NOT SIGNED IN")
            break


def main_f():
    global list_of_books, student_information, password, data, names, books
    print("-======= MAIN FUNCTION ========-")
    print('1.Signin')
    print('2.Login')
    print('3.Library Home')
    print('4.Delete your Account')
    print("5.Exit")
    try:
        choice = int(input("Enter your Choice:"))
        if choice == 1:  # Student Sign in
            student_sign_in()
        elif choice == 2:  # Student login
            student_info()
        elif choice == 3:  # home_f()
            home_f()
        elif choice == 4:  # Delete an existing account
            delete_account()
        elif choice == 5:  # exit or Terminates the program
            exit()
        else:
            print('Enter Correct value')
    except Exception as e:
        print(e, "is the exception")


# main function
print('\t-=========WELCOME TO RAGHU ENGINEERING COLLEGE LIBRARY========-')
try:
    while 1:
        main_f()
except Exception as E:
    print(E, "is the exception")