from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.core.database import Base

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True,index=True)

    name = Column(String(255))

    description = Column(String(1000))

    image = Column(String(500))