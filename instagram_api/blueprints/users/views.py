from flask import Blueprint

users_api_blueprint = Blueprint('users_api',
                             __name__,
                             template_folder='templates')

# @users_api_blueprint.route('/', methods=['GET'])
# def index():
#     return "USERS API"



# [
#   {
#     "id": 1,
#     "username": "blake",
#     "profileImage": "http://next-curriculum-instagram.s3.amazonaws.com/idol2-blake.jpg"
#   },
#   {
#     "id": 2,
#     "username": "ryanG",
#     "profileImage": "http://next-curriculum-instagram.s3.amazonaws.com/idol1-ryan.jpg"
#   },
#   {
#     "id": 3,
#     "username": "bigfan",
#     "profileImage": "http://next-curriculum-instagram.s3.amazonaws.com/bigfan-9AE7468E-4C35-41D1-AA68-31939891B5E1.png"
#   }
# ]


# # Get all the users  (Select)
# # constrcut the dictionary that reprenents a user
# # returns all the dictionanrys in a list
# # convert the list into a JSON


# users = [
#     id
#     username
#     profileimage
# ]

# return jsonify(users=users), 

