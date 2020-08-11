from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length


class TageForm(Form):
    name = StringField(
        validators=[DataRequired(message='标签名不能为空'),
                    Length(min=2, max=16, message='标签长度应为1到4')]
    )
