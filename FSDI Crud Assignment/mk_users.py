from app.routes import db, User


def create_my_user (first_name, last_name, hobbies):
    db.session.add(
        User (

            first_name=first_name,
            lsdt_name=last_name,
            hobbies=hobbies
        )
    )

    db.session.commit()



if __name__ == "__main__":
    create_my_user("Joshua", "GPL", "DIY stuff")
    users = User.query.all()
    print(users)
    create_my_user("Joshua","palmier","playing Soccer")
    user = User.query.filter_by(first_name="Joshua").first()
    print(user)