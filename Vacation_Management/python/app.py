import json
import hashlib
import webbrowser
from flask import Flask, request, Response, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

from model import Employee, Request

app = Flask(__name__)


@app.route('/')
def login():
    return Response({'redirect_to': access()}, mimetype='application/json')


def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username is None or password is None:
        return Response("{'error':'unauthorized'}", status=403, mimetype='application/json')

#check user's role and open the matching page   
def access():
    access = request.form.get('role')
    if access is 'admin':
        url = "file://frontend/admin.html"
    if access is 'employee':
        url = "file://frontend/employee.html"
    else:
        url = "file://frontend/viewer.html"

    #return redirect(url)
    return url
    
@app.route('/user')
def show_user():
    try:
        #user = User.query.filter_by(id=request.args['userid'])
        #return Response(json.dumps({user.username: {'email': user.email, 'phone': user.status, 'fax': user.username}}), mimetype='application/json')
        return Response(json.dumps({'admin': {'email': 'admin@gmail.hu', 'status': 'accepted', 'role': 'admin'}}), mimetype='application/json')
    except IntegrityError:
        return json.dumps({})


@app.route('/users')
def users():
    try:
        # users = User.query.all()
        # users_dict = {}
        # for user in users:
        #     users_dict[user.username] = {
        #         'id': user.id,
        #         'email': user.email,
        #         'status': user.status,
        #         'role': user.role
        #     }

        users_dict = {}
        users_dict['Senator Palpatine'] = {
            'id': 0,
            'email': 'palpatine@gmail.com',
            'status': 'accepted',
            'role': 'admin'
        }
        users_dict['Robert Burns'] = {
            'id': 1,
            'email': 'mrbruns@gmail.com',
            'status': 'accepted',
            'role': 'admin'
        }
        users_dict['Homer Simpson'] = {
            'id': 2,
            'email': 'homer@gmail.com',
            'status': 'accepted',
            'role': 'employee'
        }
        users_dict['Marge Simpson'] = {
            'id': 3,
            'email': 'marge@gmail.com',
            'status': 'accepted',
            'role': 'employee'
        }
        users_dict['Eric Cartman'] = {
            'id': 4,
            'email': 'eric@gmail.com',
            'status': 'accepted',
            'role': 'viewer'
        }
        users_dict['Kenny McCormic'] = {
            'id': 5,
            'email': 'kenny@gmail.com',
            'status': 'accepted',
            'role': 'viewer'
        }

        return Response(json.dumps(users_dict), mimetype='application/json')
    except IntegrityError:
        return json.dumps("", status=503, mimetype='application/json')

    
#Get employers' data and display it on the frontend
#return render_template("admin.html", name="")


#Delete an entry from database   
# $.ajax({
#     type:"DELETE",
#     url:"delete_script.php",
#     data: "userid=1",
#     success: function(msg){
#         alert("Data Deleted: " + msg);
#     }
# });

@app.route('/requests')
def requests():
    try:
        # requester_id = request.args.get('userid')
        # requests_list = []
        # if requester_id is not None:
        #     requests = Request.query.filter_by(requester=requester_id)
        #     for req in requests:
        #         requests_list.append({
        #             'id': req.id,
        #             'start_date': req.start_date,
        #             'end_date': req.end_date,
        #             'status': req.status
        #         })
        requests_list = []
        requests_list.append({
            'id': 0,
            'start_date': '20.06.2018',
            'end_date': '30.06.2018',
            'status': 'approved'
        })
        requests_list.append({
            'id': 1,
            'start_date': '01.09.2018',
            'end_date': '03.09.2018',
            'status': 'approved'
        })
        requests_list.append({
            'id': 2,
            'start_date': '07.11.2018',
            'end_date': '13.11.2018',
            'status': 'approved'
        })
        requests_list.append({
            'id': 3,
            'start_date': '11.12.2018',
            'end_date': '20.12.2018',
            'status': 'pending'
        })
        requests_list.append({
            'id': 4,
            'start_date': '07.11.2018',
            'end_date': '13.11.2018',
            'status': 'pending'
        })

        return Response(json.dumps(requests_list), mimetype='application/json')
    except IntegrityError:
        return json.dumps("", status=503, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
