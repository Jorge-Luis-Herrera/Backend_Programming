# Running the app
o run the application ,use the Flask comand or python -m flask. You need to tell the Flask where your application is with the --app option**

#### In terminal

    flask --app <Name_App> run

### Output
#
    Serving Flask app 'hello'
    Running on http://127.0.0.1:5000 (Press CTRL + C to quit)

### You can also run the server public
    flask run --host=0.0.0.0
    This tells your operating system to listen on all public IPs.

### To enable debug mode, use the --debug option.
    flask --app <app_name> run --debug

### Output
    Serving Flask app 'hello'
    Debug mode: on
    Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
    Restarting with stat
    Debugger is active!
    Debugger PIN: nnn-nnn-nnn