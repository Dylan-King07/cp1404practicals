from flask import Flask

app = Flask(__name__)


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9/5 + 32


@app.route('/')
def hello_world():
    """Hello world page."""
    return '<h1>Hello World!</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    """Greet a user with or without a name."""
    return f"Hello {name}"


@app.route('/convert/<celsius>')
def convert(celsius):
    """Convert celsius value to fahrenheit."""
    try:
        celsius = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius)
        return f"{celsius} degrees celsius = {fahrenheit:.2f} degrees fahrenheit"
    except ValueError:
        return "Invalid input. Please enter a number."


if __name__ == '__main__':
    app.run()
