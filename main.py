from flask import Flask, request

app = Flask("Gra w zgadywanie liczb 3")

min = 0
max = 1000
guess = 0
# hint = ""

def intro():
    intro = """
    <header>
    <h1>Guess The Number - Game</h1>
    <p>Think of a number from 0 to 1000.</p>
    <p>I will guess that number in max 10 attempts.</p>
    <p>Just give me hints using the buttons below.</p>
    </header>
    """
    return intro

def hints_menu():
    global min
    global max
    global guess
    global hint
    hints_form = f"""
    <form method='POST'>
    <input type='submit' value='Too small' name ='small'>
    <input type='submit' value='Too big' name ='big'>
    <input type='submit' value='You win!' name ='win'>
    <input type='hidden' name='min' value={min}>
    <input type='hidden' name='max' value={max}>
    </form>
    """
    guess = int(((max - min) / 2) + min)
    message = f"My guess is: {guess}"
    # if request.method == 'POST':
    #     if request.form.get('small'):
    #         hint = 'small'
    #     elif request.form.get('big'):
    #         hint = 'big'
    #     elif request.form.get('win'):
    #         hint = 'win'
    # return hints_menu
    if request.method == 'POST':
        if request.form.get('small'):
            min = guess
            guess = int(((max - min) / 2) + min)
            message = f"My guess is: {guess}"
        elif request.form.get('big'):
            max = guess
            guess = int(((max - min) / 2) + min)
            message = f"My guess is: {guess}"
        elif request.form.get('win'):
            final_message = "I win!"
            return final_message
    return hints_form + message

# def belly_of_the_beast(hint):
#     global min
#     global max
#     global guess
#     if hint =="small":
#         min = guess
#     elif hint == "big":
#         max = guess
#     elif hint == "win":
#         return False




@app.route("/", methods=['GET', 'POST'])
def game():
    while True:
        global guess
        global max
        global min
        global hint
        return intro() + hints_menu()
        # while True:
        #     if belly_of_the_beast(hint) is False:
        #         final_message = "I win! Thanks for playing!"
        #         return intro() + hints_menu() + final_message
        #     else:
        #         guess = int(((max - min) / 2) + min)
        #         message = f"My guess is: {guess}"
        #         belly_of_the_beast(hint)
        #         return intro() + hints_menu() + message

app.run()
