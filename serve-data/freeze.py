#!/usr/bin/env python3
from flask_frozen import Freezer
from serve_data import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
