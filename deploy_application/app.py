from flask import Flask  , render_template , redirect , request
import Predictions 

# in this folder __name__ == __main__
app = Flask(__name__)

ans = Predictions.predict("not bad")
print(ans )
@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/' , methods = [ 'POST'])
def marks():
    if request.method =='POST':
        rev = request.form['review']
        ans = Predictions.predict(rev)
        return ans 



if __name__ == "__main__":
    app.run(debug = True)
