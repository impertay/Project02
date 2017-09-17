from flask import Flask, redirect, url_for
app = Flask(__name__)

import server.home_page
import server.user_page
