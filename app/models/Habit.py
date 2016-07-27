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



    
        

    