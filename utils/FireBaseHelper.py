import pyrebase
import random


class UserExcept(Exception):
    pass


class ConnectionExcept(Exception):
    pass


config = {
    'apiKey': "AIzaSyB6G4YjrKMSkJl_h58aE_eb307SPumSRyQ",
    'authDomain': "cleverproductionpytorial.firebaseapp.com",
    'projectId': "cleverproductionpytorial",
    'databaseURL': 'https://cleverproductionpytorial-default-rtdb.firebaseio.com/',
    'storageBucket': "cleverproductionpytorial.appspot.com",
    'messagingSenderId': "1078729198626",
    'appId': "1:1078729198626:web:707b3b1da05a4c8dd48e7b",
    'measurementId': "G-5RLJL76Y7V"
}
firebase = pyrebase.initialize_app(config)
pytorial_storage = firebase.database()


def convert_base(num, to_base=10, from_base=10):
    try:
        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < to_base:
            return alphabet[n]
        else:
            return convert_base(n // to_base, to_base) + alphabet[n % to_base]
    except Exception as e:
        print(e)
        raise ConnectionExcept


def new_user(nickname, email, password):
    try:
        us = set()
        for i in pytorial_storage.child('PyTorialTables').child('Users').get().each():
            us.add(i.key())
        while True:
            rid = random.randint(1, 16777215)
            sid = convert_base(rid, to_base=16)
            if sid in us:
                continue
            data = {'Avatar': 0,
                    'CID': rid,
                    'Email': email,
                    'Nickname': nickname,
                    'Password': password,
                    'Pproger': False,
                    'Teacher': False}
            cours = {'BASE': 0,
                     'PRO': 0}
            pytorial_storage.child('PyTorialTables').child('Users').child(sid.rjust(6, '0')).set(data)
            pytorial_storage.child('PyTorialTables').child('Users').child(sid.rjust(6, '0')).child('Courses').set(cours)
            break
    except Exception as e:
        print(e)
        raise ConnectionExcept


def find_user_by_id(CID):
    try:
        data = list()
        for i in pytorial_storage.child('PyTorialTables').child('Users').child(str(CID).rjust(6, '0')).get().each():
            data.append(i.val())
        return data
    except Exception as e:
        print(e)
        raise ConnectionExcept


def find_user_by_email(email):
    try:
        for i in pytorial_storage.child('PyTorialTables').child('Users').get().each():
            if i.val()['Email'] == email:
                return find_user_by_id(i.key())
        return None
    except Exception as e:
        print(e)
        raise ConnectionExcept


def check_user_sign(email, password):
    try:
        data = find_user_by_email(email)
        if not data:
            raise UserExcept
        if data[5] == password:
            return data
        return False
    except Exception as e:
        print(e)
        raise ConnectionExcept


def get_user_progress(CID, course):
    try:
        cid = convert_base(CID, to_base=16)
        progress = 0
        for i in pytorial_storage.child(f'PyTorialTables/Users/{str(cid).rjust(6, "0")}/Courses/{course}/').get().each():
            if i.val() == 'Зачет':
                progress += 1
        return progress
    except Exception as e:
        print(e)
        return 0


def get_user_progress_one(CID, course, lesson):
    try:
        cid = convert_base(CID, to_base=16)
        return pytorial_storage.child(f'PyTorialTables/Users/{str(cid).rjust(6, "0")}/Courses/{course}/{lesson}').get().val()
    except Exception as e:
        print(e)
        raise ConnectionExcept


def update_progress(CID, course, lesson, new_progress):
    try:
        cid = convert_base(CID, to_base=16)
        data = {
            f'PyTorialTables/Users/{str(cid).rjust(6, "0")}/Courses/{course}/{lesson}': new_progress
        }
        pytorial_storage.update(data)
    except Exception as e:
        try:
            cid = convert_base(CID, to_base=16)
            data = {
                f'PyTorialTables/Users/{str(cid).rjust(6, "0")}/Courses/{course}/{lesson}': new_progress
            }
            pytorial_storage.set(data)
        except Exception as e:
            print(e)
            raise ConnectionExcept


def update_image(CID, new_image):
    try:
        cid = convert_base(CID, to_base=16)
        data = {
            f'PyTorialTables/Users/{str(cid).rjust(6, "0")}/Avatar': str(new_image)
        }
        pytorial_storage.update(data)
    except Exception as e:
        print(e)
        raise ConnectionExcept


def send_to_check(CID, course, lesson, text):
    try:
        cid = convert_base(CID, to_base=16)
        data = {
            f'PyTorialTables/Tests/{course}/{lesson}/{str(cid).rjust(6, "0")}': text
        }
        pytorial_storage.update(data)
    except Exception as e:
        try:
            cid = convert_base(CID, to_base=16)
            data = {
                f'PyTorialTables/Tests/{course}/{lesson}/{str(cid).rjust(6, "0")}': text
            }
            pytorial_storage.set(data)
        except Exception as e:
            print(e)
            raise ConnectionExcept


def get_lessons(course):
    try:
        data = list()
        for i in pytorial_storage.child('PyTorialTables').child('Tests').child(course).get().each():
            data.append(i.key())
        return data[:-1]
    except Exception as e:
        print(e)
        raise ConnectionExcept


def get_user_programs(course, lesson):
    try:
        data = dict()
        for i in pytorial_storage.child('PyTorialTables').child('Tests').child(course).child(lesson).get().each():
            data[i.key()] = i.val()
        return data
    except Exception as e:
        print(e)
        raise ConnectionExcept


def delete_program(course, lesson, CID):
    try:
        pytorial_storage.child('PyTorialTables').child('Tests').child(course).child(lesson).remove(CID)
    except Exception as e:
            print(e)
            raise ConnectionExcept