Feature: Test site url

  Scenario: Go to homepage and check
     When I go to home
     Then it should have the title 'Welcome to Django'
