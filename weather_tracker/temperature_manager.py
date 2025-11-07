from collections import namedtuple
import os

# Criamos a estrutura de dados nomeada
TemperatureRecord = namedtuple("TemperatureRecord", ["dia", "max_temp", "min_temp"])

class TemperatureManager:
    def __init__(self, data_file='data/records.txt'):
        self.data_file = data_file
        self.records = []
        self._load_records()

    def _load_records(self):
        """Carrega os registros de temperatura do arquivo."""
        if not os.path.exists(self.data_file):
            return
        with open(self.data_file, 'r', encoding='utf-8') as f:
            for line in f:
                dia, max_t, min_t = line.strip().split(';')
                self.records.append(TemperatureRecord(dia, float(max_t), float(min_t)))

    def _save_records(self):
        """Salva os registros de temperatura no arquivo."""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            for r in self.records:
                f.write(f"{r.dia};{r.max_temp};{r.min_temp}\n")

    def adicionar_registro(self, dia, max_temp, min_temp):
        """Adiciona um novo registro de temperatura."""
        novo = TemperatureRecord(dia, max_temp, min_temp)
        self.records.append(novo)
        self._save_records()
        print(f"✅ Registro de {dia} adicionado com sucesso!")

    def listar_registros(self):
        """Lista todos os registros."""
        if not self.records:
            print("Nenhum registro encontrado.")
            return
        for r in self.records:
            print(f"{r.dia}: Máx {r.max_temp}°C / Mín {r.min_temp}°C")

    def calcular_media(self):
        """Calcula a média semanal das temperaturas."""
        if not self.records:
            print("Sem dados para calcular média.")
            return
        media_max = sum(r.max_temp for r in self.records) / len(self.records)
        media_min = sum(r.min_temp for r in self.records) / len(self.records)
        print(f"🌤️ Média semanal -> Máx: {media_max:.1f}°C / Mín: {media_min:.1f}°C")

    def extremos(self):
        """Mostra o dia mais quente e o mais frio."""
        if not self.records:
            print("Sem registros para analisar.")
            return
        mais_quente = max(self.records, key=lambda r: r.max_temp)
        mais_frio = min(self.records, key=lambda r: r.min_temp)
        print(f"🔥 Dia mais quente: {mais_quente.dia} ({mais_quente.max_temp}°C)")
        print(f"❄️ Dia mais frio: {mais_frio.dia} ({mais_frio.min_temp}°C)")
