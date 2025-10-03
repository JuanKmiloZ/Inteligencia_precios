from model import entrenar_modelo

if __name__ == "__main__":
    model, mse, r2, resultados = entrenar_modelo()
    print("📊 Resultados del modelo:")
    print("MSE:", mse)
    print("R2:", r2)

    print("\n🔮 Predicciones de prueba:")
    print(resultados.head())