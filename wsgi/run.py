import os
from flask import Flask
from flask import render_template
from flask import request
import pymongo
import backend
import mongoFunctions

data_dir = "./"
#data_dir = os.environ['OPENSHIFT_DATA_DIR']
#mongo_con = pymongo.Connection(os.environ['OPENSHIFT_MONGODB_DB_HOST'],
#                               int(os.environ['OPENSHIFT_MONGODB_DB_PORT']))

#mongo_db = mongo_con[os.environ['OPENSHIFT_APP_NAME']]
#mongo_db.authenticate(os.environ['OPENSHIFT_MONGODB_DB_USERNAME'],
#                      os.environ['OPENSHIFT_MONGODB_DB_PASSWORD'])


app = Flask(__name__)
images = ['d','s']

#Create our index or root / route
@app.route("/")
def index():
    return render_template("index.html")

<<<<<<< HEAD
def clean(img):
    return ''.join(''.join((img.split('.')[3]).split('\\')).split('/')) + '.' +  img.split('.')[4]

@app.route('/stumbl', methods=['POST', 'GET'])
def stumbl():
    mongoFunctions.insert_user(25, {})
    url = backend.getUrl({"Guitar": 5, "Pennapps": 20, "Shred": 6, "HackRU": 2}, 25)
=======

@app.route('/stumbl', methods=['POST', 'GET'])
def stumbl():
    url, img = backend.getNextUrl()
    pullFile(data_dir, img, '1827130080', 'blah')
>>>>>>> parent of 0e4504c... this should work
    return render_template('stumbl.html', url = url)
    # url, img = backend.getNextUrl()
    # f = clean(img)
    # images.append(f)
    # backend.pullFile(data_dir, img, '1827130080', f)
    # return render_template('stumbl.html', url = url)


# @app.route('/movie', methods=['POST', 'GET'])
# def movie():
#     backend.makeMovie(data_dir, images)
#     return "<html> movie right here</html>"

@app.route('/like', methods=['POST', 'GET'])
def like():
    return

@app.route('/dislike', methods=['POST', 'GET'])
def dislike():
    return

@app.route('/favorites', methods=['POST', 'GET'])
def favorites():
    return


@app.route('/test', methods=['POST', 'GET'])
def test():
	return render_template('test.html')


@app.route('/dropbox', methods=['POST', 'GET'])
def movie():
    
    return "<html> movie right here</html>"


@app.route("/submit", methods=["GET", "POST"])
def getUser():
    f = open('%s/blah' % data_dir, 'w')
    r = request.form['userID']
    f.write(r)
    r = request.form['accessToken']
    f.write('\n')
    f.write(r)
    f.close()
    return render_template("index.html")


@app.route("/tutorial", methods=["GET", "POST"])
def tutorial():
    notes = [{ "name": "First Note Ever",
              "author":"Angel",
              "content":"This text is coming from the content field"
               },
             { "name":"Finish this blog",
              "author":"Angel",
              "content":"Show the template control structures"
               },
             { "name":"Deploy this shit",
              "author":"Angel",
              "content":"When finished, this is the stuff"
               },

             ]
    return render_template("index.html", notes = notes)


# Mongo DB functions

# def user_find(userid):
#     if not userid: return None
#     return mongo_db.users.find_one({ '_id': userid})

# def user_create(username, password):
#     if not username: return None
#     # check for pre existance
#     tuser = user_find(username)
#     if tuser: return None

#     nuser = {
#         '_id': username,
#         'pw': password,
#         'follower': [ ],
#         'followee': [ ],
#         'timeline': [ ],
#         'posts': [ ],
#         }
#     userid = mongo_db.users.insert(nuser)
#     return userid

# def user_list():
#     l = []
#     for u in mongo_db.users.find():
#         l.append(u['_id'])
#     l.sort()
#     return l

# def user_follow(user, tuser):
#     user['followee'].append(tuser['_id'])
#     mongo_db.users.update({ '_id': user['_id']}, user)
#     tuser['follower'].append(user['_id'])
#     mongo_db.users.update({ '_id': tuser['_id']}, tuser)
#     return

# def user_unfollow(user, tuser):
#     if tuser['_id'] in user['followee']:
#         user['followee'].remove(tuser['_id'])
#     mongo_db.users.update({ '_id': user['_id']}, user)
#     if user['_id'] in tuser['follower']:
#         tuser['follower'].remove(user['_id'])
#     mongo_db.users.update({ '_id': tuser['_id']}, tuser)
#     return



if __name__ == "__main__":
    app.run(debug = "True")
