from src.conectar_navegador import abrir_navegador
from src.config import senha_ecg, usuario_ecg
from src.ler_planilha import converter_planilha_para_json, converter_json_lista
from src.scrapper_ecg import cadastrar_kit, login_ecg

if __name__ == "__main__":
    navegador = abrir_navegador()
    login_ecg(navegador, usuario_ecg, senha_ecg)
    lista_de_kits = converter_json_lista()

    for i, kit in enumerate(lista_de_kits):
        if i == 206 or i > 330:
            try: 
                cadastrar_kit(navegador, kit)
                print(f'[ {i} ] - Kit {i} cadastrado com sucesso.')
            except Exception as e:
                print('\033[31m' + f"Erro ao cadastrar kit {i}." + '\033[0m')
                print(f'Erro: {e}')
                input('Aperte enter pra continuar')



