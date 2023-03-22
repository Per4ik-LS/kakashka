from flask import jsonify
from flask_restful import Resource, abort
from sqlalchemy import select, delete
from data import db_session
from data.users import User
from data.user_request_parser import user_parser
class UserResource(Resource):
    def get(self, user_id):
        self.abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        fields = 'id', 'name', 'surname', 'age', 'address', 'email', 'position', 'speciality'
        return jsonify({
            'user': user.to_dict(only=fields),        })
    def delete(self, user_id):
        self.abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({
            'success': 'OK',        })
    def abort_if_user_not_found(self, user_id):
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        if not users:
            abort(404, message=f"User {user_id} not found")

class UserListResource(Resource):
    def get(self):
        session = db_session.create_session()
        result = session.execute(
            select(User)
        )
        users = result.all()
        fields = 'id', 'name', 'surname', 'age', 'address', 'email', 'position', 'speciality'
        users_dict = [user.to_dict(only=fields) for user, in users]
        return jsonify({
            'users': users_dict,
        })
    def post(self):
        args = user_parser.parse_args()
        session = db_session.create_session()
        user = User(
            name=args['name'],
            surname=args['surname'],
            age=args['age'],
            address=args['address'],
            email=args['email'],
            position=args['position'],
            speciality=args['speciality'],
        )
        user.set_password(args['password'])
        session.add(user)
        session.commit()
        return jsonify({
            'success': 'OK',        })