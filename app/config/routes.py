"""
    Routes Configuration File
    Habit Breaker
"""
from system.core.router import routes
# Mains routes
routes['default_controller'] = 'Mains' #loads index.html - '/'
routes['/signin'] = 'Mains#signin' # loads signin.html
routes['/signup'] = 'Mains#signup' # loads signup page
routes['POST']['/login'] = 'Mains#login' # validates and if success redirect '/users/<int:id>', if not - rdirect to '/signin'
routes['POST']['/register'] = 'Mains#register'
routes['/logout'] = 'Mains#logout' # clears session and redirect to '/'

# Users routes
routes['/users/<int:id>'] = 'Users#show_user' # loads show_user.html with user's data
routes['/users/account/<int:id>'] = 'Users#show_account' # loads account.thml with user's account information
routes['/users/edit/<int:id>'] = 'Users#edit' # loads the edit_user.html with a form to update
routes['POST']['/users/update/<int:id>'] = 'Users#update'# validates info and updates database. if success - redirects to '/users/account'
# redundent route
#routes['/users/password'] = 'Users#password' # loads the password.html
routes['POST']['/users/password_change'] = 'Users#password_change' # validates the password and make changes in database
routes['GET']['/users/delete_user/<int:id>'] = 'Users#delete_user' # deletes user from database
routes['/users/helpers/<int:id>'] = 'Users#show_helpers' # loads list of helpers by user id

# Habits and Violations routes
routes['/habits/show_habit/<int:id>'] = 'Habits#show_habit' # loads show_habit.html with a sfecific habit id
routes['/habits/add_habit'] = 'Habits#add_habit' # loads add_habit.html
routes['POST']['/habits/new_habit'] = 'Habits#add_new_habit' # validates fields and adds new habit to user
