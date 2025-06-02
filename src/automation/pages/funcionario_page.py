import time
from pathlib import Path
import pyautogui
import src.config.config as config

class FuncionarioPage:
    def selectFormularioMenu(self):
        try:
            # Construa o caminho da imagem de forma mais robusta
            image_path = Path(config.assetPath) / 'menus' / 'Processos' / 'Formularios Menu Item.png'
            
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
    
    def searchFuncionariosForm(self):
        pyautogui.write('Funcionários', interval=0.1)

    def enterInFuncionariosForm(self):
        ...
    
    
    @staticmethod
    def searchButton(self):
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
    
    def seachByCpf(self, cpf:str):
        try:
            # Construa o caminho da imagem de forma mais robusta
            image_path = Path(config.assetPath) / 'menus' / 'Processos' / 'Funcionarios' / 'search' / 'cpf empty column.png'
            
            # Adicione parâmetros para melhorar a detecção
            location = pyautogui.locateOnScreen(
                str(image_path),
                confidence=0.9,  # Aceita 80% de similaridade
                minSearchTime=2  # Tempo mínimo de busca
            )
            
            if location:
                pyautogui.moveTo(
                    location.left + location.width // 2, 
                    (location.top + location.height // 2) + (location.height // 4)
                )
                cpf_formatado = str(cpf).zfill(11)
                cpf_formatado = f"{cpf_formatado[:3]}.{cpf_formatado[3:6]}.{cpf_formatado[6:9]}-{cpf_formatado[9:]}"
                print(cpf_formatado)
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(0.1)
                pyautogui.write(str(cpf_formatado), interval=0.1)
                time.sleep(0.1)
                pyautogui.press('enter')
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

    def searchByCpfUserFounded(self):
        try:
            image_path = Path(config.assetPath) / 'menus' / 'Processos' / 'Funcionarios' / 'search' / 'No_user_with_this_cpf.png'
            
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

    def clickOnCloseSearchButton(self):
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
            # Tira um screenshot para debug
            debug_path = Path(config.assetPath) / 'debug_screenshot.png'
            pyautogui.screenshot(str(debug_path))
            print(f"Screenshot salvo em {debug_path} para análise")
            return False
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")

    def addRegister(self):
        try:
            # Construa o caminho da imagem de forma mais robusta
            image_path = Path(config.assetPath) / 'menus' / 'Form Options' / 'Add.png'
            
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

    def verificarFuncionarioCadastradoPessoaFisica(self, name: str):
        try:
            image_path = Path(config.assetPath) / 'menus' / 'Processos' / 'Funcionarios' / 'Campo Entidade Vazio.png'
            field_pos = pyautogui.locateOnScreen(str(image_path), confidence=0.8)
            print(f"Usuário {name} não cadastrado em Pessoa Fisica!")
            return False
        except pyautogui.ImageNotFoundException:
            return True

    @staticmethod
    def fillCpfField(cpf: str):
        pyautogui.write(str(cpf).zfill(11), interval=0.1)
        pyautogui.press('tab')

    @staticmethod
    def fillNameField(nome: str):
        pyautogui.press('tab')
        return
        pyautogui.write(nome, interval=0.1)
        pyautogui.press('tab')

    @staticmethod
    def fillPreferencialNameField(name: str):
        pyautogui.press('tab')
        pyautogui.press('tab')
        return

        nameSplitted = name.split(" ")
        pyautogui.write(" ".join(nameSplitted[:2]), interval=0.1)

        #Ir para RG
        pyautogui.press('tab')
        pyautogui.press('tab')

    def verificarNomePreferencialUsuado(self, name: str):
        #TODO
        ...

    def fillRGField(rg: str):
        pyautogui.write(str(rg).zfill(11), interval=0.1)

        #Ir para empresa
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')

    def fillEmpresaField(self, empresa: int):
        pyautogui.write(str(empresa), interval=0.1)
        pyautogui.press('tab')

    def confirmRegister(self):
        try:
            image_path = Path(config.assetPath) / 'menus' / 'Form Options' / 'Confirm.png'
            
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

    def confirmRegisterConfirmation(self):
        ...

    def cancelRegister(self):
        try:
            image_path = Path(config.assetPath) / 'menus' / 'Form Options' / 'Cancel.png'
            
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
    
    def cancelRegisterConfirmation(self):
        time.sleep(1)
        pyautogui.press('enter')