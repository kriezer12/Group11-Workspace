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
                User(
                    id=1,
                    first_name="John",
                    middle_name="P.",
                    last_name="Doe",
                    email="johndoe@example.com",
                    password=generate_password_hash("johndoe123"),
                    birthday="2002-05-14",
                    gender="Male",
                    phone_number="+63-912-345-6789",
                    address="Blk 12 Lot 5, Carmona Estates, Cavite, Philippines",
                    student_id="PUPIT-2025-00123"
                ),
            ]

            for student in seed_users:
                existing_user = User.query.filter_by(email=student.email).first()
                if existing_user:
                    print(f"Skipping existing user: {student.email}")
                    continue
                db.session.add(student)

            db.session.commit()
            print("Database seeded successfully")
        
        except IntegrityError as e:
            db.session.rollback()
            print(f"Integrity error: {e}")

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"SQLALCHEMY error: {e}")
        
        except Exception as e:
            db.session.rollback()
            print(f"Unexpected error: {e}")

        finally:
            db.session.close()

if __name__ == "__main__":
    seed_data()