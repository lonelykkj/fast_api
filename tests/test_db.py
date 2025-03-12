from sqlalchemy import create_engine

from fast_api.models import User, table_registry, select

from sqlalchemy.orm import Session


def test_create_user(session):
    user = User(
        username="heitor", 
         email="heitor@mail.com", 
        password="senha"
    )

    session.add(user)
    session.commit()
        
    result = session.scalar(
            select(User).where(User.email == 'heitor@mail.com')
    )

    assert result.username == 'heitor'
