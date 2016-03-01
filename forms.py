from wtforms import Form, BooleanField, TextField, PasswordField, SelectField,FileField,validators

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=3, max=25)])
    fname = TextField('First name', [validators.Length(min=3, max=25)])
    lname=TextField('Last name', [validators.Length(min=3, max=25)])
    age=TextField('Age', [validators.Length(min=1, max=25)])
    ID=TextField('Enter ID Number', [validators.Length(min=3, max=25)])
    sex = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')])
    image = FileField('file')

    

class LoginForm(Form):
	username=TextField('Username', [validators.Length(min=3, max=25)])
	password= PasswordField('New Password', [
        validators.Required()])