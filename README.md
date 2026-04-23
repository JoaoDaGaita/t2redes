# SIMULADOR DE MEMÓRIA VIRTUAL - VERSÃO SIMPLES

## SOBRE

Simulador de paginação por demanda com MMU, page faults e algoritmo FIFO. Versão simplificada e direta.

## CONFIGURAÇÕES

| Item | Valor |
|------|-------|
| Memória Virtual | 1 MB (128 páginas de 8 KB) |
| Memória Principal | 64 KB (8 frames de 8 KB) |
| Algoritmo | FIFO |

## ARQUIVOS

| Arquivo | Linhas | Função |
|---------|--------|--------|
| config.py | 4 | Constantes do sistema |
| mmu.py | 40 | MMU (tradução, page fault, FIFO) |
| main.py | 20 | Testes e execução |

## CÓDIGO

**config.py**
```python
TAM_PAGINA = 8192    # 8 KB
NUM_PAGINAS = 128    # 1 MB
NUM_FRAMES = 8       # 64 KB