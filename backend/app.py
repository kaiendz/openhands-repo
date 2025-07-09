

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'index'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    is_business = db.Column(db.Boolean, default=False)


class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    services = db.relationship('Service', backref='business', lazy=True)


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    confirmed = db.Column(db.Boolean, default=False)


@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], 
                    email=data['email'], 
                    password=hashed_password, 
                    is_business=data.get('is_business', False))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({'message': 'Logged in successfully'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/api/appointments', methods=['POST'])
@login_required
def book_appointment():
    data = request.get_json()
    new_appointment = Appointment(user_id=current_user.id, 
                                  service_id=data['service_id'], 
                                  appointment_time=datetime.strptime(data['appointment_time'], '%Y-%m-%d %H:%M'))
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({'message': 'Appointment booked successfully'}), 201


@app.route('/api/appointments/<int:appointment_id>/confirm', methods=['PATCH'])
@login_required
def confirm_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if appointment and appointment.service.business.user_id == current_user.id:
        appointment.confirmed = True
        db.session.commit()
        return jsonify({'message': 'Appointment confirmed'}), 200
    return jsonify({'message': 'Unauthorized action'}), 403




if __name__ == '__main__':
    with app.app_context():
        db.create_all()



    app.run(host='0.0.0.0', port=5000, debug=True)

