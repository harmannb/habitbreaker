""" 
    Model File
    Habit Breaker - User Model
"""
from system.core.model import Model
import re


class User(Model):
    def __init__(self):
        super(User, self).__init__()

    """  User - Quotes  """
    
    # info about user by id
    def get_user_by_id(self, id):
        query_user = "SELECT * FROM users WHERE id = :id"
        data_user = {
            'id': id
        }
        return self.db.query_db(query_user, data_user)

    # info about user by email
    def get_user_by_email(self, email):
        query_user = "SELECT * FROM users WHERE email = :email"
        data_user = {
            'email': email
        }
        return self.db.query_db(query_user, data_user)

    def update_user(self, data):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # first name validation
        if not data['first_name']:
            errors.append('First name cannot be empty!')
        elif len(data['first_name'])<2:
            errors.append('First name should be at least 2 characters long')
        elif not data['first_name'].isalpha():
            errors.append('First name can contain only characters!')
        # last name validation
        if not data['last_name']:
            errors.append('Last name cannot be empty!')
        elif len(data['last_name'])<2:
            errors.append('Last name should be at least 2 characters long')
        elif not data['last_name'].isalpha():
            errors.append('Last name can contain only characters!')
        # email validation
        if not data['email']:
            errors.append('Email cannot be empty!')
        elif not EMAIL_REGEX.match(data['email']):
            errors.append('Email format must be valid!')
        if errors:
            return {'status': False, 'errors': errors}
        else:
            query_cur_user = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = :id"
            data_cur_user = {
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'email': data['email'],
                'id': data['id']
            }
            self.db.query_db(query_cur_user, data_cur_user)
            errors.append('You have successfully updated your account info!')
            query_email = "SELECT * FROM users WHERE email = :user_email LIMIT 1"
            data_email = {
                'user_email': data['email']
            }
            user = self.db.query_db(query_email, data_email)
            return {'status': True, 'errors': errors, 'user': user[0]}
    
    def update_password(self, data):
        errors = []
        # validate annd update password
        if not data['password']:
            errors.append('Password cannot be empty!')
        elif len(data['password'])<8:
            errors.append('Password must be at least 8 characters long!')
        elif data['password'] != data['conf_password']:
            errors.append('Password and confirmation must match!')

        if errors:
            return {'status': False, 'errors': errors}
        else:
            hashed_pass = self.bcrypt.generate_password_hash(data['password'])
            # query_cur_product = "UPDATE products SET name = :name, price = :price, description = :description, updated_at = NOW() WHERE id = :id"
            query_user = "UPDATE users SET password = :hashed_pass, updated_at = NOW() WHERE id = :id"
            data_user = {
                'hashed_pass': hashed_pass,
                'id': data['id']
            }
            self.db.query_db(query_user, data_user)
            errors.append('You have successfully updated your password!')
            return {'status': True, 'errors': errors}
    
    def delete_user(self,id):
        query_delete = "DELETE FROM users WHERE id = :id"
        data_delete = {
            'id': id
        }
        self.db.query_db(query_delete, data_delete)
        return True

    def show_helpers_by_habit_id(self,id):
        query = "SELECT users.id as helper_id, concat(users.first_name, ' ', users.last_name) as helper_name , users.email as helper_email  FROM users  WHERE users.id in ( SELECT helpers.helper_id FROM helpers WHERE habit_id = :id);"
        data = {
            'id': id
        }
        return self.db.query_db(query, data)

    def add_user_fb(self, data):
        query_email = "SELECT * FROM users WHERE email = :user_email LIMIT 1"
        data_email = {
            'user_email': data['email']
        }
        email_check = self.db.query_db(query_email, data_email)
        errors =[]
        if len(email_check)==0:
            query_user = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES(:first_name, :last_name, :email, NOW(), NOW())"
            data_user = {
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'email': data['email']
            }
            self.db.query_db(query_user, data_user)

            # users = self.db.query_db(query_email, data_email)
            return {'status': True, 'user': email_check[0]}
        else:
            
            # users = self.db.query_db(query_email, data_email)
            return {'status': True, 'user': email_check[0]}

        





