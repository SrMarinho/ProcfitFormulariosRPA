import time
from pathlib import Path
import pyautogui
import src.config.config as config

class UsuarioPage:
    def clickOnSearchButton(self):
        time.sleep(0.5)
        try:
            # Construa o caminho da imagem de forma mais robusta
            image_path = Path(config.assetPath) / 'menus' / 'Form Options' / 'Search.png'
            
            # Adicione parâmetros para melhorar a detecção
            location = pyautogui.locateOnScreen(
                str(image_path),
                confidence=0.8,  # Aceita 80% de similaridade
                minSearchTime=2  # Tempo mínimo de busca
            )
            
            if location:
                pyautogui.click(location)
                return True
            else:
                print("Imagem encontrada, mas não pôde ser clicada")
                return False
                
        except pyautogui.ImageNotFoundException:
            print(f"Erro: Imagem não encontrada - {image_path}")
            # Tira um screenshot para debug
            debug_path = Path(config.assetPath) / 'debug_screenshot.png'
            pyautogui.screenshot(str(debug_path))
            print(f"Screenshot salvo em {debug_path} para análise")
            return False
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            return False
    
    def seachByName(self, name:str):
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.write(name)
        time.sleep(0.2)
        pyautogui.press('enter')
        
    def searchByNameUserRegistered(self):
        time.sleep(2)
        try:
            image_path = Path(config.assetPath) / 'menus' / 'Ferramentas' / 'configuracoes_usuario' / 'search' / 'search_by_name_empty.png'

            location = pyautogui.locateOnScreen(
                str(image_path),
                confidence=0.98,  # Aceita 90% de similaridade
                minSearchTime=2  # Tempo mínimo de busca
            )
            
            if location:
                return False
            else:
                return True
                
        except pyautogui.ImageNotFoundException:
            return True
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            return True

    def moveFromNameToLogin(self):
        time.sleep(0.5)
        pyautogui.press('right')

    def writePossibleLogin(self, login: str):
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.press('backspace')
        time.sleep(0.1)
        pyautogui.write(login)
        time.sleep(0.1)
        pyautogui.press('enter')

    def loginAlreadyUsed(self):
        time.sleep(2)
        try:
            image_path = Path(config.assetPath) / 'menus' / 'Ferramentas' / 'configuracoes_usuario' / 'search' / 'search_by_login_no_register_founded.png'

            location = pyautogui.locateOnScreen(
                str(image_path),
                confidence=0.95,
                minSearchTime=2,
                grayscale=True
            )
            
            if location:
                return False
            else:
                print("Login já usado")
                return True
                
        except pyautogui.ImageNotFoundException:
            print("Login já usado")
            return True
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            return True

    def clickOnCloseSearchButton(self):
        time.sleep(0.5)
        try:
            image_path = Path(config.assetPath) / 'menus' / 'Processos' / 'Funcionarios' / 'search' / 'closeSearch.png'
            
            location = pyautogui.locateOnScreen(
                str(image_path),
                confidence=0.9,  # Aceita 90% de similaridade
                minSearchTime=2  # Tempo mínimo de busca
            )
            
            time.sleep(0.1)
            if location:
                pyautogui.click(location)
                return True
            else:
                print("Imagem encontrada, mas não pôde ser clicada")
                return False
                
        except pyautogui.ImageNotFoundException:
            print(f"Erro: Imagem não encontrada - {image_path}")
            return False
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")


    def addRegister(self):
        time.sleep(1)
        try:
            image_path = Path(config.assetPath) / 'menus' / 'Form Options' / 'Add.png'
            
            location = pyautogui.locateOnScreen(
                str(image_path),
                confidence=0.8,  # Aceita 80% de similaridade
                minSearchTime=2  # Tempo mínimo de busca
            )
            
            if location:
                pyautogui.click(location)
                return True
            else:
                print("Imagem encontrada, mas não pôde ser clicada")
                return False
                
        except pyautogui.ImageNotFoundException:
            print(f"Erro: Imagem não encontrada - {image_path}")
            return False
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            return False

    def fill_nome(self, name: str):
        time.sleep(1)
        try:
            image_path = Path(config.assetPath) / 'menus' / 'Ferramentas' / 'configuracoes_usuario' / 'campo_nome.png'
            
            location = pyautogui.locateOnScreen(
                str(image_path),
                confidence=0.8,
                minSearchTime=2,
                grayscale=True
            )
            
            if location:
                x = int(location.left + location.width * 0.75) # clicar em 75% do tamanho da imagem 
                y = location.top + location.height // 2 # clicar no centro do eixo Y
                pyautogui.click(x, y)
                time.sleep(0.3)
                pyautogui.write(name)
                return True
            else:
                print("Imagem encontrada, mas não pôde ser clicada")
                return False
                
        except pyautogui.ImageNotFoundException:
            print(f"Erro: Imagem não encontrada - {image_path}")
            return False
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            return False

    def fill_login(self, login: str):
        time.sleep(1)
        try:
            image_path = Path(config.assetPath) / 'menus' / 'Ferramentas' / 'configuracoes_usuario' / 'login_textfield_empty.png'
            
            location = pyautogui.locateOnScreen(
                str(image_path),
                confidence=0.8,
                minSearchTime=2,
                grayscale=True
            )
            
            if location:
                x = int(location.left + location.width * 0.75) # clicar em 75% do tamanho da imagem 
                y = location.top + location.height // 2 # clicar no centro do eixo Y
                pyautogui.click(x, y)
                time.sleep(0.3)
                pyautogui.write(login)
                return True
            else:
                print("Imagem encontrada, mas não pôde ser clicada")
                return False
                
        except pyautogui.ImageNotFoundException:
            print(f"Erro: Imagem não encontrada - {image_path}")
            return False
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            return False

    def openSearchEntidade(self):
        time.sleep(1)
        try:
            image_path = Path(config.assetPath) / 'menus' / 'Ferramentas' / 'configuracoes_usuario' / 'entidade_empty.png'
            
            location = pyautogui.locateOnScreen(
                str(image_path),
                confidence=0.8,
                minSearchTime=2,
                grayscale=True
            )
            
            if location:
                pyautogui.click(location)
                time.sleep(0.3)
                pyautogui.press("tab")
                pyautogui.press("enter")
                return True
            else:
                print("Imagem encontrada, mas não pôde ser clicada")
                return False
                
        except pyautogui.ImageNotFoundException:
            print(f"Erro: Imagem não encontrada - {image_path}")
            return False
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            return False

    def searchEntidadeFillNomeEntidade(self, name: str):
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(0.2)
        pyautogui.write(name)

    def entidadeFounded(self, name: str):
        time.sleep(1)
        try:
            image_path = Path(config.assetPath) / 'menus' / 'Ferramentas' / 'configuracoes_usuario' / 'entidade_search' / 'search_by_nome_without_row.png'
            
            location = pyautogui.locateOnScreen(
                str(image_path),
                confidence=0.8,
                minSearchTime=2,
                grayscale=True
            )
            
            if location:
                return False
            else:
                return True
                
        except pyautogui.ImageNotFoundException:
            print(f"Erro: Imagem não encontrada - {image_path}")
            return True
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            return True


    def selectEntidade(self, name: str):
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(0.2)
        pyautogui.press('enter')

    def fill_perfil_usuario_copia(self, perfil: int):
        time.sleep(1)
        try:
            image_path = Path(config.assetPath) / 'menus' / 'Ferramentas' / 'configuracoes_usuario' / 'perfil_usuario_copia_empty.png'
            
            location = pyautogui.locateOnScreen(
                str(image_path),
                confidence=0.8,
                minSearchTime=2,
                grayscale=True
            )
            
            if location:
                pyautogui.click(location)
                time.sleep(0.2)
                pyautogui.write(str(perfil))
                return True
            else:
                return False
                
        except pyautogui.ImageNotFoundException:
            print(f"Erro: Imagem não encontrada - {image_path}")
            return False
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            return False


    def activateDetailEmpresasLancemento(self):
        time.sleep(1)
        pyautogui.press("f7")

    def fill_empresa_lancamento(self, empresa: str):
        time.sleep(1)
        try:
            image_path = Path(config.assetPath) / 'menus' / 'Ferramentas' / 'configuracoes_usuario' / 'detail_empresas_lancamento_empty.png'
            
            location = pyautogui.locateOnScreen(
                str(image_path),
                confidence=0.8,
                minSearchTime=2
            )
            
            if location:
                x = location.left + location.width // 6
                y = location.top + location.height * 0.75
                pyautogui.click(x, y)
                time.sleep(0.2)
                pyautogui.write(str(empresa))
                time.sleep(0.2)
                pyautogui.press("tab")
                time.sleep(0.5)
                pyautogui.press("esc")
                return True
            else:
                print("Imagem encontrada, mas não pôde ser clicada")
                return False
                
        except pyautogui.ImageNotFoundException:
            print(f"Erro: Imagem não encontrada - {image_path}")
            return False
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            return False

    def importar_perfil(self):
        time.sleep(1)
        try:
            image_path = Path(config.assetPath) / 'menus' / 'Ferramentas' / 'configuracoes_usuario' / 'importar_perfil.png'
            
            location = pyautogui.locateOnScreen(
                str(image_path),
                confidence=0.8,
                minSearchTime=2
            )
            
            if location:
                pyautogui.click(location)
                return True
            else:
                print("Imagem encontrada, mas não pôde ser clicada")
                return False
                
        except pyautogui.ImageNotFoundException:
            print(f"Erro: Imagem não encontrada - {image_path}")
            return False
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            return False

    def resetar_senha(self):
        time.sleep(1)
        pyautogui.keyDown("ctrl")
        time.sleep(0.1)
        pyautogui.press("f2")
        pyautogui.keyUp("ctrl")
        time.sleep(0.3)
        pyautogui.write("S")
        time.sleep(0.3)
        pyautogui.press("enter")
    
    def save(self):
        time.sleep(1)
        try:
            image_path = Path(config.assetPath) / 'menus' / 'Form Options' / 'configuracoes_usuario' / 'Confirm.png'
            
            location = pyautogui.locateOnScreen(
                str(image_path),
                confidence=0.8,
                minSearchTime=2
            )
            
            if location:
                pyautogui.click(location)
                time.sleep(1)
                pyautogui.write("S")
                time.sleep(0.2)
                pyautogui.press("enter")
                return True
            else:
                print("Imagem encontrada, mas não pôde ser clicada")
                return False
                
        except pyautogui.ImageNotFoundException:
            print(f"Erro: Imagem não encontrada - {image_path}")
            return False
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            return False