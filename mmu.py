from config import *

class MMU:
    def __init__(self):
        self.tabela = [-1] * NUM_PAGINAS      # página -> frame
        self.ram = [None] * NUM_FRAMES        # memória principal
        self.livres = list(range(NUM_FRAMES)) # frames vazios
        self.pf = 0   # page faults
        self.ac = 0   # acessos
    
    def acessar(self, end):
        self.ac += 1
        pag = end // TAM_PAGINA
        off = end % TAM_PAGINA
        
        print(f"\n[{self.ac}] End: {end} | Pag:{pag} Off:{off}")
        
        frame = self.tabela[pag]
        
        if frame != -1:  # HIT
            print(f"   HIT! Frame {frame}")
            return frame * TAM_PAGINA + off
        
        # PAGE FAULT
        print(f"   PAGE FAULT!")
        self.pf += 1
        
        if self.livres:  # tem frame livre
            frame = self.livres.pop(0)
            print(f"   Frame livre: {frame}")
        else:  # FIFO
            frame = self._fifo()
            old = self._quem(frame)
            self.tabela[old] = -1
            print(f"   Substituiu pagina {old} do frame {frame}")
        
        self.ram[frame] = f"Dados Pag{pag}"
        self.tabela[pag] = frame
        print(f"   Pagina {pag} -> frame {frame}")
        return frame * TAM_PAGINA + off
    
    def _fifo(self):
        if not hasattr(self, '_f'):
            self._f = list(range(NUM_FRAMES))
        return self._f.pop(0)
    
    def _quem(self, f):
        for p, frame in enumerate(self.tabela):
            if frame == f:
                return p
        return -1
    
    def status(self):
        print(f"\nTotal acessos: {self.ac}")
        print(f"Page faults: {self.pf}")
        print(f"Taxa: {self.pf/self.ac*100:.1f}%")