from sqlalchemy.orm import sessionmaker
import pandas as pd
from modelo import engine, Pais
Session = sessionmaker(bind=engine)
session = Session()
datos_paises = pd.read_csv(
    "../data/paises.csv",
    encoding="utf-8"
)

for _, fila in datos_paises.iterrows():
    pais_existente = session.query(Pais).filter_by(
        nombre=fila["nombre"]
    ).first()

    if pais_existente is None:

        pais = Pais(
            nombre=fila["nombre"],
            continente=fila["continente"]
        )

        session.add(pais)
session.commit()

print("Países cargados correctamente")