# titulo de serie y promedio de edad de sus actores

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from config import cadena_base_datos
from modelo import Serie, Actor
engine=create_engine(cadena_base_datos)
Session=sessionmaker(bind=engine)
session=Session()
resultados = (
    session.query(
        Serie.titulo,
        func.avg(Actor.edad))
    .join(Actor).group_by(Serie.id, Serie.titulo)
    .order_by(Serie.titulo).all())

for serie, promedio in resultados:
    print(
        f"Serie: {serie}, "
        f"Promedio de edad: {promedio:.2f}")