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


def newhtml():
    print('''
    <!DOCTYPE html>
    <html lang="en">

    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Make It Stick </title>

    <!-- 
        - favicon
    -->
    <link rel="shortcut icon" href="./favicon.svg" type="image/svg+xml">
    <link rel="icon" type="image/svg+xml" href="/assets/images/favicon.svg">
    <link rel="icon" type="image/png" href="/assets/images/favicon.png">

    <!-- 
        - custom css link
    -->
    <link rel="stylesheet" href="./assets/css/style.css">

    <!-- 
        - google font link
    -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Mulish:wght@600;700;900&family=Quicksand:wght@400;500;600;700&display=swap"
        rel="stylesheet">
    </head>

    <body>

    <!-- 
        - HEADER
    -->

    <header class="header" data-header>
        <div class="container">

        <a href="#" class="logo">
            <img src="./assets/images/logo.svg" alt="Make It Stick logo">
        </a>

        <button class="menu-toggle-btn" data-nav-toggle-btn>
            <ion-icon name="menu-outline"></ion-icon>
        </button>

        <nav class="navbar">
            <ul class="navbar-list">

            <li>
                <a href="#hero" class="navbar-link">Home</a>
            </li>

            <li>
                <a href="#features" class="navbar-link">Features</a>
            </li>

            <li>
                <a href="#benefits" class="navbar-link">Benefits</a>
            </li>

            <li>
                <a href="#blog" class="navbar-link">Blog</a>
            </li>

            <li>
                <a href="#contact" class="navbar-link">Contact Us</a>
            </li>

            </ul>

        </nav>

        </div>
    </header>





    <main>
        <article>

        <!-- 
            - HERO
        -->

        <section class="hero" id="hero">
            <div class="container">

            <div class="hero-content">
                <h1 class="h1 hero-title">The Scientific Way of Learning!</h1>

                <p class="hero-text">
                Enhance your learning by generate questions from uploaded PDFs, instant feedback and tailored summaries using active learning principle.
                </p>

                <!-- <div class="btn-group">
                    <button class="btn btn-primary">Get Started</button>

                </div> -->

                <form action="" class="hero-form">
                <input type="email" name="email" required placeholder="Enter Your Email" class="email-field">

                <button type="submit" class="btn btn-primary">Subscribe</button>
                </form>
            </div>

            <figure class="hero-banner">
                <img src="./assets/images/hero-banner.png" alt="Hero image">
            </figure>

            </div>
        </section>





        <!-- 
            - About
        -->

        <section class="about" id="features">
            <div class="container">

            <div class="about-content">

                <div class="about-icon">
                <ion-icon name="cube"></ion-icon>
                </div>

                <h2 class="h2 about-title">Our Key Features</h2>

                <p class="about-text">
                Nam libero tempore cum soluta as nobis est eligendi optio cumque nihile impedite quo minus id quod maxime.
                </p>

                <button class="btn btn-outline">Learn More</button>

            </div>

            <ul class="about-list">

                <li>
                <div class="about-card">

                    <div class="card-icon">
                    <ion-icon name="thumbs-up"></ion-icon>
                    </div>

                    <h3 class="h3 card-title">PDF Upload</h3>

                    <p class="card-text">
                    Users can upload PDF documents to the web application.
                    </p>

                </div>
                </li>

                <li>
                <div class="about-card">

                    <div class="card-icon">
                    <ion-icon name="trending-up"></ion-icon>
                    </div>

                    <h3 class="h3 card-title">Question Generation</h3>

                    <p class="card-text">
                    The application automatically generates questions based on the content of the uploaded PDF.
                    </p>

                </div>
                </li>

                <li>
                <div class="about-card">

                    <div class="card-icon">
                    <ion-icon name="shield-checkmark"></ion-icon>
                    </div>

                    <h3 class="h3 card-title">Interactive Quizzing</h3>

                    <p class="card-text">
                    Interact with the generated questions, providing answers.
                    </p>

                </div>
                </li>

                <li>
                <div class="about-card">

                    <div class="card-icon">
                    <ion-icon name="server"></ion-icon>
                    </div>

                    <h3 class="h3 card-title">Answer Evaluation</h3>

                    <p class="card-text">
                    The system evaluates user-provided answers to determine correctness.
                    </p>

                </div>
                </li>

            </ul>

            </div>
        </section>





        <!-- 
            -  BENIFITS
        -->

        <section class="features" id="benefits">
            <div class="container">

            <h2 class="h2 section-title">Benefits</h2>

            <p class="section-text">
                Et harum quidem rerum facilis est et expedita distinctio nam libero tempore cum soluta nobis eligendi
                cumque.
            </p>

            <div class="features-wrapper">

                <figure class="features-banner">
                <img src="./assets/images/features-img-1.png" alt="illustration art">
                </figure>

                <div class="features-content">

                <p class="features-content-subtitle">
                    <ion-icon name="sparkles"></ion-icon>

                    <span>Active Learning</span>
                </p>

                <h3 class="features-content-title">
                    Build <strong>community</strong> & <strong>conversion</strong> with our suite of <strong>social
                    tool</strong>
                </h3>

                <p class="features-content-text">
                    Temporibus autem quibusdam et aut officiis debitis aut rerum a necessitatibus saepe eveniet ut et
                    voluptates repudiandae
                    sint molestiae non recusandae itaque.
                </p>

                <ul class="features-list">

                    <li class="features-list-item">
                    <ion-icon name="layers-outline"></ion-icon>

                    <p>Donec pede justo fringilla vel nec.</p>
                    </li>

                    <li class="features-list-item">
                    <ion-icon name="megaphone-outline"></ion-icon>

                    <p>Cras ultricies mi eu turpis hendrerit fringilla.</p>
                    </li>

                </ul>

                <!-- <div class="btn-group">
                    <button class="btn btn-primary">Read More</button>

                </div> -->

                </div>

            </div>

            <div class="features-wrapper">

                <figure class="features-banner">
                <img src="./assets/images/features-img-2.png" alt="illustration art">
                </figure>

                <div class="features-content">

                <p class="features-content-subtitle">
                    <ion-icon name="sparkles"></ion-icon>

                    <span>Efficiency</span>
                </p>

                <h3 class="features-content-title">
                    We do the work you <strong>stay focused</strong> on <strong>your customers.</strong>
                </h3>

                <p class="features-content-text">
                    Temporibus autem quibusdam et aut officiis debitis aut rerum a necessitatibus saepe eveniet ut et
                    voluptates repudiandae
                    sint molestiae non recusandae itaque.
                </p>

                <ul class="features-list">

                    <li class="features-list-item">
                    <ion-icon name="rocket-outline"></ion-icon>

                    <p>Donec pede justo fringilla vel nec.</p>
                    </li>

                    <li class="features-list-item">
                    <ion-icon name="wifi-outline"></ion-icon>

                    <p>Cras ultricies mi eu turpis hendrerit fringilla.</p>
                    </li>

                </ul>

                <div class="btn-group">
                    <!-- <button class="btn btn-primary">Read More</button> -->
                </div>

                </div>

            </div>

            <div class="features-wrapper">

                <figure class="features-banner">
                <img src="./assets/images/features-img-1.png" alt="illustration art">
                </figure>

                <div class="features-content">

                <p class="features-content-subtitle">
                    <ion-icon name="sparkles"></ion-icon>

                    <span>Accessibility</span>
                </p>

                <h3 class="features-content-title">
                    Build <strong>community</strong> & <strong>conversion</strong> with our suite of <strong>social
                    tool</strong>
                </h3>

                <p class="features-content-text">
                    Temporibus autem quibusdam et aut officiis debitis aut rerum a necessitatibus saepe eveniet ut et
                    voluptates repudiandae
                    sint molestiae non recusandae itaque.
                </p>

                <ul class="features-list">

                    <li class="features-list-item">
                    <ion-icon name="layers-outline"></ion-icon>

                    <p>Donec pede justo fringilla vel nec.</p>
                    </li>

                    <li class="features-list-item">
                    <ion-icon name="megaphone-outline"></ion-icon>

                    <p>Cras ultricies mi eu turpis hendrerit fringilla.</p>
                    </li>

                </ul>

                <div class="btn-group">
                    <!-- <button class="btn btn-primary">Read More</button> -->
                </div>

                </div>

            </div>

            </div>
        </section>





        <!-- 
            - BLOG
        -->

        <section class="blog" id="blog">
            <div class="container">

            <h2 class="h2 section-title">Our Articles</h2>

            <p class="section-text">
                Et harum quidem rerum facilis est et expedita distinctio nam
            </p>

            <ul class="blog-list">

                <li>
                <div class="blog-card">

                    <figure class="blog-banner">
                    <img src="./assets/images/blog-banner-1.jpg" alt="Best Traveling Place">
                    </figure>

                    <div class="blog-meta">

                    <span>
                        <ion-icon name="calendar-outline"></ion-icon>

                        <time datetime="2024-03-01">March 1 2024</time>
                    </span>

                    </div>

                    <h3 class="blog-title">What is Make it Stick</h3>

                    <p class="blog-text">
                    Integer ante arcu accumsan a consectetuer eget posuere mauris praesent adipiscing phasellus
                    ullamcorper ipsum rutrum
                    punc.
                    </p>

                    <a href="#" class="blog-link-btn">
                    <span>Learn More</span>

                    <ion-icon name="chevron-forward-outline"></ion-icon>
                    </a>

                </div>
                </li>

                <li>
                <div class="blog-card">

                    <figure class="blog-banner">
                    <img src="./assets/images/blog-banner-2.jpg" alt="Private Meeting Room">
                    </figure>

                    <div class="blog-meta">

                    <span>
                        <ion-icon name="calendar-outline"></ion-icon>

                        <time datetime="2024-03-01">March 1 2024</time>
                    </span>

                    </div>

                    <h3 class="blog-title">How to use Make it Stick Application</h3>

                    <p class="blog-text">
                    Integer ante arcu accumsan a consectetuer eget posuere mauris praesent adipiscing phasellus
                    ullamcorper ipsum rutrum
                    punc.
                    </p>

                    <a href="#" class="blog-link-btn">
                    <span>Learn More</span>

                    <ion-icon name="chevron-forward-outline"></ion-icon>
                    </a>

                </div>
                </li>

                <li>
                <div class="blog-card">

                    <figure class="blog-banner">
                    <img src="./assets/images/blog-banner-3.jpg" alt="The Best Business Ideas">
                    </figure>

                    <div class="blog-meta">

                    <span>
                        <ion-icon name="calendar-outline"></ion-icon>

                        <time datetime="2024-03-01">March 1 2024</time>
                    </span>

                    </div>

                    <h3 class="blog-title">How to uplod PDFs</h3>

                    <p class="blog-text">
                    Integer ante arcu accumsan a consectetuer eget posuere mauris praesent adipiscing phasellus
                    ullamcorper ipsum rutrum
                    punc.
                    </p>

                    <a href="#" class="blog-link-btn">
                    <span>Learn More</span>

                    <ion-icon name="chevron-forward-outline"></ion-icon>
                    </a>

                </div>
                </li>

            </ul>

            </div>
        </section>





        <!-- 
            - CONTACT
        -->

        <section class="contact" id="contact">
            <div class="container">

            <h2 class="h2 section-title">Wanna Talk to us!</h2>

            <p class="section-text">
                Et harum quidem rerum facilis est et expedita distinctio nam libero tempore cum soluta nobis eligendi
                cumque.
            </p>

            <div class="contact-wrapper">

                <form action="form-process.php" method="POST" class="contact-form">

                <div class="wrapper-flex">

                    <div class="input-wrapper">
                    <label for="name">Name*</label>

                    <input type="text" name="name" id="name" required placeholder="Enter Your Name" class="input-field">
                    </div>

                    <div class="input-wrapper">
                    <label for="emai">Email*</label>

                    <input type="text" name="email" id="email" required placeholder="Enter Your Email"
                        class="input-field">
                    </div>

                </div>

                <label for="message">Message*</label>

                <textarea name="message" id="message" required placeholder="Type Your Message"
                    class="input-field"></textarea>

                <button type="submit" class="btn btn-primary">
                    <span>Send Message</span>

                    <ion-icon name="paper-plane-outline"></ion-icon>
                </button>

                </form>

                <ul class="contact-list">

                <li>
                    <a href="mailto:support@website.com" class="contact-link">
                    <ion-icon name="mail-outline"></ion-icon>

                    <span>: contact@makeitstick.com</span>
                    </a>
                </li>

                <li>
                    <a href="#" class="contact-link">
                    <ion-icon name="globe-outline"></ion-icon>

                    <span>: www.makeitstick.com</span>
                    </a>
                </li>

                <li>
                    <a href="tel:+0011234567890" class="contact-link">
                    <ion-icon name="call-outline"></ion-icon>

                    <span>: (+001) 123 456 7890</span>
                    </a>
                </li>

                <li>
                    <div class="contact-link">
                    
                    </div>
                </li>

                <li>
                    <a href="#" class="contact-link">
                </li>

                </ul>

            </div>

            </div>
        </section>

        </article>
    </main>





    <!-- 
        - FOOTER
    -->

    <footer>

        <div class="footer-top">
        <div class="container">

            <div class="footer-brand">

            <a href="#" class="logo">
                <img src="./assets/images/logo-footer.svg" alt="Make It Stick logo">
            </a>

            <p class="footer-text">
                Enhance your learning by generate questions from uploaded PDFs, instant feedback and tailored summaries using active learning principle.
            </p>

            <ul class="social-list">

                <li>
                <a href="#" class="social-link">
                    <ion-icon name="logo-facebook"></ion-icon>
                </a>
                </li>

                <li>
                <a href="#" class="social-link">
                    <ion-icon name="logo-twitter"></ion-icon>
                </a>
                </li>

                <li>
                <a href="#" class="social-link">
                    <ion-icon name="logo-instagram"></ion-icon>
                </a>
                </li>

                <li>
                <a href="#" class="social-link">
                    <ion-icon name="logo-linkedin"></ion-icon>
                </a>
                </li>

            </ul>

            </div>

            <div class="footer-link-box">

            <ul class="footer-list">

                <li>
                <p class="footer-item-title">ABOUT US</p>
                </li>

                <li>
                <a href="#" class="footer-link">Features</a>
                </li>

                <li>
                <a href="#" class="footer-link">Benifits</a>
                </li>

                <li>
                <a href="#" class="footer-link">Articles</a>
                </li>


                <li>
                <a href="#" class="footer-link">Mission</a>
                </li>

            </ul>

            

            <ul class="footer-list">

                <li>
                <p class="footer-item-title">SUPPORT</p>
                </li>

                <li>
                <a href="#" class="footer-link">Developers</a>
                </li>

                <li>
                <a href="#" class="footer-link">Support</a>
                </li>

                <li>
                <a href="#" class="footer-link">Customer Service</a>
                </li>

                <li>
                <a href="#" class="footer-link">Get Started</a>
                </li>

                <li>
                <a href="#" class="footer-link">Guide</a>
                </li>

            </ul>

            </div>

        </div>
        </div>

        <div class="footer-bottom">
        <div class="container">
            <p class="copyright">
            &copy; 2024 <a href="">Make It Stick</a>. All Right Reserved
            </p>
        </div>
        </div>

    </footer>





    <!-- 
        - custom js link
    -->
    <script src="./assets/js/script.js"></script>

    <!-- 
        - ionicon link
    -->
    <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>

    </body>

    </html>
    ''')


