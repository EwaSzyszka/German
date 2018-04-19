# -*- coding: utf-8 -*-
from flask import Flask, render_template,request
from popularity_checker import get_most_popular, check_popularity
import numpy as np
app = Flask(__name__)

@app.route('/',methods = ['GET'])
@app.route('/popularity', methods=['GET', 'POST'])
def popularity():
    if request.method == 'POST':
        article = request.form['article']
        most_popular = get_most_popular()
        estential_vocab = check_popularity(article, most_popular)
        if len(np.unique(estential_vocab)) > 2:
            should_use_for_learning = ''
        else:
            should_use_for_learning = 'not '
#            #v = estential_vocab[0]
            
        return render_template('age.html', should_use=should_use_for_learning,voca=', '.join(estential_vocab))
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
