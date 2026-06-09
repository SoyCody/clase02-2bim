from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import cadena_base_datos
from modelo import Pais, Plataforma
import pandas as pd
engine = create_engine(cadena_base_datos)
Session=sessionmaker(bind=engine)
session=Session()
datos_plataformas = pd.read_csv("../data/plataformas.csv")

for _, fila in datos_plataformas.iterrows():

    pais = session.query(Pais).filter_by(
        nombre=fila["pais"]
    ).first()

    plataforma = Plataforma(
        nombre=fila["nombre"],
        suscriptores_millones=fila["suscriptores_millones"],
        pais=pais
    )

    session.add(plataforma)

session.commit()