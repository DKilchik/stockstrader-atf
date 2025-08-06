from step_definitions.login_steps import *
from step_definitions.home_steps import *


from pytest_bdd import scenario

@scenario('login.feature', 'User login the service')
def test_login():
    pass