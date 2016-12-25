from flask import Flask, render_template, request, redirect, url_for
from todo.database import db, init_db
from config import SQLALCHEMY_DATABASE_URI

todo = Flask(__name__)

from todo import controller

todo.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
init_db(todo)
