"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import mercadorias3.views
