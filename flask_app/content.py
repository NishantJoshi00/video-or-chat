#!/usr/bin/env python3

from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user
from .models import User
from . import db, socketio

content = Blueprint('content', __name__)

# ------------------ Some Pages ----------------------- #

@content.route("/")
def index():
	return render_template("index.html")

@content.route("/profile")
@login_required
def profile():
	return render_template("dashboard.html", user = current_user)

@content.route("/create_voice_channel", methods=["GET"])
@login_required
def create_voice_channel():
	... # Creating the UDP socket for managing the connection

@content.route("/join_voice_channel", methods=["POST"])
@login_required
def join_voice_channel():
	... # Join the UDP socket the connection


@content.route("/create_video_channel", methods=["GET"])
@login_required
def create_video_channel():
	... # Creating the UDP socket for managing the connection

@content.route("/join_video_channel", methods=["POST"])
@login_required
def join_video_channel():
	... # Join the UDP socket the connection

