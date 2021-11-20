from flask import Flask

application = Flask(__name__)


@application.route("/")
def index():
    return "Hello World! This is Flask Main Page"


@application.route("/help")
def helppage():
    return "<b><font color=blue>This is Help Page v2!!!</font></b>"


@application.route("/htmlpage")
def show_html_page():
    myfile = open("mypage.html", mode='r')
    page   = myfile.read()
    myfile.close()
    return page

if __name__ == "__main__":
    application.run()
