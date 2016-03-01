from flask import Flask,render_template,request
from forms import RegistrationForm
from dbModel import db, Profiles
import time
import os
from werkzeug import secure_filename

app=Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def home():
	return render_template("index.html")

@app.route('/profile',methods=['POST','GET'])
def profle():

	form = RegistrationForm(request.form)
	file=""
	notify=""
	if request.method == 'POST' and form.validate():
		file = request.files['file']
		notify="your profile has been saved! visit profiles/<idnum> to view profile"
		
		thisUser=Profiles(form.username.data,
		 	form.lname.data,form.fname.data,
		 	form.ID.data,form.sex.data,
		 	form.age.data,time.strftime("%d/%m/%Y"),file.filename)
		db.session.add(thisUser)
		db.session.commit()
		
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  
		


	return render_template('profile.html',form=form,notify=notify)



@app.route('/profiles',methods=['POST','GET'])
def profiles():
	profiles=Profiles.query.all()
	return render_template('profiles.html',profiles=profiles)

@app.route('/profile/<int:id>')
def userprofile(id):
	profile=Profiles.query.get(id)
	return render_template('userprofile.html',profile=profile)






if __name__=='__main__':
	app.run(host='0.0.0.0',debug=True)