def newcss():
    print('''
    :root {

    /**
    * colors
    */

    --raisin-black-2: hsl(245, 16%, 16%);
    --raisin-black-1: hsl(244, 17%, 19%);
    --majorelle-blue: hsl(245, 67%, 59%);
    --ghost-white-1: hsl(240, 100%, 99%);
    --ghost-white-2: hsl(228, 50%, 96%);
    --white-opacity: hsla(0, 0%, 100%, 0.5);
    --independence: hsl(245, 17%, 27%);
    --lavender-web: hsl(247, 69%, 95%);
    --eerie-black: hsl(210, 11%, 15%);
    --cool-gray: hsl(244, 17%, 61%);
    --sapphire: hsl(211, 100%, 35%);
    --white: hsl(0, 0%, 100%);

    /**
    * typography
    */

    --ff-quicksand: "Quicksand", sans-serif;
    --ff-mulish: "Mulish", sans-serif;

    --fs-1: 36px;
    --fs-2: 28px;
    --fs-3: 20px;
    --fs-4: 17px;
    --fs-5: 16px;
    --fs-6: 15px;
    --fs-7: 14px;

    --fw-500: 500;
    --fw-600: 600;
    --fw-700: 700;

    /**
    * transition
    */

    --transition: 0.25s ease;

    /**
    * spacing
    */

    --section-padding: 80px;

    }





    /*-----------------------------------*\
    #RESET
    \*-----------------------------------*/

    *, *::before, *::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    }

    li { list-style: none; }

    a { text-decoration: none; }

    a,
    img,
    span,
    input,
    label,
    button,
    ion-icon,
    textarea { display: block; }

    button {
    border: none;
    background: none;
    font: inherit;
    cursor: pointer;
    }

    input,
    textarea {
    border: none;
    font: inherit;
    width: 100%;
    }

    html {
    font-family: var(--ff-quicksand);
    scroll-behavior: smooth;
    }

    body { background: var(--white); }





    /*-----------------------------------*\
    #REUSED STYLE
    \*-----------------------------------*/

    .container { padding-inline: 15px; }

    .h1,
    .h2,
    .h3 {
    color: var(--independence);
    font-family: var(--ff-mulish);
    line-height: 1.2;
    }

    .h1 { font-size: var(--fs-1); }

    .h2 { font-size: var(--fs-2); }

    .h3 { font-size: var(--fs-3); }

    .btn {
    font-size: var(--fs-6);
    font-weight: var(--fw-700);
    padding: 15px 30px;
    border-radius: 4px;
    transition: var(--transition);
    }

    .btn:is(:hover, :focus) { transform: translateY(-2px); }

    .btn-primary {
    background: var(--majorelle-blue);
    color: var(--white);
    }

    .btn-primary:is(:hover, :focus) {
    --majorelle-blue: hsl(245, 67%, 55%);
    box-shadow: 0 3px 10px hsla(245, 67%, 59%, 0.5);
    }

    .btn-outline { 
    border: 1px solid var(--majorelle-blue);
    color: var(--majorelle-blue);
    }

    .btn-outline:is(:hover, :focus) {
    background: var(--majorelle-blue);
    color: var(--white);
    box-shadow: 0 3px 10px hsla(245, 67%, 59%, 0.5);
    }

    .btn-secondary {
    background: hsla(245, 67%, 59%, 0.15);
    color: var(--majorelle-blue);
    }

    .section-title { text-align: center; }

    .section-text {
    color: var(--cool-gray);
    font-size: var(--fs-6);
    line-height: 1.7;
    text-align: center;
    }





    /*-----------------------------------*\
    #HEADER
    \*-----------------------------------*/

    .header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: var(--white);
    padding-block: 20px;
    box-shadow: 0 1px 2px hsla(0, 0%, 0%, 0.05);
    height: 65px;
    overflow: hidden;
    transition: 0.5s ease-in-out;
    z-index: 4;
    }

    .header.active { height: 330px; }

    .header .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    }

    .menu-toggle-btn { font-size: 25px; }

    .navbar {
    position: absolute;
    width: 100%;
    top: 64px;
    left: 0;
    padding-inline: 30px;
    visibility: hidden;
    opacity: 0;
    transition: 0.5s ease-in-out;
    }

    .header.active .navbar {
    visibility: visible;
    opacity: 1;
    }

    .navbar-link,
    .header-action-link {
    color: var(--cool-gray);
    font-size: var(--fs-6);
    font-family: var(--ff-mulish);
    padding-block: 8px;
    }

    :is(.navbar-link, .header-action-link):is(:hover, :focus) { color: var(--majorelle-blue); }





    /*-----------------------------------*\
    #HERO
    \*-----------------------------------*/

    .hero {
    padding: 125px 0 var(--section-padding);
    background: var(--ghost-white-1);
    }

    .hero-content { margin-bottom: 80px; }

    .hero-title { margin-bottom: 25px; }

    .hero-text {
    color: var(--cool-gray);
    font-size: var(--fs-4);
    font-weight: var(--fw-500);
    line-height: 1.8;
    margin-bottom: 40px;
    }

    .form-text {
    color: var(--independence);
    font-weight: var(--fw-500);
    line-height: 1.8;
    margin-bottom: 20px;
    }

    .form-text span {
    display: inline-block;
    font-size: 20px;
    }

    .email-field {
    background: var(--ghost-white-2);
    padding: 17px 20px;
    border-radius: 8px;
    margin-bottom: 20px;
    }

    .email-field:focus { outline-color: var(--majorelle-blue); }

    .hero .btn-primary { margin-inline: auto; }

    .hero-banner img { width: 100%; }





    /*-----------------------------------*\
    #ABOUT
    \*-----------------------------------*/

    .about { padding-block: var(--section-padding); }

    .about-content { margin-bottom: 30px; }

    .about-icon {
    width: 60px;
    height: 60px;
    background: var(--lavender-web);
    display: grid;
    place-items: center;
    color: var(--majorelle-blue);
    font-size: 40px;
    border-radius: 4px;
    margin-bottom: 20px;
    }

    .about-title { margin-bottom: 10px; }

    .about-text {
    color: var(--cool-gray);
    font-weight: var(--fw-500);
    line-height: 1.8;
    margin-bottom: 20px;
    }

    .about-list {
    display: grid;
    gap: 20px;
    }

    .about-card {
    padding: 20px;
    text-align: center;
    box-shadow: 0 3px 12px hsla(233, 77%, 10%, 0.06);
    border-radius: 4px;
    transition: var(--transition);
    }

    .about-card:hover {
    background: var(--majorelle-blue);
    transform: translateY(-5px);
    box-shadow: 0 5px 18px hsla(245, 67%, 59%, 0.4);
    }

    .about-card .card-icon {
    width: 60px;
    height: 60px;
    background: var(--lavender-web);
    display: grid;
    place-items: center;
    color: var(--majorelle-blue);
    font-size: 28px;
    border-radius: 50%;
    margin-inline: auto;
    margin-bottom: 20px;
    transition: var(--transition);
    }

    .about-card:hover .card-icon {
    background: hsla(0, 0%, 100%, 0.15);
    color: var(--white);
    box-shadow: 0 0 0 8px hsla(0, 0%, 100%, 0.05);
    }

    .about-card .card-title {
    margin-bottom: 10px;
    transition: var(--transition);
    }

    .about-card:hover .card-title { color: var(--white); }

    .about-card .card-text {
    color: var(--cool-gray);
    font-size: var(--fs-6);
    font-weight: var(--fw-500);
    line-height: 1.8;
    transition: var(--transition);
    }

    .about-card:hover .card-text { color: hsla(0, 0%, 100%, 0.5); }





    /*-----------------------------------*\
    #FEATURES
    \*-----------------------------------*/

    .features {
    padding-block: var(--section-padding);
    background: var(--ghost-white-1);
    }

    .features .section-title { margin-bottom: 15px; }

    .features .section-text { margin-bottom: 60px; }

    .features-wrapper:not(:last-child) { margin-bottom: 80px; }

    .features-banner { margin-bottom: 35px; }

    .features-banner img { width: 100%; }

    .features-content-subtitle {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: var(--fs-5);
    color: var(--eerie-black);
    margin-bottom: 20px;
    }

    .features-content-subtitle ion-icon {
    color: var(--majorelle-blue);
    font-size: 20px;
    }

    .features-content-title {
    font-size: var(--fs-2);
    font-family: var(--ff-mulish);
    color: var(--independence);
    font-weight: var(--fw-600);
    margin-bottom: 25px;
    }

    .features-content-title strong { font-weight: var(--fw-700); }

    .features-content-text {
    font-size: var(--fs-6);
    color: var(--cool-gray);
    line-height: 1.7;
    margin-bottom: 25px;
    }

    .features-list { margin-bottom: 40px; }

    .features-list-item {
    display: flex;
    align-items: flex-start;
    gap: 5px;
    font-size: var(--fs-5);
    color: var(--cool-gray);
    margin-bottom: 10px;
    }

    .features-list-item ion-icon { font-size: 23px; }

    .features-list-item p { width: calc(100% - 28px); }

    .features-wrapper:last-child {
    display: flex;
    flex-direction: column-reverse;
    }

    .btn-group {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
    align-items: flex-start;
    gap: 10px;
    }





    /*-----------------------------------*\
    #BLOG
    \*-----------------------------------*/

    .blog { padding-block: var(--section-padding); }

    .blog .section-title { margin-bottom: 20px; }

    .blog .section-text { margin-bottom: 40px; }

    .blog-list {
    display: grid;
    gap: 30px;
    }

    .blog-banner { margin-bottom: 20px; }

    .blog-banner img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 4px;
    }

    .blog-meta {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    gap: 20px;
    font-size: var(--fs-6);
    text-transform: uppercase;
    color: var(--cool-gray);
    margin-bottom: 10px;
    }

    .blog-meta span {
    display: flex;
    align-items: center;
    gap: 5px;
    }

    .blog-title {
    font-size: var(--fs-3);
    color: var(--independence);
    }

    .blog-text {
    color: var(--cool-gray);
    font-size: var(--fs-6);
    line-height: 1.7;
    margin-bottom: 15px;
    }

    .blog-link-btn {
    display: flex;
    align-items: center;
    gap: 5px;
    color: var(--majorelle-blue);
    font-weight: var(--fw-600);
    }

    .blog-link-btn:is(:hover, :focus) { color: var(--sapphire); }





    /*-----------------------------------*\
    #CONTACT
    \*-----------------------------------*/

    .contact {
    padding-block: var(--section-padding);
    background: var(--ghost-white-1);
    }

    .contact .section-title { margin-bottom: 15px; }

    .contact .section-text { margin-bottom: 60px; }

    .contact-form { margin-bottom: 50px; }

    .input-wrapper { margin-bottom: 20px; }

    .contact label {
    color: var(--independence);
    font-weight: var(--fw-500);
    margin-bottom: 10px;
    }

    .contact .input-field {
    background: transparent;
    color: var(--independence);
    font-size: var(--fs-7);
    padding: 10px 15px;
    border: 1px solid hsla(244, 17%, 67%, 0.3);
    border-radius: 4px;
    }

    .contact .input-field:focus {
    outline: none;
    background: var(--ghost-white-2);
    }

    .contact .input-field::placeholder { color: var(--cool-gray); }

    textarea.input-field {
    margin-bottom: 20px;
    resize: vertical;
    min-height: 50px;
    height: 100px;
    max-height: 200px;
    }

    .contact .btn-primary {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    }

    .contact .btn-primary ion-icon { --ionicon-stroke-width: 40px; }

    .contact-list li:not(:last-child) { margin-bottom: 25px; }

    .contact-link {
    color: var(--cool-gray);
    font-weight: var(--fw-500);
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    gap: 5px;
    }

    .contact-link ion-icon {
    font-size: 20px;
    --ionicon-stroke-width: 30px;
    }

    .contact-link :is(span, address) { width: calc(100% - 25px); }

    .contact-link address { font-style: normal; }





    /*-----------------------------------*\
    #FOOTER
    \*-----------------------------------*/

    footer {
    background: var(--raisin-black-1);
    color: var(--white-opacity);
    font-weight: var(--fw-500);
    }

    .footer-top { padding-block: var(--section-padding); }

    .footer-brand { margin-bottom: 60px; }

    footer .logo { margin-bottom: 25px; }

    .footer-text {
    font-size: var(--fs-6);
    line-height: 1.8;
    margin-bottom: 25px;
    }

    .social-list {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    gap: 20px;
    }

    .social-link {
    color: var(--white-opacity);
    font-size: 25px;
    transition: var(--transition);
    }

    .social-link:is(:hover, :focus) { color: var(--white); }

    .footer-link-box {
    display: grid;
    gap: 50px;
    }

    .footer-list li:first-child { margin-bottom: 20px; }

    .footer-item-title {
    color: var(--white);
    font-family: var(--ff-mulish);
    font-weight: var(--fw-700);
    }

    .footer-link {
    color: var(--white-opacity);
    font-size: var(--fs-6);
    transition: var(--transition);
    padding-block: 10px;
    }

    .footer-link:is(:hover, :focus) {
    color: var(--white);
    transform: translateX(5px);
    }

    .footer-bottom {
    background: var(--raisin-black-2);
    padding-block: 20px;
    text-align: center;
    }

    .copyright a {
    display: inline-block;
    color: var(--white-opacity);
    transition: var(--transition);
    }

    .copyright a:is(:hover, :focus) { color: var(--white); }





    /*-----------------------------------*\
    #MEDIA QUERIES
    \*-----------------------------------*/

    /**
    * responsive for larger than 450px screen
    */

    @media (min-width: 450px) {

    /**
    * HERO
    */

    .hero-form { position: relative; }

    .email-field {
        margin-bottom: 0;
        padding-right: 155px;
    }

    .hero .btn-primary {
        position: absolute;
        top: 5px;
        right: 5px;
        padding-block: 12.5px;
    }



    /**
    * ABOUT
    */

    .about-card .card-text {
        max-width: 300px;
        margin-inline: auto;
    }

    }





    /**
    * responsive for larger than 576px screen
    */

    @media (min-width: 576px) {

    /**
    * CUSTOM PROPERTY
    */

    :root {

        /**
        * typography
        */

        --fs-1: 52px;

    }



    /**
    * REUSED STYLE
    */

    .container {
        max-width: 525px;
        margin-inline: auto;
    }

    .section-text {
        max-width: 460px;
        margin-inline: auto;
        margin-bottom: 80px;
    }

    }





    /**
    * responsive for larger than 768px screen
    */

    @media (min-width: 768px) {

    /**
    * REUSED STYLE
    */

    .container { max-width: 720px; }

    .section-text { max-width: 645px; }



    /**
    * HERO
    */

    .hero :is(.hero-text, .form-text, .hero-form) { max-width: 520px; }

    .hero-banner {
        max-width: 600px;
        margin-inline: auto;
    }



    /**
    * ABOUT
    */

    .about-list { grid-template-columns: 1fr 1fr; }



    /**
    * CONTACT
    */

    .contact-form .wrapper-flex {
        display: flex;
        gap: 30px;
    }

    .wrapper-flex .input-wrapper { width: 50%; }



    /**
    * FOOTER
    */

    .footer-link-box { grid-template-columns: repeat(3, 1fr); }

    }





    /**
    * responsive for larger than 992px screen
    */

    @media (min-width: 992px) {

    /**
    * REUSED STYLE
    */

    .container { max-width: 950px; }

    .section-text { max-width: 450px; }



    /**
    * HEADER
    */

    .header {
        overflow: visible;
        padding-block: 0;
        height: unset;
    }

    .header.active { height: unset; }

    .menu-toggle-btn { display: none; }

    .navbar {
        position: static;
        visibility: visible;
        opacity: 1;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-inline: 0;
    }

    .navbar-list {
        display: flex;
        justify-content: center;
        align-items: center;
        width: max-content;
        gap: 40px;
        margin-inline: auto;
    }

    .header-actions {
        display: flex;
        align-items: center;
        gap: 40px;
    }

    .navbar-link,
    .header-action-link { padding-block: 25px; }



    /**
    * HERO
    */

    .hero .container {
        display: grid;
        grid-template-columns: 4fr 5fr;
        align-items: center;
        gap: 60px;
    }

    .hero-content { margin-bottom: 0; }



    /**
    * ABOUT
    */

    .about .container {
        display: flex;
        align-items: center;
        gap: 50px;
    }

    .about-content {
        margin-bottom: 0;
        width: 40%;
    }

    .about-list {
        gap: 30px;
        padding-bottom: 50px;
    }

    .about-list li:nth-child(odd) { transform: translateY(50px); }



    /**
    * FEATURES
    */

    .features-wrapper {
        display: grid !important;
        grid-template-columns: 1fr 1fr;
        align-items: center;
        gap: 90px;
    }

    .features-wrapper:not(:last-child) { margin-bottom: 100px; }

    .features-wrapper:last-child .features-banner {
        grid-column: 2 / 3;
        grid-row: 1 / 2;
    }



    /**
    * BLOG
    */

    .blog-list { grid-template-columns: repeat(3, 1fr); }

    .blog .section-text { margin-bottom: 50px; }



    /**
    * CONTACT
    */

    .contact-wrapper {
        display: grid;
        grid-template-columns: 3fr 2fr;
        gap: 80px;
        align-items: center;
    }

    .contact-form { margin-bottom: 0; }



    /**
    * FOOTER
    */

    .footer-top .container {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 50px;
    }

    .footer-brand {
        margin-bottom: 0;
        max-width: 300px;
    }

    .footer-list { width: 140px; }

    }





    /**
    * responsive for larger than 1200px screen
    */

    @media (min-width: 1200px) {

    /**
    * REUSED STYLE
    */

    .container { max-width: 1150px; }



    /**
    * HERO
    */

    .hero .container { gap: 150px; }



    /**
    * FOOTER
    */

    .footer-link-box { margin-right: 40px; }

    .footer-list { width: 170px; }

    }
    ''')