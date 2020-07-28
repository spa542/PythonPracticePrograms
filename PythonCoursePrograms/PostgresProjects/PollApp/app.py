import os
from typing import List
import psycopg2
from psycopg2.errors import DivisionByZero
from dotenv import load_dotenv
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

def prompt_create_poll(connection):
    poll_title = input("Enter poll title: ")
    poll_owner = input("Enter poll owner: ")
    options = []

    new_option = input(NEW_OPTION_PROMPT)
    while new_option != "":
        options.append(new_option)
        new_option = input(NEW_OPTION_PROMPT)

    database.create_poll(connection, poll_title, poll_owner, options)


def list_open_polls(connection):
    polls = database.get_polls(connection)

    for _id, title, owner in polls:
        print(f"{_id}: {title} (created by {owner})")


def prompt_vote_poll(connection):
    poll_id = int(input("Enter poll you would like to vote on: "))

    poll_options = database.get_poll_details(connection, poll_id)
    _print_poll_options(poll_options)

    option_id = int(input("Enter option you'd like to vote for: "))
    username = input("Enter the username you'd like to vote as: ")
    database.add_poll_vote(connection, username, option_id)


def _print_poll_options(poll_with_options: List[database.PollWithOptions]):
    for option in poll_with_options:
        print(f"{option[3]}: {option[4]}")


def show_poll_votes(connection):
    poll_id = int(input("Enter poll you would like to see votes for: "))
    try:
        # This gives us cont and percentage of votes for each option in a poll
        poll_and_votes = database.get_poll_and_vote_results(connection, poll_id)
    except DivisionByZero:
        print("No votes yet cast for this poll")
    else:
        for _id, option_text, count, percentage in poll_and_votes:
            print(f"{option_text} got {count} votes ({percentage:.2f}% of total)")


def randomize_poll_winner(connection):
    poll_id = int(input("Enter poll you'd like to pick a winner for: "))
    poll_options = database.get_poll_details(connection, poll_id)
    _print_poll_options(poll_options)

    option_id = int(input("Enter which is the winning option, we'll pick a random winner from voters: "))
    winner = database.get_random_poll_vote(connection, option_id)
    print(f"The randomly selected winner is {winner[0]}.")


MENU_OPTIONS = {
    "1": prompt_create_poll,
    "2": list_open_polls,
    "3": prompt_vote_poll,
    "4": show_poll_votes,
    "5": randomize_poll_winner
}

def menu():
    database_url = input(DATABASE_PROMPT)
    if not database_url:
        load_dotenv()
        database_url = os.environ["DATABASE_URL"]

    connection = psycopg2.connect(database_url)
    database.create_tables(connection)

    selection = input(MENU_PROMPT)
    while selection != "6":
        try:
            MENU_OPTIONS[selection](connection)
        except KeyError:
            print("Invalid input selected. Please try again.")
        selection = input(MENU_PROMPT)


if __name__ == '__main__':
    menu()
