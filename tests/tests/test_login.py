from step_definitions.login_steps import *
from step_definitions.home_steps import *

from pytest_bdd import scenario


@scenario('login.feature', 'User can login the service')
def test_login():
    pass


@scenario('login.feature', 'User pass wrong username and password into login form')
def test_login_negative():
    pass
