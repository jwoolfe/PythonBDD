Feature: Verifying registration functionality

Scenario: Registration with valid data
    Given User is on registration page 
    When User enters username
    And User enters email id
    And User enters password
    And User clicks on signup button
    Then User is registered successfully

Scenario: Registration with duplicate username data
    Given User is on registration page
    When User enters duplicate username
    And User enters email id
    And User enters password
    And User clicks on signup button
    Then User is registered successfully