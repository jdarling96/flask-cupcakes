
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, RadioField
from wtforms.validators import InputRequired, Optional

class AddCupCake(FlaskForm):
    """Form for adding cupcakes"""

    flavor = StringField("Flavor", validators=[InputRequired()])

    size = RadioField("Size", choices=[('small','small'),('medium','medium'),('large','large')], 
    validators=[InputRequired()])
    
    rating = FloatField("Rating", validators=[InputRequired()])
    
    image = StringField('Image URL', validators=[Optional()], 
    default='https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg')
