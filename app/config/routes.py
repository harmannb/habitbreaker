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
routes['/users/password'] = 'Users#password' # loads the password.html
routes['POST']['/users/password_change'] = 'Users#password_change' # validates the password and make changes in database

# Habits and Violations routes

