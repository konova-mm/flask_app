from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://www.adorama.com/alc/wp-content/uploads/2021/05/bird-wings-flying-feature.gif",
    "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/5eeea355389655.59822ff824b72.gif",
    "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/5eeea355389655.59822ff824b72.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
