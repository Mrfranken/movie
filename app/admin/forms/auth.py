from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, ValidationError
from app.models import Admin


class LoginForm(Form):
    user = StringField(
        validators=[DataRequired(message='user can not be empty'),
                    Length(4, 24, message='user length has to be range from 4 to 24')]
    )

    pwd = StringField(
        validators=[DataRequired(message='password can not be empty'),
                    Length(6, 18, message='password length has to be range from 6 to 18')]
    )

    # def validate_user(self, field):
    #     count = Admin.query.filter_by(name=field.data).count()
    #     if count == 0:
    #         raise ValidationError('user is not exist')
