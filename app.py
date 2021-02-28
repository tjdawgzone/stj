import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.debug = True
app.config["FILE_UPLOADS"] = "/Users/teerathamvitchutripop/Documents/teerathamprojects/sutayjee/test-download"
@app.route('/')


@app.route("/upload-file", methods=["GET", "POST"])
def upload_file():

    if request.method == "POST":

        if request.files:

                file = request.files["file"]
                filename = file.filename
                file.save(os.path.join(app.config["FILE_UPLOADS"], filename))
                print("File saved")
                return redirect(request.url)
    return render_template("index.html")



if __name__ == "__main__":
    app.run()
