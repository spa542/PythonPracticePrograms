from typing import List
import random
import datetime
import pytz
from connections import get_connection
from models.poll import Poll
from models.option import Option
import database

DATABASE_PROMPT = "Enter the DATABASE_URL value or leave empty to load from .env file: "

MENU_PROMPT = """-- Menu --

1) Create new poll
2) List open polls
3) Vote on a poll
4) Show poll votes
5) Select a random winner from a poll option
6) Exit

Enter your choice: """

NEW_OPTION_PROMPT = "Enter new option text (or leave empty to stop adding options): "

def prompt_create_poll():
    poll_title = input("Enter poll title: ")
    poll_owner = input("Enter poll owner: ")
    poll = Poll(poll_title, poll_owner)
    poll.save()

    new_option = input(NEW_OPTION_PROMPT)
    while new_option != "":
        poll.add_option(new_option)
        new_option = input(NEW_OPTION_PROMPT)


def list_open_polls():
    for poll in Poll.all():
        print(f"{poll.id}: {poll.title} (created by {poll.owner})")


def prompt_vote_poll():
    poll_id = int(input("Enter poll you would like to vote on: "))

    _print_poll_options(Poll.get(poll_id).options)

    option_id = int(input("Enter option you'd like to vote for: "))
    username = input("Enter the username you'd like to vote as: ")

    Option.get(option_id).vote(username)


def _print_poll_options(options: List[Option]):
    for option in options:
        print(f"{option.id}: {option.text}")


def show_poll_votes():
    poll_id = int(input("Enter poll you would like to see votes for: "))
    poll = Poll.get(poll_id)
    options = Poll.get(poll_id).options
    votes_per_option = [len(option.votes) for option in options]
    total_votes = sum(votes_per_option)

    try:
        for option, votes in zip(options, votes_per_option):
            percentage = votes / total_votes * 100
            print(f"{option.text} got {votes} votes ({percentage:.2f}% of total)")
    except ZeroDivisionError:
        print("No votes cast for this poll yet.")

    vote_log = input("Would you like to see the vote log? (y/N) ")

    if vote_log == "y":
        _print_votes_for_options(options)


def _print_votes_for_options(options: List[Option]):
    for option in options:
        print(f"-- {option.text} --")
        for vote in option.votes:
            naive_datetime = datetime.datetime.utcfromtimestamp(vote[2])
            utc_date = pytz.utc.localize(naive_datetime)
            local_date = utc_date.astimezone(pytz.timezone("Europe/London")).strftime("%Y-%m-%d %H-%M")
            print(f"\t- {vote[0]} on {local_date}")


def randomize_poll_winner():
    poll_id = int(input("Enter poll you'd like to pick a winner for: "))
    _print_poll_options(Poll.get(poll_id).options)

    option_id = int(input("Enter which is the winning option, we'll pick a random winner from voters: "))
    votes = Option.get(option_id).votes
    winner = random.choice(votes)
    print(f"The randomly selected winner is {winner[0]}.")


MENU_OPTIONS = {
    "1": prompt_create_poll,
    "2": list_open_polls,
    "3": prompt_vote_poll,
    "4": show_poll_votes,
    "5": randomize_poll_winner
}

def menu():
    with get_connection() as connection:
        database.create_tables(connection)

    selection = input(MENU_PROMPT)
    while selection != "6":
        try:
            MENU_OPTIONS[selection]()
        except KeyError:
            print("Invalid input selected. Please try again.")
        selection = input(MENU_PROMPT)


if __name__ == '__main__':
    menu()
