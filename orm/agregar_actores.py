from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import cadena_base_datos
import pandas as pd
from modelo import Pais, Serie, Actor

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session=Session()
datos_actores = pd.read_csv("../data/actores.csv")

for _, fila in datos_actores.iterrows():

    pais = session.query(Pais).filter_by(
        nombre=fila["pais"]
    ).first()

    serie = session.query(Serie).filter_by(
        titulo=fila["serie"]
    ).first()

    actor = Actor(
        nombre=fila["nombre"],
        edad=fila["edad"],
        pais=pais,
        serie=serie
    )

    session.add(actor)

session.commit()