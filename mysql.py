import pymysql

con = pymysql.connect('localhost', 'root',
                      'Ostanivkanavadime78328z', 'debts')
print('Для просмотра базы данных введите "просмотр". '
      'Для редактирования введите "редактировать"')
act = input()
if act == "просмотр":
    def view(con):
        print('Для просмотра всех студентов введите "все", '
              'для просмтора конкретного студента введите "поиск студента"')
        entry = input()
        if entry == 'поиск студента':
            print('Введите фамилию студента.')
            surname = input()
            a = "SELECT students.MarkBookNumber, surname, name, debts.namedebt, debts.subjectname " \
            "FROM students, debts WHERE students.MarkBookNumber = debts.MarkBookNumber and surname = " + "'" + surname + "'"
            cur1 = con.cursor()
            cur1.execute(a)
            rows1 = cur1.fetchall()
            for row1 in rows1:
                print("{0} {1} {2} {3} {4} {5} {6}".format(row1[0], row1[1], row1[2], '-', row1[3], '-', row1[4]))
        elif entry == "все":
            с = "SELECT students.MarkBookNumber, surname, name, debts.namedebt, debts.subjectname " \
            "FROM students, debts WHERE students.MarkBookNumber = debts.MarkBookNumber"
            cur2 = con.cursor()
            cur2.execute(с)
            rows2 = cur2.fetchall()
            for row2 in rows2:
                print("{0} {1} {2} {3} {4} {5} {6}".format(row2[0], row2[1], row2[2], '-', row2[3], '-', row2[4]))
        else:
            print('Вы ввели что-то не то.')
    view(con)
elif act == 'редактировать':
    def edit(con):
        print("Для того, чтобы добавить долг студенту введите 'поиск студента', "
              "чтобы добавить нового студента введите 'добавить', \n"
              "для того, чтобы изменить имеющуюся информацию введите 'изменить',\n"
              "для того, чтобы удалить студента или удалить долг введите 'удалить'"
              "(примечание: если удаляется последний долг, то с ним удалиться и студент) ")
        ans = input()
        if ans == 'добавить':
            print('Введите номер зачетной книжки, фамилию, имя, описание долга, предмет.'
                  ' (вводить через enter)')
            markbooknumber = input()
            surname = input()
            name = input()
            namedebt = input()
            subject = input()
            cursor = con.cursor()
            cursor1 = con.cursor()
            sql = "INSERT INTO students (MarkBookNumber, surname, name) values (" + "'" + markbooknumber + "'" + ", " + "'" \
              + surname + "'" + ", " + "'" + name + "'" + ");"
            sql1 = "INSERT INTO debts (namedebt, MarkBookNumber, subjectname) values(" + "'" + namedebt + "'" + ", " + "'" \
              + markbooknumber + "'" + ", " + "'" + subject + "'" + ");"
            cursor.execute(sql)
            cursor1.execute(sql1)
            con.commit()
        elif ans == 'поиск студента':
            print("Введите номер зачетной книги студента")
            markbooknumber = input()
            print('Введите описание долга и предмет(через enter)')
            namedebt = input()
            subject = input()
            cursor3 = con.cursor()
            sql3 = "INSERT INTO debts (namedebt, MarkBookNumber, subjectname) values(" + "'" + namedebt + "'" + ", " + "'" \
                   + markbooknumber + "'" + ", " + "'" + subject + "'" + ");"
            cursor3.execute(sql3)
            con.commit()

        elif ans == 'удалить':
            print("Чтобы удалить долг введите 'долг',"
                  "чтобы удалить студента с долгами введите 'поиск студента'")
            delete = input()
            if delete == 'долг':
                print('Введите номер зачетки и описание долга(через enter)')
                markbooknumber = input()
                debt = input()
                cursor2 = con.cursor()
                sql2 = "Delete from debts where MarkBookNumber = " + "'" + markbooknumber + "' " + 'and namedebt = ' + \
                       "'" + debt + "'"
                cursor2.execute(sql2)
                con.commit()
            elif delete == 'поиск студента':
                print('Введите фамилию студента.')
                surname = input()
                SQL = "SELECT * FROM students WHERE surname = " + "'" + surname + "'"
                cursor5 = con.cursor()
                cursor5.execute(SQL)
                rows = cursor5.fetchall()
                for row in rows:
                    markbooknumber = ("{0}".format(row[0]))
                cursor6 = con.cursor()
                sql6 = "Delete from debts where MarkBookNumber = " + "'" + markbooknumber + "' "
                cursor6.execute(sql6)
                con.commit()
                cursor4 = con.cursor()
                sql4 = "Delete from students where surname = " + "'" + surname + "' "
                cursor4.execute(sql4)
                con.commit()
            else:
                print('Вы ввели что-то не то.')
        elif ans == 'изменить':
            print('Введите фамилию студента у которого хотите изменить данные.')
            surname = input()
            print('Что вы хотите изменить "фамилия", "имя"')
            change = input()
            if change == 'фамилия':
                print('Введите новую фамилию.')
                newsurname = input()
                SQL = "SELECT * FROM students WHERE surname = " + "'" + surname + "'"
                cursor = con.cursor()
                cursor.execute(SQL)
                rows = cursor.fetchall()
                for row in rows:
                    prevmarkbooknumber = ("{0}".format(row[0]))
                cursor = con.cursor()
                sql = "UPDATE students SET surname = '" + newsurname + "'" + \
                      "WHERE MarkBookNumber = '" + prevmarkbooknumber + "'"
                cursor.execute(sql)
                con.commit()
            elif change == 'имя':
                print('Введите новое имя.')
                newname = input()
                cursor = con.cursor()
                sql = "UPDATE students SET name = '" + newname + "'" + \
                      "WHERE surname = '" + surname + "'"
                cursor.execute(sql)
                con.commit()
            else:
                print('Вы ввели что-то не то.')
        else:
            print('Вы ввели что-то не то.')
    edit(con)
con.close()


