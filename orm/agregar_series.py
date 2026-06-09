from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import cadena_base_datos
import pandas as pd
from modelo import Pais, Plataforma, Serie

engine=create_engine(cadena_base_datos)
Session=sessionmaker(bind=engine)
session=Session()

datos_series = pd.read_csv("../data/series.csv")

for _, fila in datos_series.iterrows():

    pais = session.query(Pais).filter_by(
        nombre=fila["pais"]
    ).first()

    plataforma = session.query(Plataforma).filter_by(
        nombre=fila["plataforma"]
    ).first()

    serie = Serie(
        titulo=fila["titulo"],
        genero=fila["genero"],
        anio_estreno=fila["anio_estreno"],
        temporadas=fila["temporadas"],
        pais=pais,
        plataforma=plataforma
    )

    session.add(serie)

session.commit()