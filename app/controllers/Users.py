"""
    Controller File
    Habit Breaker - Users Controller
"""
from system.core.controller import *
from flask import flash
class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        
        self.load_model('User')
        self.load_model('Habit')
        self.db = self._app.db

   
    def index(self):
        print "redirected"
        return redirect('/')


    def show_user(self, id):
        user = self.models['User'].get_user_by_id(id)
        habit = self.models['Habit'].get_habits_by_user_id(id)
        # we will pass user variable with user ifno, habits with all habits, violation per habit, list of helpers per habit
        return self.load_view('/users/show_user.html', user = user[0], habits = habit )

    def show_account(self,id):
        user = self.models['User'].get_user_by_id(id)
        return self.load_view('/users/account.html', user= user[0])

    def edit(self,id):
        user = self.models['User'].get_user_by_id(id)
        return self.load_view('/users/edit_user.html', user=user[0])

    def update(self, id):
        print 'updated =)'
        validate = self.models['User'].update_user(request.form)
        print validate
        if validate['status'] == True:
            for message in validate['errors']:
                flash(message, 'valid')
            return redirect('/users/account/'+str(id))
        else:
            for message in validate['errors']:
                flash(message, 'error')
            return redirect('/users/edit/'+str(id))

    def password(self):
        return self.load_view('/users/password.html')

