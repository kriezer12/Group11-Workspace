from app import app
from models.db import db
from models.user_model import User
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def seed_data():
    with app.app_context():
        try:
            print("Starting database seeding")

            seed_users = [
                students(
                    id="1"
                    first_name="John",
                    middle_name="P."
                    last_name="Doe",
                    email = db.Column(db.String(100), unique=True, nullable=False)
                    password = db.Column(db.String(255), nullable=False)  # Should be hashed
                    birthday = db.Column(db.Date, nullable=False)
                    gender = db.Column(db.String(10))
                    phone_number = db.Column(db.String(20))
                    address = db.Column(db.String(255))
                    student_id = db.Column(db.String(50), unique=True)
                ),
            ]

            for user in seed_users:
                existing_user = User.query.filter_by(email=user.email).first()
                if existing_user:
                    print(f"Skipping existing user: {user.email}")
                    continue
                db.session.add(user)

            db.session.commit()
            print("Database seeded successfully")
        
        except IntegrityError as e:
            db.session.rollback
            print(f"Integrity error: {e}")

        except SQLAlchemyError as e:
            db.session.rollback
            print(f"SQLALCHEMY error: {e}")
        
        except Exception as e:
            db.session.rollback
            print(f"Unexpected error: {e}")

        finally:
            db.session.close()

if __name__ == "__main__":
    seed_data()