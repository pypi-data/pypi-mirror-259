def app():
    print('''
    from flask import Flask, jsonify, render_template, request, redirect, url_for, session
    import pdfplumber
    import json
    import google.generativeai as genai

    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    GOOGLE_API_KEY = 'AIzaSyD2_BY1YIYvhxEw7lMk0XuDzA3pwHV4nYU'
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    global wrongAns 

    @app.route('/')
    def index():
        session.clear()
        return render_template('index.html')

    @app.route('/extract_text', methods=['POST'])
    def extract_text():
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        if file:
            text = ''
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    text += page.extract_text()
            session['extracted_text'] = text
            session['current_question_index'] = 0
            
            # Generate questions and answers from extracted text
            prompt = f"""generate 2 question and there answers in json format from the given context delimited by triple backtick ```{text}```"""
            response = model.generate_content(prompt)
            response_json = json.loads(response.text.split("```")[1][4:])
            print(response_json)
            questions_answers = response_json["questions"]
            session['questions_answers'] = questions_answers

            return redirect(url_for('quiz'))

    @app.route('/quiz', methods=['GET', 'POST'])
    def quiz():
        
        if 'current_question_index' not in session or 'questions_answers' not in session:
            return redirect(url_for('index'))

        questions_answers = session['questions_answers']

        def generate_summary(wrongAns):
            if(wrongAns == ""):
                return "You got all the answers right. Great job!"
            else:
                response = model.generate_content(f"generate a summary in simple english words Instructing about how what user should study based on {wrongAns}")
                ans = response.text
                ans  = ans.replace('*', '')
                return ans
        
        def check_answer(question, answer, correct_answer):
            response = model.generate_content(f"given the system question, system answer and the user answer provided by the user if the user answer is similar to system answer return true else return false give only one word output system question={question}, system answer={correct_answer}, user answer={answer} ")
            # print(response.text)
            if response.text == "true" or response.text == "True" or response.text == "TRUE":
                return False
            return True

        if request.method == 'POST':
            answered = request.form.get('answer')
            question = questions_answers[session['current_question_index']]['question']
            correct_answer = questions_answers[session['current_question_index']]['answer']

            if not answered:
                error = "Please provide an answer."
            elif check_answer(question, answered, correct_answer):
                
                error = "Wrong answer. The correct answer is: {}".format(correct_answer)
            else:
                questions_answers[session['current_question_index']]['answer'] = "correct"
                session['current_question_index'] += 1

                if session['current_question_index'] < len(questions_answers):
                    return redirect(url_for('quiz'))
                else:
                    session.clear()
                    wrongAns = json.dumps(questions_answers)
                    return render_template('quiz_completed.html', summ=generate_summary(wrongAns))
            
            return render_template('quiz.html', question=questions_answers[session['current_question_index']]['question'], empty_error=error if not answered else None, wrong_answer_error=error if answered else None)

        if session['current_question_index'] < len(questions_answers):
            question = questions_answers[session['current_question_index']]['question']
            return render_template('quiz.html', question=question)

        return redirect(url_for('index'))

    if __name__ == '__main__':
        app.run(debug=True)

    ''')
    
