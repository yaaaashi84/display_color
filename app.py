from flask import Flask, render_template
import img

app = Flask(__name__)


@app.route("/")
def show_form():
    return render_template("index.html")


@app.route("/img")
def image():
    img.create_img()
    return render_template("img.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)

# r = random.randint(0, 255)
# g = random.randint(0, 255)
# b = random.randint(0, 255)
# img = Image.new("RGB", (300, 300), (r, g, b))
# img.save("/static/random_color.gif")
# img.show("/static/random_colr.gif")
