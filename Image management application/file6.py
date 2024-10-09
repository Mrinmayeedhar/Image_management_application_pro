from flask import Flask, render_template, redirect, request, url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt

# Flask Login Setup
login_manager = LoginManager()
login_manager.init_app(app)

# Add Signup and Login code here
