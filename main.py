from mmu import MMU

mmu = MMU()

# Teste 1: Primeiros acessos (page faults)
print("=== TESTE 1: Primeiros acessos ===")
for i in range(5):
    mmu.acessar(i * 8192)

# Teste 2: Repetindo (HITs)
print("\n=== TESTE 2: Repetindo acessos ===")
for i in range(5):
    mmu.acessar(i * 8192)

# Teste 3: Forçando substituição
print("\n=== TESTE 3: Substituição FIFO ===")
for i in range(10):
    mmu.acessar(i * 8192)

mmu.status()