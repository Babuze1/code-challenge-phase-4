from random import randint
from app import app, db
from model.hero import Hero
from model.heroPower import HeroPower
from model.power import Power
from sqlalchemy.exc import IntegrityError

def seed():
    with app.app_context():
        db.create_all() 

        print("🦸‍♀️ Seeding powers...")
        powers_data = [
            {"name": "super strength", "description": "gives the wielder super-human strengths"},
            {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
            {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
            {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
        ]

        powers = [Power(**data) for data in powers_data]
        db.session.add_all(powers)
        db.session.commit()

        print("🦸‍♀️ Seeding heroes...")
        heroes_data = [
            {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
            {"name": "Doreen Green", "super_name": "Squirrel Girl"},
            {"name": "Stacy Queen", "super_name": "Spider-Gwen"},
            {"name": "Babuze Prior", "super_name": "Dr. Papuse"},
            {"name": "Nigga Groo", "super_name": "De Nigga"},
            {"name": "Kai Cenat", "super_name": "Woolant Kai"},
            {"name": "I Show Speed", "super_name": "Speedy"},
            {"name": "J J", "super_name": "KSI"},
            {"name": "Side Men", "super_name": "Hit EM All"},
            {"name": "Peter Parker", "super_name": "Spiderman"},
            {"name": "Robert Olwon", "super_name": "Jalango"},
            {"name": "Type Shit", "super_name": "Auto Correct"},
            {"name": "Suck Onn", "super_name": "Dicks On"},
        ]

        heroes = [Hero(**data) for data in heroes_data]
        db.session.add_all(heroes)
        db.session.commit()

        print("🦸‍♀️ Adding powers to heroes...")
        strengths = ["Strong", "Weak", "Average"]

        for hero in heroes:
            for _ in range(1, 4):
                power = Power.query.order_by(db.func.random()).first()
                hero_power = HeroPower(hero=hero, power=power, strength=strengths[randint(0, 2)])
                try:
                    db.session.add(hero_power)
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()

        print("🦸‍♀️ Done seeding!")

if __name__ == "__main__":
    seed()
    print("Database seeded successfully.")

