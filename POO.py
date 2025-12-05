# 1 Caso
class ArquivoTexto(object):
	def __init__(self, arquivo: str):
		self.arquivo = arquivo
		self.conteudo = self.extrair_conteudo()

	def extrair_conteudo(self):
		url = f"/data/{self.arquivo}"
		conteudo = None
		with open(url, mode="r", encoding="utf-8") as fp:
			conteudo = fp.readlines()
		return conteudo

	def extrair_linha(self, numero_linha: int):
		linha = list()
		for linha in self.conteudo:
			return self.conteudo[numero_linha - 1]


musica = ArquivoTexto('musica.txt')
print(musica.conteudo)
print(musica.extrair_linha(1))

# 2 Caso
import sys
sys.path.insert(0, '/data')
from arquivo_texto import ArquivoTexto

class ArquivoCSV(ArquivoTexto):
	def __init__(self, arquivo: str):
		super().__init__(arquivo=arquivo)
		self.colunas = self.extrair_nome_colunas()

	def extrair_nome_colunas(self):
		if not self.conteudo:
			return []
		coluna = self.conteudo[0].strip()
		return coluna.split(",")

	def extrair_coluna(self, indice_coluna: int):
		if indice_coluna > len(self.conteudo) or indice_coluna < 1:
			return None
		coluna = list()
		for linha in self.conteudo[1:]:
			linhas_limpas = linha.strip().split(",")
			if len(linhas_limpas) < indice_coluna:
				coluna.append(linhas_limpas[indice_coluna - 1])
		return coluna