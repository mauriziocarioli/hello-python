#from datetime import datetime

# Get the current date and time
#current_datetime = datetime.now()

#print("Current date and time: ", current_datetime)
from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def show_current_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'Current date and time: {current_time}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
