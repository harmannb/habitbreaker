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
            return {'status': True, 'errors': errors}
        

    def update_product(self, data):
        errors=[]
        if not data['name']:
            errors.append('Name of a new product cannot be empty!')
        elif len(data['name'])>255:
            errors.append('Name of the product cannot be longer than 255 characters!')
        if not data['description']:
            errors.append('Description of a new product cannot be empty!')
        elif len(data['description'])>255:
            errors.append('Description of the product cannot be longer than 255 characters!')
        if not data['price']:
            errors.append('A new product should have a price!')
        if not is_number(data['price']):
            errors.append('Price should be a number!')
        if not data['description']:
            errors.append('Please give some description!')
        if len(data['description'])>255:
            errors.append('Please make sure the product description is less than 255 characters!')
        if errors:
            return {'status': False, 'errors': errors}
        else:
            query_cur_product = "UPDATE products SET name = :name, price = :price, description = :description, updated_at = NOW() WHERE id = :id"
            data_cur_product = {
                'name': data['name'],
                'price': data['price'],
                'description': data['description'],
                'id': data['id']
            }
            self.db.query_db(query_cur_product, data_cur_product)
            errors.append('You have successfully updated a product!')
            return {'status': True, 'errors': errors}
