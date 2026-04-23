# processo.py - Processos Leves

class ProcessoLeve:
    def __init__(self, nome, mmu, enderecos):
        self.nome = nome
        self.mmu = mmu
        self.enderecos = enderecos
    
    def executar(self):
        print(f"\n🚀 Iniciando {self.nome}")
        for endereco in self.enderecos:
            self.mmu.traduzir_endereco(endereco)
        print(f"✅ {self.nome} finalizado!")