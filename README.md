# Simulador Visual Interativo — Árvore Binária de Busca (BST)

Projeto desenvolvido para a disciplina de **Estruturas de Dados (Trabalho P2)**, contendo a implementação de referência em Python puro e um simulador visual interativo executado diretamente no navegador, com execução passo a passo, análise de estado e cenários didáticos.

---

##  Demonstração em Vídeo
Não haverá video.

---

##  Organização do Repositório

```  Text
trabalho-p2-ed/
├── README.md               # Documentação teórica, Big-O, Diário de IA e LINK DO VÍDEO
└── src/
    ├── algoritmo.py        # Implementação em Python puro + casos de teste
    └── demo/
        ├── index.html      # Interface do simulador visual
        ├── styles.css      # Estilização da página e animações
        └── app.js          # Lógica da simulação passo a passo
```

##  Fundamentação Teórica:
Uma Árvore Binária de Busca (Binary Search Tree — BST) é uma estrutura de dados hierárquica baseada em nós na qual cada nó armazena uma chave (valor) e possui no máximo dois filhos: subárvore esquerda e subárvore direita.
Propriedade Invariante da BSTPara qualquer nó $x$ da árvore:Todos os nós na subárvore esquerda de $x$ possuem chaves estritamente menores que $x.\text{valor}$.Todos os nós na subárvore direita de $x$ possuem chaves estritamente maiores que $x.\text{valor}$.
Ambas as subárvores esquerda e direita também são Árvores Binárias de Busca.Operações PrincipaisBusca (search): Inicia na raiz e compara o alvo com o nó atual, descartando metade da árvore restante a cada passo.Inserção (insert): 
Percorre a árvore seguindo a propriedade invariante até encontrar uma referência nula (None / null), onde o novo nó folha é alocado.Remoção (delete): Divide-se em três casos:Nó folha (0 filhos): Removido diretamente.
Nó com 1 filho: Substituído diretamente pelo seu único filho.Nó com 2 filhos: Substituído pelo seu sucessor in-order (menor valor da subárvore direita), seguido da remoção recursiva desse sucessor.Percursos (Travessias):Em-Ordem (In-Order — E, R, D): 
Visita os elementos em ordem crescente.Pré-Ordem (Pre-Order — R, E, D): Útil para clonar ou serializar a topologia da árvore.Pós-Ordem (Post-Order — E, D, R): Útil para desalocação segura de memória.
Em Nível (Level-Order / BFS): Visita nível por nível utilizando uma fila (FIFO).

##  Análise de Complexidade Assintótica (Big-O)
Onde $n$ é o número total de nós e $h$ é a altura da árvore:
Operação, "Caso Médio (Árvore Balanceada, h=⌊log2​n⌋)","Pior Caso (Árvore Degenerada, h=n−1)",Complexidade Espacial (Auxiliar)
Busca, O(logn),O(n),O(1) iterativa / O(h) recursiva
Inserção, O(logn),O(n),O(1) iterativa / O(h) recursiva
Remoção, O(logn),O(n),O(h) recursiva
Percursos (DFS/BFS),Θ(n),Θ(n),O(h) DFS / O(n) BFS

Caso Médio: Ocorre quando os elementos são inseridos em ordem aleatória, mantendo a altura próxima de $\log_2 n$.
Pior Caso: Ocorre quando os elementos são inseridos já ordenados (crescente ou decrescente), degenerando a BST em uma lista encadeada linear.

 Como Executar: 1. Simulador Visual Interativo (Web)Não requer instalação de servidores ou dependências externas: Navegue até a pasta src/demo/.Abra o arquivo index.html diretamente em qualquer navegador moderno (Chrome, Edge, Firefox, Safari).
