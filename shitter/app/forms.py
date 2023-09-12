from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User

# class used to make the login form work and interact with the data base
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# calss to make the registraition work. username, email and passowrd check
class RegestraionForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

# class to check if the users username is allready taken
def validate_username(self, username):
    user = User.query.filer_by(username=username.data).first()
    if user is not None:
        raise ValidationError('Please use a different username, you are not uniqe')
    
# class to see if some one else already registed with this email
def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user is not None:
        raise ValidationError('Please dont use other ppl emails')

# class to allow a person to change their profile.
class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    # some scary shit
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    # checking username validaion again
    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please dont copy others')
            
class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


# class for making posts
class PostForm(FlaskForm):
    post = TextAreaField('Enter your brain trash', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit= SubmitField('Submit')