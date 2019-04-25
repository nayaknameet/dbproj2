import mysql.connector
from mysql.connector import errorcode
import Credentials
import Query
from flask import Flask, render_template, request
import re
app = Flask(__name__)

config = Credentials.credentials_dict
regex_ = re.compile(r'[a-zA-Z]+ [a-zA-Z]+|[a-zA-Z]+')       #Regex for only [alphabets] and [alphabets space alphabets]

def is_valid_input(str):
    # Inorder to make the script secure
    # Check if it matches the regex or is empty
    if regex_.fullmatch(str) or not str:
        return True
    else:
        return False

def check_inputs(country_name, color):
    # To check which input box is empty and generate error messages
    # accordingly. Otherwise, return True if requirements are fulfilled
    if not color and not country_name:
        return 'Please Enter Inputs'
    elif not country_name:
        return 'Please Enter a valid Country_name'
    elif not color:
        return True
    else:
        return False


class WorldCup:
    # To generate a connection with the database and query against the database
    def __init__(self):
        # To generate a connection
        try:
            self.cnx = mysql.connector.connect(**config, database = 'world_cup')
            self.cursor = self.cnx.cursor()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def wc_country(self, country_name):
        # For 1st query
        cc = self.cursor
        self.cursor.execute((Query.q1).format(country_name))
        result = self.cursor.fetchall()
        return result

    def wc_color(self, country_name, color):
        # For 2nd query
        c = self.cursor
        self.cursor.execute((Query.q2).format(country_name, color))
        result = self.cursor.fetchall()
        return result


@app.route("/")
def hello():
    # For initial page
    return render_template("index.html")

@app.route("/send", methods = ['POST'])
def user_inputs():
    # To fetch the inputs from the html form and generate data accordingly
    country_name = request.form['country_name']                     # Fetch country_name from the form
    regex_checking_cn = is_valid_input(country_name)

    color = request.form['color']                                      # Fetch color from the form
    regex_checking_c = is_valid_input(color)

    if regex_checking_c == False or regex_checking_cn == False:         # Checking if the both the inputs fall into the pattern matching cases
        return render_template("index.html", error_msg="Invalid input(s)")  # Else generate error message


    input_val = check_inputs(country_name, color)                       # Check if requirements are made for the input(s)

    if input_val == True:                                               # Country_name is only returned
        result = wc1.wc_country(country_name)
        if not result:                                                  # Results are empty, therefore no data exists
            return render_template("index.html", error_msg="No such data exists")
        else:
            return render_template("index.html", variable=result, table_names_1=['GameID', 'Player_Name', 'Player_No'])
    elif input_val == False:                                            # Both the inputs are returned
        result = wc1.wc_color(country_name, color)
        if not result:
            return render_template("index.html", error_msg = "No such data exists")
        else:
            return render_template("index.html", q2 = result, table_names_2 = ['GameID', 'Player_Name'])
    else:
        return render_template("index.html", error_msg = input_val)


if __name__ == '__main__':
    wc1 = WorldCup()
    app.run(debug=True)