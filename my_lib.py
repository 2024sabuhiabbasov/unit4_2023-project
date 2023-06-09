# Description: This file contains all the functions that are used in the main file
import sqlite3


class database_worker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()


# code for the password hashing
from passlib.hash import sha256_crypt

hasher = sha256_crypt.using(rounds=30000)  # Make it slower


def encrypt_password(user_password):
    return hasher.hash(user_password)


def check_password(hashed_password, user_password):
    return hasher.verify(user_password, hashed_password)
