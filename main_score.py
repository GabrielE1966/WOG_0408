from flask import Flask
from utils import BAD_RETURN_CODE, SCORES_FILE_NAME

app = Flask(__name__)


@app.route("/")
def score_server():
    # open the file.
    user_score = 0
    try:
        score_file = open(SCORES_FILE_NAME, 'r')
        file_line = score_file.readline()
        user_score = int(file_line)
        score_file.close()
    except FileNotFoundError:
        user_score = -1
    except TypeError:
        user_score = -1

    if user_score >= 0:
        return f'''
                    <html>
                        <head> 
                            <title> Scores Game </title>
                        </head>
                        <body>
                           <h1> The score is: </h1>
                           <div id="score"> {user_score} </div>
                        </body>
                    </html>     
               '''
    else:
        return f'''
                    <html>
                        <head> 
                            <title> Scores Game </title>
                        </head>
                        <body>
                           <h1> ERROR: </h1>
                           <div id="score" style="color:red"> {BAD_RETURN_CODE} </div>
                        </body>
                    </html>     
               '''
