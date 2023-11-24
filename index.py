from flask import Flask, render_template
from db import (Person, Department, insert_person, get_person_by_id, update_user_name_by_id, delete_person_by_id, get_all_person)

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':

    #get person by id
    # data = get_person_by_id(2)
    # if(data != None):
    #     print('this is person have id = 2: ' + data.user_name)
    # else:
    #     print('data not exists!!!')

    #update person
    # update_user_name_by_id(2)

    #delete person
    # del_person = delete_person_by_id(2)

    #create person
    # new_person = insert_person(7, 'HoangAnhTu', 'tuhoanganh@gmail.com', 'Bc Giang', 'IT Comtor', 3)
    # print(new_person.user_name)

    #get all person
    list_person = get_all_person()
    for x in list_person:
        print(x.user_name)

    app.run(debug=True)