from flask import Flask, render_template,request
from popularity_checker import get_most_popular, check_popularity
app = Flask(__name__)

@app.route('/',methods = ['GET'])
@app.route('/popularity', methods=['GET', 'POST'])
def popularity():
    if request.method == 'POST':
        article = request.form['article']
        most_popular = get_most_popular()
        if check_popularity(article, most_popular):
            should_use_for_learning = ''
        else:
            should_use_for_learning = 'not '
        return render_template('age.html', should_use=should_use_for_learning)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
