# main.py - Programa Principal

from config import *
from mmu import MMU
from processo import ProcessoLeve

def main():
    print("="*50)
    print("   SIMULADOR DE MEMÓRIA VIRTUAL")
    print("="*50)
    print(f"\n📐 Configurações:")
    print(f"   Memória Virtual: 1 MB ({NUM_PAGINAS} páginas de {TAMANHO_PAGINA//1024} KB)")
    print(f"   Memória Principal: 64 KB ({NUM_FRAMES} frames de {TAMANHO_PAGINA//1024} KB)")
    
    mmu = MMU()
    
    # Simulação 1
    print("\n" + "="*50)
    print("   SIMULAÇÃO 1: ACESSOS SEQUENCIAIS")
    print("="*50)
    
    for i in range(5):
        mmu.traduzir_endereco(i * TAMANHO_PAGINA)
    
    for i in range(5):
        mmu.traduzir_endereco(i * TAMANHO_PAGINA)
    
    mmu.mostrar_status()
    
    # Simulação 2
    print("\n" + "="*50)
    print("   SIMULAÇÃO 2: PROCESSOS CONCORRENTES")
    print("="*50)
    
    p1 = ProcessoLeve("Processo A", mmu, [0, 100, 200, 300, 400])
    p2 = ProcessoLeve("Processo B", mmu, [500, 600, 700, 0, 100])
    p3 = ProcessoLeve("Processo C", mmu, [1000, 1100, 1200, 500, 50])
    
    p1.executar()
    p2.executar()
    p3.executar()
    
    # Simulação 3
    print("\n" + "="*50)
    print("   SIMULAÇÃO 3: TESTE DE SUBSTITUIÇÃO")
    print("="*50)
    print("   Acessando 15 páginas diferentes (forçando substituição)")
    
    for i in range(15):
        mmu.traduzir_endereco(i * TAMANHO_PAGINA)
    
    mmu.mostrar_status()
    
    # Relatório final
    print("\n" + "="*50)
    print("   RELATÓRIO FINAL")
    print("="*50)
    print(f"\n📊 Total de acessos: {mmu.total_acessos}")
    print(f"   Total de Page Faults: {mmu.total_page_faults}")
    if mmu.total_acessos > 0:
        taxa = (mmu.total_page_faults / mmu.total_acessos) * 100
        print(f"   Taxa de Page Fault: {taxa:.1f}%")
    
    frames_usados = NUM_FRAMES - len(mmu.frames_livres)
    print(f"\n💾 Frames ocupados: {frames_usados}/{NUM_FRAMES}")

if __name__ == "__main__":
    main()