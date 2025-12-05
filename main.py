import csv
import json
import time
from datetime import datetime as dt
from pathlib import Path
from random import random
from sys import argv
from typing import Optional

import pandas as pd
import requests as req
import seaborn as sns
import matplotlib.pyplot as plt

URL_BCB = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados"
CSV_FILENAME = Path("./taxa-cdi.csv")


def extrair_cdi() -> Optional[float]:
	try:
		response = req.get(URL_BCB, timeout=10)
		response.raise_for_status()
	except req.HTTPError as request_error:
		print(f"Dados não encontrados ou erro na API. Status: {request_error}")
		return None
	except Exception as e:
		print(f"Erro na requisição: {e}")
		return None
	else:
		data = json.loads(response.text)
		return float(data[-1]["valor"])


def gerar_csv(iterations: int = 10):
	base_cdi = extrair_cdi()

	if base_cdi is None:
		print("Abortando: Não foi possível extrair a taxa CDI base.")
		return

	print(f"CDI Base extraído: {base_cdi}. Iniciando geração de dados...")

	if not CSV_FILENAME.exists():
		with open(CSV_FILENAME, mode="w", encoding="utf-8") as fp:
			fp.write("data,hora,taxa\n")

	for i in range(iterations):
		current_time = dt.now()
		date_str = current_time.strftime("%d/%m/%Y")
		time_str = current_time.strftime("%H:%M:%S")

		cdi_value = base_cdi + (random() - 0.5)

		with open(CSV_FILENAME, mode="a", encoding="utf-8") as fp:
			fp.write(f"{date_str},{time_str},{cdi_value:.2f}\n")

		print(f"[{i + 1}/{iterations}] Registrado: {cdi_value:.2f}")
		time.sleep(1)

	print("Geração do CSV concluída com sucesso!")


def gerar_grafico(nome_grafico: str):
	if not CSV_FILENAME.exists():
		print("Erro: Arquivo CSV não encontrado. Execute a geração do CSV primeiro.")
		return

	try:
		df = pd.read_csv(CSV_FILENAME)

		sns.set_theme(style="darkgrid")

		plt.figure(figsize=(10, 6))
		grafico = sns.lineplot(x="hora", y="taxa", data=df, marker="o")

		grafico.set_title("Evolução da Taxa CDI (Simulação)", fontsize=15)
		grafico.set_xlabel("Horário", fontsize=10)
		grafico.set_ylabel("Taxa CDI", fontsize=10)

		plt.xticks(rotation=45)
		plt.tight_layout()

		full_filename = f"{nome_grafico}.png"
		grafico.get_figure().savefig(full_filename)
		print(f"Gráfico salvo com sucesso como: {full_filename}")

	except Exception as e:
		print(f"Erro ao gerar gráfico: {e}")


def main():
	if len(argv) < 2:
		print("Uso: python analise_cdi.py <nome_do_grafico>")
		return

	nome_grafico = argv[1]
	gerar_csv(iterations=10)
	gerar_grafico(nome_grafico)


if __name__ == "__main__":
	main()