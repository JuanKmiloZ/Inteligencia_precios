import pandas as pd
from db import SessionLocal, Producto

def cargar_datos():
    session = SessionLocal()
    productos = session.query(Producto).all()
    print("Productos encontrados:", len(productos))  # 👈 debug

    data = []
    for p in productos:
        data.append({
            "id": p.id,
            "nombre": p.nombre,
            "categoria": p.categoria.nombre if p.categoria else None,
            "material": p.material,
            "peso": float(p.peso) if p.peso else None,
            "quilates": float(p.quilates) if p.quilates else None,
            "precio": float(p.precio) if p.precio else None,
            "tienda": p.tienda.nombre if p.tienda else None,
            "ubicacion_tienda": p.tienda.ubicacion if p.tienda else None,
            "fecha_scraping": p.fecha_scraping
        })
    session.close()

    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = cargar_datos()
    print(df.head())