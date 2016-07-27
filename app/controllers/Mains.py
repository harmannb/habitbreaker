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
        self.db = self._app.db
   
    def index(self):
        return self.load_view('index.html')

    def signin(self):
        return self.load_view('/main/signin.html')

    def signup(self):
        return self.load_view('/main/signup.html')

    def register(self):
        validate = self.models['Main'].validate_add_user(request.form)
        if validate['status'] == True:
            session['id'] = validate['user']['id']
            session['first_name'] = validate['user']['first_name']
            # change to /quotes
            return redirect('/users/'+str(session['id']))
        else:
            for message in validate['errors']:
                flash(message, 'error reg')
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

