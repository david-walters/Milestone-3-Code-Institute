"""
This module is used to run the Flask application.

It imports the Flask app instance from the events_list module and starts
the application on the configured host and port.
"""

from events_list import app

if __name__ == '__main__':
    host = app.config.get('IP', '127.0.0.1')
    port = app.config.get('PORT', 5000)
    DEBUG = False

    app.run(host=host, port=port, debug=DEBUG)
