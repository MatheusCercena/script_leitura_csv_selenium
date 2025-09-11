import pandas as pd
import json
from pathlib import Path

def converter_planilha_para_json(nome_planilha):
    '''
    Args:
        nome_planilha: nome completo do arquivo com os dados(com extensao)
    '''
    caminho_excel = Path(f"data\\{nome_planilha}")

    xls = pd.ExcelFile(caminho_excel)
    dados = {}

    for planilha in xls.sheet_names:
        df = pd.read_excel(caminho_excel, sheet_name=planilha)
        
        df = df.iloc[:, :3]
        df.columns = ["codigo", "produto", "valor_bruto"]
        df["valor_bruto"] = df["valor_bruto"].astype(str).str.replace(".", ",")
        dados[planilha] = df.to_dict(orient="records")

    caminho_json = Path(f"data\\planilha_convertida.json")
    with open(caminho_json, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

    print(f"JSON salvo em: {caminho_json}")

def converter_json_lista():
    dados = json.load(open('data\\planilha_convertida.json', 'r', encoding='utf-8'))
    return [kit for planilha in dados.values() for kit in planilha]

 