def indexhtml():
    print('''
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../static/styles/style.css">
        <title>MakeItStick.ai</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link
            href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"
            rel="stylesheet" />
    </head>

    <body>
        <img src="../static/assets/header.png" alt="Header Image" class="header-image">


        <section>
            <div class="containerp">
                <div class="text-container">
                    <h2>MakeItStick.ai</h2>
                    <p>Access to thousands of design
                        resources and templates bla bla
                        bla catch phrase here</p>
                </div>
                <div class="extra-container upload-section">
                    <form action="/extract_text" method="post" enctype="multipart/form-data">
                        <div class="box">
                            <input type="file" name="file" accept=".pdf">
                            <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"
                                style="fill: #D2D2D2;">
                                <path
                                    d="M440-320v-326L336-542l-56-58 200-200 200 200-56 58-104-104v326h-80ZM240-160q-33 0-56.5-23.5T160-240v-120h80v120h480v-120h80v120q0 33-23.5 56.5T720-160H240Z" />
                            </svg>
                        </div>
                        <br>
                        <div class="upload-btn-container">
                            <input type="submit" value="Upload PDF" class="upload-button">
                        </div>
                    </form>
                </div>
            </div>
        </section>

        <section class="middle">
            <h2 class="htu">How to use MakeItStick.ai</h2>
            <div class="container">
                <div class="htu-image">
                    <img src="../static/assets/pdf.png" alt="upload pdf" width="300px">
                    <p>1. Upload your Study Material</p>
                </div>
                <div class="htu-image">
                    <img src="../static/assets/ans.png" alt="ans pdf" width="300px">
                    <p>2. Answer The Generated Ques</p>
                </div>
                <div class="htu-image">
                    <img src="../static/assets/feed.png" alt="feed pdf" width="300px">
                    <p>3. Get Proper Feedback</p>
                </div>
            </div>
        </section>
        <section>
            <div class="container2">
                <div class="smtxt">
                    <p>Project by,</p>
                </div>
                <div class="bolttxt">TeamStackUnderflow</div>
            </div>
        </section>
        <hr width="90%">
        <p class="htu">Non Copyrighted © 2024 Design and upload by TeamStackUnderflow</p>
    </body>

    </html>
    ''')

def quizhtml():
    print('''
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../static/styles/quiz.css">
        <title>Questions</title>
    </head>

    <body>
        <section>
            <h1 class="question">Question</h1>
            <br>
            <form action="/quiz" method="post">
                <p class="txt">{{ question }}</p>
                <input type="text" name="answer" placeholder="Enter your answer here.">
                <div id="submit-btn">
                    <input type="submit" value="Next">
                </div>

                <div class="answer">
                    Answer:
                </div>
                {% if empty_error %}
                <div class="check-text">
                    <p style="color: red;">{{ empty_error }}</p>
                </div>
                {% endif %}
                {% if wrong_answer_error %}
                <div class="ans-container">
                    <p style="color: red;">{{ wrong_answer_error }}</p>
                </div>
                {% endif %}
            </form>
        </section>
    </body>

    </html>
    ''')

def quizchtml():
    print('''
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../static/styles/quiz.css">
        <title>Summary</title>
        <link
        href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"
        rel="stylesheet" />
    </head>

    <body>
        <div>
            <div class="question">
                Summary
            </div>
            <div class="answer">
                Here are some points you can improve on
            </div>
            <div class="summ-container">
                {{ summ }}
            </div>
            <form action="/" method="get">
                <input type="submit" value="Done"
                    style="position: relative; top: 480px; left: 1200px; width: 160px; background: linear-gradient(86.91deg, #b62ea6 0%, #4b3684 102.34%); color: white; border: none; padding: 10px 20px; font-size: 16px; cursor: pointer; border-radius: 20px;">
            </form>
        </div>
    </body>

    </html>
    ''')

def stylecss():
    print('''
    body {
        display: flex;
        flex-direction: column;
        margin: 0;
        overflow-x: hidden;
        background-color: #1F1F1F;
        font-family: Regular;
    }

    p {
        font-family: "Poppins", sans-serif;
        font-weight: 400;
        font-size: 18px;
        font-style: normal;
    }

    h2 {
        font-family: "Poppins", sans-serif;
        font-weight: 600;
        font-size: 40px;
        font-style: normal;
        /* Use a valid font weight value */
    }

    /* Page Index.html */
    .header-image {
        height: 150px;
        width: 100%;
    }

    .containerp {
        padding-top: 160px;
        display: flex;
        justify-content: space-evenly;
        align-items: center;
    }

    .text-container {
        color: white;
        width: 400px;
        height: 224px;
    }

    .upload-button {
        background: linear-gradient(86.91deg, #B62EA6 0%, #4B3684 102.34%);
        margin-top: 20px;
        color: #D2D2D2;
        padding: 0.5rem 2.5rem;
        border: none;
        cursor: pointer;
        border-radius: 32px;
        margin-left: 0.5rem;
        margin-left: 10px;
        font-family: "Poppins", sans-serif;
        font-weight: 400;
        font-size: 20px;
        font-style: normal;
    }

    .upload-button:hover {
        background-color: #444;
    }

    input[type="file"] {
        color: #D2D2D2;
    }

    .box {
        width: 500px;
        height: 150px;
        border: 2px dashed white;
        border-radius: 10px;
        margin: 20px;
        margin-bottom: 0px;
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
    }

    .upload-section {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .middle {
        display: flex;
        flex-direction: column;
        padding: 160px 0 80px 0;
    }

    .container {
        display: flex;
        justify-content: space-evenly;
        align-items: center;
    }

    .htu {
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .htu-image {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-radius: 30px;
        color: #D2D2D2;
    }

    .container2 {
        color: white;
        margin: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .bolttxt {
        margin-left: 10px;
        font-family: "Poppins", sans-serif;
        font-weight: 600;
        font-size: 40px;
        font-style: normal;
    }

    .upload-btn-container {
        display: flex;
        justify-content: center;
    }
    ''')

