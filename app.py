from flask import Flask, render_template, request

app = Flask(__name__)

feedback_list = []  # To temporarily store feedbacks (in-memory)

@app.route('/', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        feedback = request.form['feedback']
        feedback_list.append({'name': name, 'feedback': feedback})
        return render_template('index.html', message="Thank you for your feedback!", feedbacks=feedback_list)
    return render_template('index.html', feedbacks=feedback_list)

if __name__ == '__main__':
    app.run(debug=True)