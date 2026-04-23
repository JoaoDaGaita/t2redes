# mmu.py - Memory Management Unit

from config import *

class MMU:
    def __init__(self):
        self.tabela_paginas = [-1] * NUM_PAGINAS
        self.memoria_principal = [bytearray(TAMANHO_PAGINA) for _ in range(NUM_FRAMES)]
        self.frames_livres = list(range(NUM_FRAMES))
        self.total_page_faults = 0
        self.total_acessos = 0
        self.dados_processos = self._criar_dados_simulados()
    
    def _criar_dados_simulados(self):
        dados = {}
        for pagina in range(NUM_PAGINAS):
            dados[pagina] = f"[Dados da Pagina {pagina}] " + "X" * 50
        return dados
    
    def traduzir_endereco(self, endereco_virtual):
        self.total_acessos += 1
        numero_pagina = endereco_virtual // TAMANHO_PAGINA
        offset = endereco_virtual % TAMANHO_PAGINA
        
        print(f"\n{'='*50}")
        print(f"📍 ACESSO #{self.total_acessos}")
        print(f"   Endereço Virtual: {endereco_virtual}")
        print(f"   Página: {numero_pagina} | Offset: {offset}")
        
        frame = self.tabela_paginas[numero_pagina]
        
        if frame != -1:
            print(f"{COR_VERDE}   ✅ HIT! Página {numero_pagina} está no FRAME {frame}{COR_RESET}")
            endereco_fisico = (frame * TAMANHO_PAGINA) + offset
            print(f"   Endereço Físico: {endereco_fisico}")
            return endereco_fisico, False
        else:
            print(f"{COR_VERMELHO}   ❌ PAGE FAULT! Página {numero_pagina} NÃO está na memória{COR_RESET}")
            self.total_page_faults += 1
            self._tratar_page_fault(numero_pagina)
            frame = self.tabela_paginas[numero_pagina]
            endereco_fisico = (frame * TAMANHO_PAGINA) + offset
            return endereco_fisico, True
    
    def _tratar_page_fault(self, numero_pagina):
        print(f"   🔄 Tratando PAGE FAULT para página {numero_pagina}")
        
        if self.frames_livres:
            frame = self.frames_livres.pop(0)
            print(f"{COR_VERDE}   📥 Frame livre encontrado: FRAME {frame}{COR_RESET}")
        else:
            frame = self._escolher_vitima()
            pagina_removida = self._encontrar_pagina_por_frame(frame)
            print(f"{COR_AZUL}   🔄 Sem frames livres! Substituindo página {pagina_removida} do FRAME {frame}{COR_RESET}")
            self.tabela_paginas[pagina_removida] = -1
        
        self.memoria_principal[frame] = bytearray(self.dados_processos[numero_pagina], 'utf-8')
        self.tabela_paginas[numero_pagina] = frame
        print(f"{COR_VERDE}   ✅ Página {numero_pagina} carregada no FRAME {frame}{COR_RESET}")
    
    def _escolher_vitima(self):
        if not hasattr(self, '_fila_fifo'):
            self._fila_fifo = list(range(NUM_FRAMES))
        return self._fila_fifo.pop(0)
    
    def _encontrar_pagina_por_frame(self, frame_busca):
        for pagina, frame in enumerate(self.tabela_paginas):
            if frame == frame_busca:
                return pagina
        return -1
    
    def mostrar_status(self):
        print("\n" + "="*50)
        print("📊 ESTADO ATUAL DA MEMÓRIA")
        print("="*50)
        print("\n📋 Tabela de Páginas (primeiras 20):")
        for pagina in range(min(20, NUM_PAGINAS)):
            frame = self.tabela_paginas[pagina]
            if frame != -1:
                print(f"      Página {pagina:3d} -> Frame {frame}")
        
        frames_usados = [f for f in range(NUM_FRAMES) if f not in self.frames_livres]
        print(f"\n💾 Frames em uso: {frames_usados}")
        print(f"   Frames livres: {self.frames_livres}")
        
        print(f"\n📈 Page Faults: {self.total_page_faults}/{self.total_acessos}")
        if self.total_acessos > 0:
            taxa = (self.total_page_faults / self.total_acessos) * 100
            print(f"   Taxa: {taxa:.1f}%")