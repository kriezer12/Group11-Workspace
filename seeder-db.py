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
                User(
                    id=2,
                    first_name="Jane",
                    middle_name="R.",
                    last_name="Santos",
                    email="janesantos@example.com",
                    password=generate_password_hash("janesantos123"),
                    birthday="2001-11-22",
                    gender="Female",
                    phone_number="+63-917-555-1122",
                    address="Unit 8B, Sunrise Residences, Quezon City, Philippines",
                    student_id="PUPIT-2025-00456"
                ),
                User(
                    id=3,
                    first_name="Michael",
                    middle_name="T.",
                    last_name="Reyes",
                    email="michaelreyes@example.com",
                    password=generate_password_hash("michaelreyes123"),
                    birthday="2000-08-09",
                    gender="Male",
                    phone_number="+63-915-888-2211",
                    address="123 Mabini St., San Pedro, Laguna, Philippines",
                    student_id="PUPIT-2025-00789"
                ),
            ]

            added_count = 0
            for student in seed_users:
                existing_user = User.query.filter_by(email=student.email).first()
                if existing_user:
                    print(f"Skipping existing user: {student.email}")
                    continue
                db.session.add(student)
                added_count += 1
                print(f"Added new user: {student.email}")

            db.session.commit()
            print(f"Database seeded successfully. Added {added_count} new user(s).")
            
            # Show total users in database
            total_users = User.query.count()
            print(f"Total users in database: {total_users}")
        
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