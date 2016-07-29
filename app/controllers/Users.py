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
        friend_habits = self.models['Habit'].get_habits_by_helper_id(id)
        # we will pass user variable with user ifno, habits with all habits, violation per habit, list of helpers per habit
        # we are using habits variable so far
        return self.load_view('/users/show_user.html', user = user[0], habits = habit, friend_habits = friend_habits )

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
            session['first_name'] = validate['user']['first_name']
            return redirect('/users/account/'+str(id))
        else:
            for message in validate['errors']:
                flash(message, 'error')
            return redirect('/users/edit/'+str(id))

    def password(self):
        return self.load_view('/users/password.html')

    def password_change(self):
        # model function - def update_password(self):
        print 'updated password =)'
        validate = self.models['User'].update_password(request.form)
        print validate
        if validate['status'] == True:
            for message in validate['errors']:
                flash(message, 'valid')
            return redirect('/users/account/'+str(session['id']))
        else:
            for message in validate['errors']:
                flash(message, 'error')
            return redirect('/users/password')
        

    def delete_user(self, id):
        print 'deleted =)'
        deleted = self.models['User'].delete_user(id) 
        if deleted:
            flash('The user was deleted successfully!', 'valid')
        else:
            flash('Something went wrong while deleting', 'error')
        return redirect('/logout')

    def show_helpers(self,id):
        helpers = self.models['User'].show_helpers_by_habit_id(id)
        violations = self.models['Habit'].get_violations_by_habit_id(id)
        return self.load_view('/users/show_helpers.html', habit_id = id, helpers = helpers, violations = violations)

        #signup
    def facebook_success(self, first_name, last_name, email):
        users = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        }
        validate = self.models['User'].add_user_fb(users)
        if validate['status'] == True:
            session['id'] = validate['user']['id']
            session['first_name'] = validate['user']['first_name']
            return redirect('/users/'+str(session['id']))
        else: # will never go to else
            for message in validate['errors']:
                flash(message, 'error reg')
            return redirect('/signup')
