import sys
import re

class OnePieceLanguageInterpreter:
    def __init__(self):
        self.bau_do_tesouro = [0] * 1000 
        self.lapis = 0                   
        self.instrucoes = []             
        self.mapa_saltos = {}            

    def _analisar_linha(self, linha):
        linha = linha.strip()
        
        # Ignora linhas vazias
        if not linha: return None

        # Tratamento de Comentários (Aceita Yohohoho e //)
        if "Yohohoho" in linha:
            linha = linha.split("Yohohoho")[0].strip()
        elif "//" in linha:
            linha = linha.split("//")[0].strip()
        
        if not linha: return None

        # --- ANÁLISE DE COMANDOS ---

        # 1. Estrutura e Controle
        if linha == "Tripulação reunida!": return ("START",)
        if linha == "Fim da Jornada.": return ("EXIT",)
        if "Enquanto houver esperança" in linha: return ("WHILE_START",)
        if "Fim do ciclo" in linha: return ("WHILE_END",)
        if "Fim da verificação" in linha: return ("IF_END",)

        # 2. String (CORREÇÃO DA FALHA: Lógica de split em vez de Regex estrito)
        # Se a linha contém o comando de diário, pegamos tudo depois do ":"
        if "Registrar Entrada no Diário:" in linha:
            try:
                # Divide a linha no primeiro ":", pega a parte do texto (índice 1)
                conteudo_bruto = linha.split(":", 1)[1].strip()
                # Remove aspas das pontas (qualquer tipo: reta, curva simples ou dupla)
                conteudo_limpo = conteudo_bruto.strip('"“”\'')
                # Converte o \n escrito em quebra de linha real
                conteudo_final = conteudo_limpo.replace(r"\n", "\n")
                return ("PRINT_STR", conteudo_final)
            except IndexError:
                return None

        # 3. Manipulação Direta
        match_set = re.match(r"Mudar recompensa para (\d+)", linha, re.IGNORECASE)
        if match_set: return ("SET", int(match_set.group(1)))

        if re.match(r"Aumentar Recompensa", linha, re.IGNORECASE): return ("INC",)
        if re.match(r"Pagar a Nami", linha, re.IGNORECASE): return ("DEC",)

        # 4. Movimentação e Matemática
        if re.match(r"Seguir Log Pose", linha, re.IGNORECASE): return ("MOVE_R",)
        if re.match(r"Voltar para resgatar", linha, re.IGNORECASE): return ("MOVE_L",)
        if "Gomu Gomu no" in linha: return ("MUL2",)
        if "Santoryuu" in linha: return ("DIV2",)
        if "Usar Rumble Ball" in linha: return ("ZERO",)

        # 5. Entrada e Saída Numérica
        if "Gritar nível de poder" in linha: return ("PRINT_NUM",)
        if "Ler Poneglyph" in linha: return ("PRINT_CHAR",)
        if "Den Den Mushi tocou" in linha: return ("INPUT",)

        # 6. Condicionais
        match_if = re.match(r"Se o Tesouro Atual for (Maior|Menor|Igual) (?:que|a) (\d+)", linha, re.IGNORECASE)
        if match_if:
            return ("IF_START", match_if.group(1).lower(), int(match_if.group(2)))

        return None

    def _mapear_fluxo(self):
        pilha = []
        for i, cmd in enumerate(self.instrucoes):
            if not cmd: continue
            op = cmd[0]

            if op in ["WHILE_START", "IF_START"]:
                pilha.append(i)
            elif op == "WHILE_END":
                inicio = pilha.pop()
                self.mapa_saltos[inicio] = i
                self.mapa_saltos[i] = inicio
            elif op == "IF_END":
                inicio = pilha.pop()
                self.mapa_saltos[inicio] = i 

    def executar(self, codigo_fonte):
        self.instrucoes = []
        linhas = codigo_fonte.split('\n')
        
        for linha in linhas:
            token = self._analisar_linha(linha)
            if token:
                self.instrucoes.append(token)
        
        try:
            self._mapear_fluxo()
        except IndexError:
            print("Erro de Sintaxe: Blocos abertos e não fechados corretamente.")
            return

        pc = 0
        executando = False

        while pc < len(self.instrucoes):
            cmd = self.instrucoes[pc]
            op = cmd[0]

            if op == "START":
                executando = True
                pc += 1; continue
            elif op == "EXIT":
                print("\n--- Fim da Jornada ---")
                break
            
            if not executando:
                pc += 1; continue

            # Execução
            if op == "SET": self.bau_do_tesouro[self.lapis] = cmd[1]
            elif op == "INC": self.bau_do_tesouro[self.lapis] += 1
            elif op == "DEC": self.bau_do_tesouro[self.lapis] -= 1
            elif op == "MUL2": self.bau_do_tesouro[self.lapis] *= 2
            elif op == "DIV2": self.bau_do_tesouro[self.lapis] //= 2
            elif op == "ZERO": self.bau_do_tesouro[self.lapis] = 0
            elif op == "MOVE_R": self.lapis = (self.lapis + 1) % 1000
            elif op == "MOVE_L": self.lapis = (self.lapis - 1) % 1000
            
            elif op == "PRINT_NUM": print(str(self.bau_do_tesouro[self.lapis]), end="")
            elif op == "PRINT_CHAR": print(chr(self.bau_do_tesouro[self.lapis]), end="")
            elif op == "PRINT_STR": print(cmd[1], end="")
            
            elif op == "INPUT":
                val = input("")
                self.bau_do_tesouro[self.lapis] = int(val) if val.isdigit() else ord(val[0])

            elif op == "WHILE_START":
                if self.bau_do_tesouro[self.lapis] == 0: pc = self.mapa_saltos[pc]
            elif op == "WHILE_END":
                if self.bau_do_tesouro[self.lapis] != 0: pc = self.mapa_saltos[pc]

            elif op == "IF_START":
                cond, ref = cmd[1], cmd[2]
                val = self.bau_do_tesouro[self.lapis]
                res = (cond == "maior" and val > ref) or \
                      (cond == "menor" and val < ref) or \
                      (cond == "igual" and val == ref)
                if not res: pc = self.mapa_saltos[pc]

            pc += 1

if __name__ == "__main__":
    import os
    
    # Verifica se o usuário passou o nome do arquivo no terminal
    if len(sys.argv) > 1:
        nome_arquivo = sys.argv[1]
        
        # Verifica se o arquivo realmente existe na pasta
        if os.path.exists(nome_arquivo):
            print(f">>> Lendo Diário de Bordo: {nome_arquivo} <<<\n")
            
            # Abre o arquivo externo e lê o conteúdo
            try:
                with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                    codigo_fonte = arquivo.read()
                
                # Executa o interpretador
                interprete = OnePieceLanguageInterpreter()
                interprete.executar(codigo_fonte)
                
            except Exception as e:
                print(f"Erro ao ler o arquivo: {e}")
        else:
            print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
            print("Verifique se o nome está correto e se ele está na mesma pasta.")
    
    else:
        # Se o usuário rodar sem argumentos, mostra a ajuda
        print("--- One Piece Language Interpreter (OPL) ---")
        print("Uso correto: python opl_interpreter.py <arquivo.opl>")