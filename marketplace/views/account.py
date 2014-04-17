__author__ = 'owner'

from marketplace.views import *
from pyramid.security import remember, forget, authenticated_userid
from marketplace.forms.account import LoginForm,RegistrationForm
from marketplace.models.account import User
from pyramid.renderers import render_to_response
from marketplace.models import (
    DBSession
    )
from pyramid.renderers import render
from pyramid.response import Response

# Create Account View Class
class AccountViews(object):

    def __init__(self, request):
        self.request = request
        #Use base layout
        renderer = get_renderer("marketplace:templates/layout.mako")

    @view_config(route_name='login', renderer='marketplace:templates/accounts/login.mako')
    def login(self):

        request = self.request
        form = LoginForm(self.request.POST)
        if self.request.method =="POST" and form.validate():
            email = form.email.data
            password = form.password.data
            if User.check_password(email, password):
                headers = remember(request, email)

                url = self.request.route_url('home')


                return HTTPFound(location=url, headers=headers)

        return {'title': "Login" , 'form':form}

    @view_config(route_name='register', renderer='marketplace:templates/accounts/registration.mako')
    def register(self):


        form = RegistrationForm(self.request.POST)
        if self.request.method =="POST" and form.validate():

            print "Creating User"
            email = form.email.data
            password = form.password.data

            print password
            #prescription_number = form.prescription_number
            #first_name = form.first_name
            #last_name = form.last_name



            user = User(email, password)
            DBSession.add(user)

            # Return login route
            return HTTPFound(location=self.request.route_url('login'))

        else:
            print form.errors

        return {'title': "Registration" , 'form':form}