from flask import Blueprint, render_template

# Define the blueprint
main = Blueprint('main', __name__)

# Home page route
@main.route('/')
def index():
    return render_template('index.html')

# About Us page route
@main.route('/about-us')
def about_us():
    return render_template('about_us.html')

# Our Mission page route
@main.route('/our-mission')
def our_mission():
    return render_template('our_mission.html')

# Donate page route
@main.route('/donate')
def donate():
    return render_template('donate.html')

# Join Us page route
@main.route('/join-us')
def join_us():
    return render_template('join_us.html')
