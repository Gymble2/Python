# Cria um nó, atribui o  valor a ele e cria um nó seguinte vazio
class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:

    def __init__(self):
        # Inicia uma lista com um nó (espaço) fictício que faz
        # remover um nó do inicio ser mais facil
        self.head = ListNode(-1)
        self.tail = self.head

    # pega um valor de um nó especificado
    # curr = ponteiro
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

        # insere um valor na "cabeça" da lista

    # new_node = novo nó
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        # verifica se a lista esta vazia ou se esta fora do esaço de nós
        if not new_node.next:
            self.tail = new_node

    # insere valor no final da lista  no "rabo"
    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    # remove um valor da posição(index) indicada
    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        # percorre a lista levando em conta que a posição da lista é menos 1
        while i < index and curr:
            i += 1
            curr = curr.next

        # remove o valor da da lista
        if curr and curr.next:
            # verifica se é o ultimo valor da lista e se for transforma a calda em ponteiro
            if curr.next == self.tail:
                self.tail = curr
            # Troca a posição dos ponteiros
            curr.next = curr.next.next
            return True
        return False

    # pega os valores dos ponteiros e imprime eles
    def getValues(self) -> list[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
