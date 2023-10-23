# Python viratal env: https://docs.python.org/3/library/venv.html

# python -m venv mywebsite     (creates a vritual environment )
# . mywebsite/bin/activate   (activates virtual envrionment )
# deactivate   (deactivates virtual env)

# pip install Flask

# export FLASK_APP=server.py
# export FLASK_ENV=development  (turns on debug mode)
# flask run 




# Flask: https://flask.palletsprojects.com/en/3.0.x/quickstart/
# varible rules https://flask.palletsprojects.com/en/3.0.x/quickstart/#variable-rules
# Free icons # https://icon-icons.com/
# Mime Type: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types
# Python CSV module: https://docs.python.org/3/library/csv.html

# Starwars API:  https://swapi.dev
# Robohash website:  https://robohash.org/




from flask import Flask , render_template, url_for, request, redirect 
import csv

app = Flask(__name__)


@app.route('/')
def my_home():    
    return render_template('index.html')
    
@app.route('/<string:page_name>')
def html_page(page_name):    
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
    
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST': 
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect('/thankyou.html')
        except:
            return 'did not savae to database'
    else:
        return 'Something went wrong. Please Try again!'

"""
    
@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/works.html')
def work():
    return render_template('works.html')

    
@app.route("/contaclt.html")
def contact():
    return render_template('contact.html')

"""