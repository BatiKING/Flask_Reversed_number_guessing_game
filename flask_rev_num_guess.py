from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/numguess", methods=['GET', 'POST'])
def num_guess():
    """Main game function - asks player to give hints to CPU by pressing html buttons"""
    min_num = 0
    max_num = 1001
    guess_count = 1
    guess = calc_guess(min_num, max_num)
    if request.method == 'GET':
        return f"""
        <html>
            <body>
                <h1>Think of a number in range 0-1000 and I will guess it in 10 tries max</h1>
                <br>
                <h2>My guess is {guess}</h2>
                <br>
                <form method="POST">
                    <input type="hidden" name="min" value="{min_num}">
                    <input type="hidden" name="max" value="{max_num}">
                    <input type="hidden" name="guess" value="{guess}">
                    <input type="hidden" name="guess_count" value="{guess_count}">
                    <button type="submit" name="form_button" value="too_small">Too small!</button>
                    <button type="submit" name="form_button" value="too_big">Too big!</button>
                    <button type="submit" name="form_button" value="correct">Correct!</button>
                </form>
            </body>
        </html>
        """
    elif request.method == 'POST':
        if request.form['form_button'] == 'correct':
            return f"<h1>I Win! <br> I guessed it in {request.form['guess_count']} tries!</h1> "
        elif request.form['form_button'] == 'too_small':
            min_num = int(request.form['guess'])
            max_num = int(request.form['max'])
            guess = calc_guess(min_num, max_num)
            guess_count = int(request.form['guess_count']) + 1
        elif request.form['form_button'] == 'too_big':
            min_num = int(request.form['min'])
            max_num = int(request.form['guess'])
            guess = calc_guess(min_num, max_num)
            guess_count = int(request.form['guess_count']) + 1
        else:
            return "<h1>Something went wrong!</h1>"

        return f"""
        <html>
            <body>
                <h1>Think of a number in range 0-1000 and I will guess it in 10 tries max</h1>
                <br>
                <h2>My guess is {guess}</h2>
                <br>
                <form method="POST">
                    <input type="hidden" name="min" value="{min_num}">
                    <input type="hidden" name="max" value="{max_num}">
                    <input type="hidden" name="guess" value="{guess}">
                    <input type="hidden" name="guess_count" value="{guess_count}">
                    <button type="submit" name="form_button" value="too_small">Too small!</button>
                    <button type="submit" name="form_button" value="too_big">Too big!</button>
                    <button type="submit" name="form_button" value="correct">Correct!</button>
                </form>
            </body>
        </html>
        """




def calc_guess(min_arg, max_arg):
    """Calculating next CPU guess"""
    return int((max_arg - min_arg) / 2) + min_arg


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
