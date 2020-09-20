from flask import render_template,redirect,url_for
from . import main


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'One Minute Pitch'

    return render_template('index.html', title = title)

