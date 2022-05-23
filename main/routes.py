from main import app,db
from flask import redirect, render_template,request,url_for
from main.model import Degerler

@app.route('/', methods=['GET','POST'])
def index():
    content = Degerler.query.all()
    if request.method == "GET":
        text = request.args.get('toprakNem')
        print(text)
        if text:
            toprakNem = request.args.get('toprakNem')
            yagmur = request.args.get('yagmur')
            isik = request.args.get('isik')
            havaNem = request.args.get('havaNem')
            havaSicaklik = request.args.get('havaSicaklik')
            print(toprakNem)
            content_to_create = Degerler(toprakNem = toprakNem, yagmur=yagmur, isik=isik, havaNem=havaNem, havaSicaklik=havaSicaklik)
            db.session.add(content_to_create)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('index.html', content=content)