@high
Feature: The dealer for the game of 21

@dealcards
Scenario: Deal initial cards
    Given a dealer
    When the round starts
    Then the dealer gives herself two cards

Scenario Outline: Get hand total
    Given a <hand>
    When the dealer sums the cards
    Then the <total> is correct

Examples: Hands
    | hand      | total |
    | 5,7       | 12    |
    | 5,Q       | 15    |
    | Q,Q,A     | 21    |
    | Q,A       | 21    |
    | A,A,A     | 13    |

@rules
Scenario Outline: Dealer plays by the rules
    Given a hand <total>
    When the dealer determines a play
    Then the <play> is correct

Examples: Hands
    | total | play  |
    | 10    | hit   |
    | 15    | hit   |
    | 16    | hit   |
    | 17    | stand  |
    | 18    | stand  |
    | 19    | stand  |
    | 20    | stand  |
    | 21    | stand  |
    | 22    | stand  |


