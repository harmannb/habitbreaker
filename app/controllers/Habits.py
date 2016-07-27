"""
    Controller File
    Habit Breaker - Habits Controller
"""
from system.core.controller import *
import datetime

class Habits(Controller):
    def __init__(self, action):
        super(Habits, self).__init__(action)
        
        self.load_model('User')
        self.load_model('Habit')
        self.db = self._app.db

   
    def index(self):
        print "redirected"
        return redirect('/')

    def show_habit(self,id):
        habit = self.models['Habit'].show_habit_by_id(id)
        violation = self.models['Habit'].show_viol_by_habitid(id)
        habit_violations = self.models['Habit'].get_violations_by_habit_id(id)
        sum_am = 0
        for i in habit_violations:
            sum_am += i['amount']

        return self.load_view('/habits/show_habit.html', habit_violations = habit_violations, sum = sum_am)

    def add_habit(self):
        return self.load_view('/habits/add_habit.html')

    def add_new_habit(self):
        validate = self.models['Habit'].add_new_habit(request.form)
        if validate['status'] == True:
            for message in validate['errors']:
                flash(message, 'valid')
            return redirect('/users/'+str(session['id']))
        else:
            for message in validate['errors']:
                flash(message, 'errors')
            return redirect('/habits/add_new_habit')


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