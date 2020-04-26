import os

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://oranehzkghexin:9530bcc4898247cbd7385fff8f1a3f66f17ddb5e54c3f05f5fd493129cc3340a@ec2-34-197-212-240.compute-1.amazonaws.com:5432/dasqjqdnj4ff1k'
SQLALCHEMY_TRACK_MODIFICATIONS = False
