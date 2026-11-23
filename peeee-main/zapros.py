from database import session, Product

with session() as db:
    stmt = Product(name = "андрей", category_id = "человек", description = "65кг", price = "12", photo = "/static/assets/nigers.webp")
    db.add(stmt)
    db.commit()

with session() as db:
    stmt = Product(name = "Бананы", category_id = "фрукт", description = "1кг", price = "99", photo = "/static/assets/ban.webp")
    db.add(stmt)
    db.commit()

with session() as db:
    stmt = Product(name = "Лук", category_id = "овощ", description = "1кг", price = "30", photo = "/static/assets/lyk.webp")
    db.add(stmt)
    db.commit()

with session() as db:
    stmt = Product(name = "Капуста брюссельская", category_id = "овощ", description = "1 шт", price = "200", photo = "/static/assets/kat.webp")
    db.add(stmt)
    db.commit()

