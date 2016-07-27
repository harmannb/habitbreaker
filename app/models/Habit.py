""" 
    Model File
    Habit Breaker - Habit Model
"""
from system.core.model import Model
import re


class Habit(Model):
    def __init__(self):
        super(Habit, self).__init__()

    def get_habits_by_user_id(self, id):
        query_habits = "SELECT * FROM habits WHERE holder_id = :myid"
        data_user = {
            'myid' : id
        }
        return self.db.query_db(query_habits, data_user)
    
    def show_habit_by_id(self, id):
        query_habit = "SELECT * FROM habits WHERE id = :id;"
        data_habit = {
            'id': id
        }
        return self.db.query_db(query_habit, data_habit)

    def show_viol_by_habitid(self, id):
        query_viol = "SELECT * FROM violations WHERE habit_id = :id;"
        data_viol = {
            'id': id
        }
        return self.db.query_db(query_viol, data_viol)

    def get_violations_by_habit_id(self, id):
        query_viol = "SELECT violations.created_at as viol_date, violations.id as viol_id, concat(users.first_name, ' ', users.last_name) as helper_name, users.email as helper_email, habits.amount as amount, habits.habit_name as habit_name, habits.created_at as habit_date, habits.id as habit_id  FROM violations  LEFT JOIN users ON users.id = violations.helper_id LEFT JOIN habits ON habits.id = violations.habit_id WHERE habit_id = :id;"
        data_viol = {
            'id':id
        }
        return self.db.query_db(query_viol, data_viol)
    """
    def create_product(self, data):
            errors=[]
            if not data['name']:
                errors.append('Name of a new product cannot be empty!')
            elif len(data['name'])>255:
                errors.append('Name of the product cannot be longer than 255 characters!')
            
            if not data['description']:
                errors.append('Please give some description!')
            elif len(data['description'])>255:
                errors.append('Please make sure the product description is less than 255 characters!')
            
            if not data['price']:
                errors.append('A new product should have a price!')
            if not is_number(data['price']):
                errors.append('Price should be a number!')

            if errors:
                return {'status': False, 'errors': errors}
            else:
                query_new_product = "INSERT INTO products (name, price, description, created_at, updated_at) VALUES (:name, :price, :description, NOW(), NOW())"
                data_new_product = {
                    'name': data['name'],
                    'price': data['price'],
                    'description': data['description']
                }
                self.db.query_db(query_new_product, data_new_product)
                errors.append('You have successfully added a product!')
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

    def delete_product(self, id):
        query_delete = "DELETE FROM products WHERE id = :id"
        data_delete = {
            'id': id
        }
        self.db.query_db(query_delete, data_delete)
        return True

    """
'''
import re
a way how to check if unicode string is a number
if re.match("^\d+?\.\d+?$", element) is None:
    print "Not float"
'''
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False



    
        

    