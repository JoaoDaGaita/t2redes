# 🖥️ SIMULADOR DE MEMÓRIA VIRTUAL

## 📌 SOBRE O PROJETO

Simulador de paginação por demanda desenvolvido em Python para a disciplina de Sistemas Operacionais. Demonstra o funcionamento da MMU (Memory Management Unit), page faults e algoritmo de substituição FIFO.

## ⚙️ CONFIGURAÇÕES DO SISTEMA

| Parâmetro | Valor | Cálculo |
|-----------|-------|---------|
| Memória Virtual | 1 MB | 128 páginas × 8 KB |
| Memória Principal | 64 KB | 8 frames × 8 KB |
| Tamanho da Página/Frame | 8 KB | 8192 bytes |

## 📁 ESTRUTURA DOS ARQUIVOS

 simulador_memoria/
├── 📄 config.py # Configurações e constantes do sistema
├── 📄 mmu.py # MMU (tradução, page fault, FIFO)
├── 📄 processo.py # Processos leves concorrentes
└── 📄 main.py # Execução das simulações
text



## 🧠 ARQUIVO MMU - DETALHAMENTO COMPLETO

### 📌 O que é a MMU?

A Memory Management Unit (MMU) é o componente de hardware responsável por traduzir endereços virtuais gerados pelo processador em endereços físicos na memória RAM. Neste simulador, a MMU é implementada como uma classe Python que gerencia toda a lógica de paginação.

### 🏗️ Estruturas de Dados da MMU

| Variável | Tipo | Descrição |
|----------|------|-----------|
| tabela_paginas | list[int] | Vetor de 128 posições. Índice = página virtual, valor = frame físico. -1 = página não carregada |
| memoria_principal | list[bytearray] | Lista de 8 frames, cada um com 8192 bytes simulando a RAM real |
| frames_livres | list[int] | Lista de frames disponíveis para carregar novas páginas |
| total_page_faults | int | Contador acumulado de faltas de página durante toda execução |
| total_acessos | int | Contador acumulado de acessos à memória (cada tradução) |
| dados_processos | dict | Simula o disco rígido: mapeia página virtual para seu conteúdo |
| _fila_fifo | list[int] | Fila utilizada pelo algoritmo FIFO para controlar ordem de substituição |

### 🔧 Métodos da MMU

| Método | Descrição |
|--------|-----------|
| __init__() | Inicializa tabela de páginas com -1, cria memória principal vazia, preenche frames livres e estatísticas zero |
| _criar_dados_simulados() | Cria conteúdo fictício para cada uma das 128 páginas simulando o que estaria no disco |
| traduzir_endereco(endereco_virtual) | Método principal. Recebe endereço virtual, calcula página/offset, consulta tabela, retorna endereço físico e booleano de page fault |
| _tratar_page_fault(numero_pagina) | Carrega página do disco para memória. Decide entre frame livre ou substituição FIFO |
| _escolher_vitima() | Implementa algoritmo FIFO. Mantém fila de frames e remove o primeiro (mais antigo) |
| _encontrar_pagina_por_frame(frame_busca) | Varre tabela de páginas para descobrir qual página está ocupando um determinado frame |
| mostrar_status() | Exibe tabela de páginas, frames em uso/livres, estatísticas de page fault |

## Como executar
python main.py
