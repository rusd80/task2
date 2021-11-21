from flask import Flask, render_template
import os

application = Flask(__name__)


@application.route("/")
def index():
    print(os.getcwd())
    return "Hello World! This is Flask Main Page"


@application.route("/help")
def help_page():
    return "<b><font color=green>This is Help Page!</font></b>"


@application.route("/htmlpage")
def show_html_page():
    my_file = open("/home/cube366/flask_ansible/templates/index.html", mode='r')
    page = my_file.read()
    my_file.close()
    user = {'nickname': 'Miguel'}
    return render_template("index.html",
                           title='Home',
                           user=user)


if __name__ == "__main__":
    application.run()
