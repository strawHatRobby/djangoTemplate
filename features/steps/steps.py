

from behave import *
from django.test import TestCase

@when('I go to home')
def step(context):
    context.browser.get('http://localhost:8000')


@then("it should have the title 'Welcome to Django'")
def step(context):
    assert 'Welcome to Django' in context.browser.title


@when('I add two and two')
def step(context):
    context.test.assertEqual(2+2,3)
