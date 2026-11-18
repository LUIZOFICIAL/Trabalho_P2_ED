Implementação de Referência (Python)Requer Python 3.8+:Bashpython src/algoritmo.py
 Diário de Uso de Inteligência ArtificialEtapaFerramenta / ModeloObjetivo do PromptValidação e Ajustes Realizados
1. Arquitetura e UIGeminiGerar o simulador visual autocontido em HTML/CSS/JS com máquina de estados passo a passo, cenários didáticos e painel de métricas.Testados todos os casos de borda na interface: inserção duplicada, remoção da raiz com 2 filhos, pausa/retomada e velocidade da animação.
2. ModularizaçãoGeminiSeparar a aplicação monolítica na estrutura oficial do repositório (index.html, styles.css, app.js) e criar algoritmo.py.Verificada a integridade dos caminhos relativos (styles.css e app.js) e executada a suíte unittest em Python para validar invariantes da BST.
3. DocumentaçãoGeminiEstruturar a fundamentação teórica e tabela de complexidade assintótica no README.md.Revisadas as notações Big-O ($O(\log n)$ vs $O(n)$) e alinhada a terminologia com o material da disciplina.
---

### 2. `src/algoritmo.py`

```python
"""
Implementação de referência de Árvore Binária de Busca (BST) em Python puro,
com métricas de comparações, cálculo de altura/balanceamento e casos de teste.
"""

from collections import deque
from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


@dataclass
class Node:
    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None
        self.comparisons: int = 0

    def reset_metrics(self) -> None:
        self.comparisons = 0

    def insert(self, value: int) -> bool:
        """Insere um valor na BST. Retorna False se o valor já existir."""
        self.reset_metrics()
        if self.root is None:
            self.root = Node(value)
            return True

        current = self.root
        while current is not None:
            self.comparisons += 1
            if value == current.value:
                return False
            elif value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return True
                current = current.right
        return False

    def search(self, value: int) -> Tuple[Optional[Node], int]:
        """Busca um valor na BST e retorna (nó_encontrado, comparações)."""
        self.reset_metrics()
        current = self.root
        while current is not None:
            self.comparisons += 1
            if value == current.value:
                return current, self.comparisons
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None, self.comparisons

    def delete(self, value: int) -> bool:
        """Remove um valor da BST tratando os 3 casos clássicos."""
        self.reset_metrics()
        self.root, deleted = self._delete_recursive(self.root, value)
        return deleted

    def _delete_recursive(
        self, node: Optional[Node], value: int
    ) -> Tuple[Optional[Node], bool]:
        if node is None:
            return None, False

        self.comparisons += 1
        if value < node.value:
            node.left, deleted = self._delete_recursive(node.left, value)
            return node, deleted
        elif value > node.value:
            node.right, deleted = self._delete_recursive(node.right, value)
            return node, deleted

        # Nó encontrado (value == node.value)
        # Caso 1 e 2: 0 ou 1 filho
        if node.left is None:
            return node.right, True
        if node.right is None:
            return node.left, True

        # Caso 3: 2 filhos -> substitui pelo sucessor in-order
        successor = self._min_node(node.right)
        node.value = successor.value
        node.right, _ = self._delete_recursive(node.right, successor.value)
        return node, True

    @staticmethod
    def _min_node(node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self) -> List[int]:
        result: List[int] = []
        self._inorder_rec(self.root, result)
        return result

    def _inorder_rec(self, node: Optional[Node], result: List[int]) -> None:
        if node is not None:
            self._inorder_rec(node.left, result)
            result.append(node.value)
            self._inorder_rec(node.right, result)

    def preorder(self) -> List[int]:
        result: List[int] = []
        self._preorder_rec(self.root, result)
        return result

    def _preorder_rec(self, node: Optional[Node], result: List[int]) -> None:
        if node is not None:
            result.append(node.value)
            self._preorder_rec(node.left, result)
            self._preorder_rec(node.right, result)

    def postorder(self) -> List[int]:
        result: List[int] = []
        self._postorder_rec(self.root, result)
        return result

    def _postorder_rec(self, node: Optional[Node], result: List[int]) -> None:
        if node is not None:
            self._postorder_rec(node.left, result)
            self._postorder_rec(node.right, result)
            result.append(node.value)

    def level_order(self) -> List[int]:
        if self.root is None:
            return []
        result: List[int] = []
        queue: deque[Node] = deque([self.root])
        while queue:
            current = queue.popleft()
            result.append(current.value)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return result

    def height(self) -> int:
        """Retorna a altura da árvore (-1 se vazia, 0 se apenas raiz)."""
        return self._height_rec(self.root)

    def _height_rec(self, node: Optional[Node]) -> int:
        if node is None:
            return -1
        return 1 + max(self._height_rec(node.left), self._height_rec(node.right))

    def is_balanced(self) -> bool:
        """Verifica se a árvore respeita a condição de balanceamento AVL (|fb| <= 1)."""
        def check(node: Optional[Node]) -> Tuple[bool, int]:
            if node is None:
                return True, -1
            left_ok, left_h = check(node.left)
            right_ok, right_h = check(node.right)
            balanced = left_ok and right_ok and abs(left_h - right_h) <= 1
            return balanced, 1 + max(left_h, right_h)

        return check(self.root)[0]


class TestBinarySearchTree(unittest.TestCase):
    def test_average_case_balanced(self) -> None:
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            self.assertTrue(bst.insert(v))

        self.assertEqual(bst.inorder(), [20, 30, 40, 50, 60, 70, 80])
        self.assertEqual(bst.preorder(), [50, 30, 20, 40, 70, 60, 80])
        self.assertEqual(bst.postorder(), [20, 40, 30, 60, 80, 70, 50])
        self.assertEqual(bst.level_order(), [50, 30, 70, 20, 40, 60, 80])
        self.assertEqual(bst.height(), 2)
        self.assertTrue(bst.is_balanced())

        node, comps = bst.search(60)
        self.assertIsNotNone(node)
        self.assertEqual(comps, 3)

    def test_worst_case_degenerate(self) -> None:
        bst = BinarySearchTree()
        values = [10, 20, 30, 40, 50]
        for v in values:
            bst.insert(v)

        self.assertEqual(bst.height(), 4)
        self.assertFalse(bst.is_balanced())
        node, comps = bst.search(50)
        self.assertIsNotNone(node)
        self.assertEqual(comps, 5)  # O(n) no pior caso

    def test_delete_all_cases(self) -> None:
        bst = BinarySearchTree()
        for v in [50, 30, 70, 20, 40, 60, 80, 65]:
            bst.insert(v)

        # Caso 1: Folha (20)
        self.assertTrue(bst.delete(20))
        self.assertEqual(bst.inorder(), [30, 40, 50, 60, 65, 70, 80])

        # Caso 2: 1 Filho (60 -> filho 65)
        self.assertTrue(bst.delete(60))
        self.assertEqual(bst.inorder(), [30, 40, 50, 65, 70, 80])

        # Caso 3: 2 Filhos (raiz 50 -> sucessor in-order é 65)
        self.assertTrue(bst.delete(50))
        self.assertEqual(bst.root.value, 65)
        self.assertEqual(bst.inorder(), [30, 40, 65, 70, 80])


if __name__ == "__main__":
    print("=== Demonstração Rápida: BST em Python ===")
    arvore = BinarySearchTree()
    for chave in [50, 30, 70, 20, 40, 60, 80]:
        arvore.insert(chave)

    print("Em-Ordem (In-Order):  ", arvore.inorder())
    print("Pré-Ordem (Pre-Order):", arvore.preorder())
    print("Pós-Ordem (Post-Order):", arvore.postorder())
    print("Em Nível (BFS):       ", arvore.level_order())
    print("Altura da Árvore:     ", arvore.height())
    print("Está Balanceada?:     ", arvore.is_balanced())
    print("\nExecutando testes unitários...\n")
    unittest.main(verbosity=2)
