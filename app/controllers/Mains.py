"""
    Controller File
    Habit Breaker - Mains Controller
"""
from system.core.controller import *

# handle home, signin, signup, logout

class Mains(Controller):
    def __init__(self, action):
        super(Mains, self).__init__(action)

        self.load_model('Main')
        self.load_model('Habit')
        self.db = self._app.db
   
    def index(self):
        return self.load_view('index.html')

    def signin(self):
        return self.load_view('/main/signin.html')

    def signup(self):
        return self.load_view('/main/signup.html')

    # def signup_helper(self, habit_id):
    #     validate = self.models['Main'].validate_add_user(request.form)
    #     if validate['status'] == True:
    #         session['id'] = validate['user']['id']
    #         session['first_name'] = validate['user']['first_name']
    #         self.models['Habit'].add_helper(session['id'], habit_id)
    #         return redirect('/users/'+str(session['id']))
    #     else:
    #         for message in validate['errors']:
    #             flash(message, 'error reg')
    #         return redirect('/signup/'+str(habit_id))


    def register(self):
        validate = self.models['Main'].validate_add_user(request.form)
        if validate['status'] == True:
            session['id'] = validate['user']['id']
            session['first_name'] = validate['user']['first_name']
            if request.form['habit_id']:
                self.models['Habit'].add_helper(session['id'], request.form['habit_id'])
                return redirect('/users/'+str(session['id']))
            else:
                return redirect('/users/'+str(session['id']))
        else:
            for message in validate['errors']:
                flash(message, 'error reg')
            if request.form['habit_id']:
                return redirect('/signup/'+str(request.form['habit_id']))
            else:
                return redirect('/signup')

    
    def login(self):
        validate = self.models['Main'].validate_log_user(request.form)
        if validate['status'] == True:
            session['id'] = validate['user']['id']
            session['first_name'] = validate['user']['first_name']
            # change to /quotes
            return redirect('/users/'+str(session['id']))
        else:
            for message in validate['errors']:
                flash(message, 'error log')
            return redirect('/signin')

    def logout(self):
        session.clear()
        return redirect('/')

