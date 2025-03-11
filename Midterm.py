from flask import Flask, render_template

app = Flask(__name__)

@app.route('/books')
def book_list():
    books= ["The Hunger Games by Jennifer Collins", 
            "Monument 14 by Emmy Melbourne",
            "Eighth Grade Bites by Heather Brewer",
            
            ]

    return  render_template ("amirsmidterm.html", books=books)

if __name__ == '__main__':
    app.run(debug=True)