from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Set up base and engine
Base = declarative_base()
engine = create_engine("sqlite:///store.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# Define Category table
class Category(Base):
    __tablename__ = "categories"
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, nullable=False)
    products = relationship("Product", back_populates="category")

# Define Product table
class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"))
    category = relationship("Category", back_populates="products")

# Create tables
Base.metadata.create_all(engine)

# --- SAMPLE DATA SETUP ---

# Clear any existing data
session.query(Product).delete()
session.query(Category).delete()

# Add categories
categories = [
    Category(category_name="Electronics"),
    Category(category_name="Books"),
    Category(category_name="Groceries")
]
session.add_all(categories)
session.commit()

# Add products
products = [
    Product(product_name="Smartphone", price=299.99, category=categories[0]),
    Product(product_name="Laptop", price=999.99, category=categories[0]),
    Product(product_name="Fiction Novel", price=15.99, category=categories[1]),
    Product(product_name="Rice", price=2.99, category=categories[2])
]
session.add_all(products)
session.commit()

# --- DATA RETRIEVAL ---

print("📦 Product List:\n")
all_products = session.query(Product).all()
for product in all_products:
    print(f"🔹 {product.product_name} - ${product.price:.2f} ({product.category.category_name})")

# Close session
session.close()
