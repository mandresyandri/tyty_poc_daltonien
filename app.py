from flask import Flask, render_template, request
from blind_friendly import blind_optimized

app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def index(): 
    image_url = None
    output_image = None  # Initialize output_image here
    if request.method == 'POST':
        image_url = request.form.get('image_url')
        output_image = blind_optimized(image_url, "image_2")
        
    return render_template("index.html", image_url=image_url, output_image=output_image)

# if  __name__ == "__main__":
#     app.run(debug=True)