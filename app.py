from flask import Flask, render_template, request

app = Flask(__name__)

# Função do simulador
def simulador_investimentos(valor_inicial, anos, selic=0.15, ipca=0.04):
    resultados = {}
    
    # Tesouro Selic
    resultados["Tesouro Selic"] = valor_inicial * (1 + selic) ** anos
    
    # Tesouro Prefixado (assumindo 12% a.a.)
    taxa_prefixado = 0.12
    resultados["Tesouro Prefixado"] = valor_inicial * (1 + taxa_prefixado) ** anos
    
    # Tesouro IPCA+ (IPCA + juro real 6%)
    juro_real = 0.06
    resultados["Tesouro IPCA+"] = valor_inicial * (1 + ipca + juro_real) ** anos
    
    # Poupança (0,5% ao mês)
    resultados["Poupança"] = valor_inicial * (1 + 0.005) ** (anos * 12)
    
    # CDB 100% CDI (≈ Selic)
    resultados["CDB 100% CDI"] = valor_inicial * (1 + selic) ** anos
    
    # Conta Bancária (80% da Selic)
    resultados["Conta Bancária (80% Selic)"] = valor_inicial * (1 + selic * 0.8) ** anos
    
    return resultados

# Rota principal
@app.route("/", methods=["GET", "POST"])
def index():
    resultados = None
    melhor = None
    if request.method == "POST":
        valor = float(request.form["valor"])
        anos = int(request.form["anos"])
        selic = float(request.form["selic"]) / 100
        ipca = float(request.form["ipca"]) / 100

        resultados = simulador_investimentos(valor, anos, selic, ipca)
        
        # Descobrir melhor investimento
        melhor = max(resultados, key=resultados.get)

    return render_template("index.html", resultados=resultados, melhor=melhor)

if __name__ == "__main__":
    app.run(debug=True)
