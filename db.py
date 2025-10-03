from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# ⚠️ Ajusta usuario y contraseña
DATABASE_URL = "postgresql://postgres:QeaqueEa791*@localhost:5432/joyeria_competencia"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)   # 👈 ESTA ES LA CLAVE
Base = declarative_base()

class Tienda(Base):
    __tablename__ = "tiendas"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    ubicacion = Column(String)

    productos = relationship("Producto", back_populates="tienda")

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

    productos = relationship("Producto", back_populates="categoria")

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    material = Column(String)
    peso = Column(DECIMAL)
    quilates = Column(DECIMAL)
    precio = Column(DECIMAL)
    fecha_scraping = Column(Date)

    tienda_id = Column(Integer, ForeignKey("tiendas.id"))
    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    tienda = relationship("Tienda", back_populates="productos")
    categoria = relationship("Categoria", back_populates="productos")

Base.metadata.create_all(bind=engine)