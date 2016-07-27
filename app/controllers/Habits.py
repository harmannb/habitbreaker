"""
    Controller File
    Habit Breaker - Habits Controller
"""
from system.core.controller import *
from flask import flash
class Habits(Controller):
    def __init__(self, action):
        super(Habits, self).__init__(action)
        
        self.load_model('User')
        self.load_model('Habit')
        self.db = self._app.db

   
    def index(self):
        print "redirected"
        return redirect('/')

    """
    def new(self):
        return self.load_view('/products/new.html')

    def show(self,id):
        print 'showen =)'
        product = self.models['Product'].get_product(id)
        return self.load_view('/products/show.html', product = product[0])

    def edit(self, id):
        print 'editing =)'
        product = self.models['Product'].get_product(id)
        return self.load_view('/products/edit.html', product = product[0])

    def update(self, id):
        print 'updated =)'
        validate = self.models['Product'].update_product(request.form)
        print validate
        if validate['status'] == True:
            for message in validate['errors']:
                flash(message, 'valid')
            return redirect('/products')
        else:
            for message in validate['errors']:
                flash(message, 'error')
            return redirect('/products/edit/'+str(id))
    
    def create(self):
        print 'added =)'
        validate = self.models['Product'].create_product(request.form)
        if validate['status'] == True:
            for message in validate['errors']:
                flash(message, 'valid')
            return redirect('/products')
        else:
            for message in validate['errors']:
                flash(message, 'error')
            return redirect('/products/new')

    
    def destroy(self, id):
        print 'deleted =)'
        deleted = self.models['Product'].delete_product(id) 
        if deleted:
            flash('The product was deleted successfully!', 'valid')
            
        else:
            flash('Something went wrong while deleting', 'error')
        return redirect('/products')

    """