import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from data import cargar_datos

def entrenar_modelo():
    df = cargar_datos()

    # --- Variables predictoras y objetivo ---
    X = df[["peso", "quilates"]]
    y = df["precio"]

    # --- División de datos ---
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # --- Modelo ---
    model = LinearRegression()
    model.fit(X_train, y_train)

    # --- Evaluación ---
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # --- Resultados en DataFrame ---
    resultados = pd.DataFrame({
        "Real": y_test.values,
        "Predicho": y_pred
    })

    return model, mse, r2, resultados