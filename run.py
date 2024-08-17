from events_list import app

if __name__ == '__main__':
    host = app.config.get('IP', '127.0.0.1')
    port = app.config.get('PORT', 5000)
    debug = app.config.get('DEBUG', False)
   
    app.run(host=host, port=port, debug=debug)