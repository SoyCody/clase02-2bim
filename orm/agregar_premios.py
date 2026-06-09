import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import cadena_base_datos
from modelo import Pais, Plataforma, Serie, Actor, Premio
engine=create_engine(cadena_base_datos)
Session=sessionmaker(bind=engine)
session=Session()
datos_premios = pd.read_csv("../data/premios.csv")

for _, fila in datos_premios.iterrows():

    serie = session.query(Serie).filter_by(
        titulo=fila["serie"]
    ).first()

    premio = Premio(
        nombre_premio=fila["nombre_premio"],
        categoria=fila["categoria"],
        anio=fila["anio"],
        serie=serie
    )

    session.add(premio)

session.commit()