# titulo de serie y promedio de edad de sus actores

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from config import cadena_base_datos
from modelo import Serie, Actor
engine=create_engine(cadena_base_datos)
Session=sessionmaker(bind=engine)
session=Session()
serie= session.query(Serie).order_by(Serie.titulo).all()

for s in serie:
    promedio = s.obtener_edad_actores()
    premios= s.obtener_numero_premios()
    print(
        f"Serie: {s.titulo}, "
        f"Promedio de edad: {promedio:.2f}, "
        f"Número de premios: {premios}")