def quizcss():
    print('''
    body {
        display: flex;
        flex-direction: column;
        margin: 0;
        overflow-x: hidden;
        background-color: #1F1F1F;
        font-family: Regular;
    }

    p {
        font-family: "Poppins", sans-serif;
        font-weight: 400;
        font-size: 18px;
        font-style: normal;
    }

    h2 {
        font-family: "Poppins", sans-serif;
        font-weight: 600;
        font-size: 40px;
        font-style: normal;
        /* Use a valid font weight value */
    }

    /* Page quiz.html */
    .question {
        color: white;
        font-family: "Poppins", sans-serif;
        font-weight: 600;
        font-size: 30px;
        font-style: bold;
        line-height: 68px;
        letter-spacing: 0em;
        text-align: left;
        width: 220px;
        height: 68px;
        position: relative;
        top: 87px;
        left: 158px;
    }

    .txt {
        width: 950px;
        height: 48px;
        position: relative;
        top: 30px;
        left: 187px;
        font-family: "Poppins", sans-serif;
        font-weight: 400;
        font-size: 18px;
        font-style: normal;
        line-height: 48px;
        letter-spacing: 0em;
        text-align: left;
        color: #ffffffcc;
        padding: 10px;
    }

    input[type="text"] {
        width: 1200px;
        height: 66px;
        position: relative;
        background-color: #1f1f1f;
        top: 30px;
        left: 178px;
        border-radius: 20px;
        border: 3px solid #838383;
        font-family: Poppins;
        font-size: 24px;
        font-weight: 400;
        line-height: 86px;
        letter-spacing: 0em;
        text-align: left;
        padding: 0 20px;
        color: white;
    }

    input[type="submit"] {
        position: relative;
        top: 80px;
        left: 1200px;
        width: 200px;
        background: linear-gradient(86.91deg, #B62EA6 0%, #4B3684 102.34%);
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        border-radius: 20px;
    }

    .answer {
        color: #ffffffcc;
        font-family: "Poppins", sans-serif;
        font-weight: 400;
        font-size: 24px;
        font-style: normal;
        line-height: 48px;
        letter-spacing: 0em;
        text-align: left;
        width: 950px;
        height: 48px;
        position: relative;
        top: 80px;
        left: 187px;
    }

    .check-text {
        font-family: Poppins;
        font-size: 24px;
        font-weight: 100;
        line-height: 48px;
        letter-spacing: 0em;
        text-align: left;
        width: 950px;
        height: 48px;
        position: relative;
        top: 40px;
        left: 200px;
    }

    .ans-container {
        width: 1200px;
        height: auto;
        position: absolute;
        top: 600px;
        left: 187px;
        background-color: #343434;
        color: #FFFFFFCC;
        padding: 20px;
        box-sizing: border-box;
        border-radius: 20px;
    }

    /* page quiz_completed */

    .summ-container {
        width: 1200px;
        height: 336px;
        /* Specify max-height for scrollability */
        position: absolute;
        top: 250px;
        left: 187px;
        background-color: #343434;
        color: #FFFFFFCC;
        padding: 20px;
        box-sizing: border-box;
        border-radius: 1cm;
    }
    ''')