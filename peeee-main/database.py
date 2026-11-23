from typing import List, Optional
from decimal import Decimal
from sqlalchemy import BigInteger, Integer, String, ForeignKey, Numeric, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

DATABASE_URL = "sqlite:///./shop.db"

engine = create_engine(DATABASE_URL, echo=True)
session = sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    phone: Mapped[Optional[int]] = mapped_column(BigInteger)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    login: Mapped[str] = mapped_column(String(100), unique=True)

    addresses: Mapped[List["UserAddress"]] = relationship(back_populates="account")


class UserAddress(Base):
    __tablename__ = "user_addresses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    city: Mapped[str] = mapped_column(String(100))
    street: Mapped[str] = mapped_column(String(150))
    house: Mapped[str] = mapped_column(String(20))
    apartment: Mapped[Optional[str]] = mapped_column(String(20))
    entrance: Mapped[Optional[int]] = mapped_column(Integer)
    floor: Mapped[Optional[int]] = mapped_column(Integer)

    account: Mapped["Account"] = relationship(back_populates="addresses")


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)

    products: Mapped[List["Product"]] = relationship(back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("categories.id", ondelete="SET NULL"), nullable=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    description: Mapped[Optional[str]] = mapped_column(String(1000))
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    photo: Mapped[str] = mapped_column(String(255))

    category: Mapped["Category"] = relationship(back_populates="products")
    orders: Mapped[List["Order"]] = relationship(back_populates="product")


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id", ondelete="RESTRICT"))
    status: Mapped[str] = mapped_column(String(50), default="in_cart")
    quantity: Mapped[int] = mapped_column(Integer, default=1)
    total_price: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    product: Mapped["Product"] = relationship(back_populates="orders")


def get_db():
    with session() as session:
        yield session


Base.metadata.create_all(engine)
