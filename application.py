from flask import Flask

application=Flask(__name__)

@application.route('/')
def VivaPeron():
    return "Viva Peron"

if __name__ == '__main__':
    application.debug = True
    application.run(host="0.0.0.0")
