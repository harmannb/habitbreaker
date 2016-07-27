""" 
    Sample Model File
    Habit Breaker - Main Model
"""
from system.core.model import Model
import re

class Main(Model):
    def __init__(self):
        super(Main, self).__init__()

    """  Log In - Registration  """
   
    # validation check and inserting new user into database
    def validate_add_user(self, data):
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

        # move to separate form
        #if not data['phone_number']:
        #    errors.append('Phone_number cannot be empty!')
        # elif not data['phone_number'].isdigit():
        #     errors.append('Phone number format must be valid!')

        # password validation
        if not data['password']:
            errors.append('Password cannot be empty!')
        elif len(data['password'])<8:
            errors.append('Password must be at least 8 characters long!')
        elif data['password'] != data['conf_password']:
            errors.append('Password and confirmation must match!')

        if errors:
            return {'status': False, 'errors': errors}
        else:
            # validation passed, inserting the info
            query_email = "SELECT * FROM users WHERE email = :user_email LIMIT 1"
            data_email = {
                'user_email': data['email']
            }
            email_check = self.db.query_db(query_email, data_email)
            if len(email_check)==0:
                hashed_pass = self.bcrypt.generate_password_hash(data['password'])
                query_user = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name, :last_name, :email, :hashed_pass, NOW(), NOW())"
                data_user = {
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                    'email': data['email'],
                    'hashed_pass': hashed_pass
                }
                self.db.query_db(query_user, data_user)
                # retrieve the last inserted user by email
                users = self.db.query_db(query_email, data_email)
                return {'status': True, 'user': users[0]}
            else:
                errors.append('This email in use already!')
                return {'status': False, 'errors': errors}
            
    def validate_log_user(self, data):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # email validation
        if not data['email']:
            errors.append('Email cannot be empty!')
        
        # password validation
        if not data['password']:
            errors.append('Password cannot be empty!')
        
        if errors:
            return {'status': False, 'errors': errors}
        else:
            query_email = "SELECT * FROM users WHERE email = :user_email LIMIT 1"
            data_email = {
                'user_email': data['email']
            }
            user_curr = self.db.query_db(query_email, data_email)
            
            if len(user_curr)==1:
                if self.bcrypt.check_password_hash(user_curr[0]['password'], data['password']):
                    return {'status': True, 'user': user_curr[0]}
                else:
                    errors.append('Password is not matching!')
                    return {'status': False, 'errors': errors}
            else:
                errors.append('Email is not matching!')
                return {'status': False, 'errors': errors}

    