
from behave import *
from twentyone import *


@given(u'a dealer')
def step_impl(context):
    context.dealer = Dealer()       # initialize state

@given('a hand {total:d}')
def step_impl(context, total):
    context.dealer = Dealer()
    context.total = total

@when(u'the round starts')
def step_impl(context):
    context.dealer.new_round()

@then(u'the dealer gives herself two cards')
def step_impl(context):
    assert (len(context.dealer.hand) == 2)

@given('a {hand}')                          # {hand} maps to <hand> in dealer.feature
def step_impl(context, hand):               # hand passed in as second parameter
    context.dealer = Dealer()
    context.dealer.hand = hand.split(',')   # split hand to get a list

@when(u'the dealer sums the cards')
def step_impl(context):
    context.dealer_total = context.dealer.get_hand_total()


@then(u'the {total:d} is correct')          # d: means treat parameter as integer
def step_impl(context, total):
    assert (context.dealer_total == total)

@when('the dealer determines a play')
def step_impl(context):
    context.dealer_play = context.dealer.determine_play(context.total)

@then('the dealer gives itself two cards')
def step_impl(context):
    assert (len(context.dealer.hand) == 2)

@then('the {total:d} is correct')
def step_impl(context, total):
    assert (context.dealer_total == total)

## NEW STEP
@then('the {play} is correct')
def step_impl(context, play):
    assert (context.dealer_play == play)