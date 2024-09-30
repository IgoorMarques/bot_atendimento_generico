class Atendimento:
    def __init__(self, automacao):
        self.automacao = automacao
        self.blocks = self.automacao['atendimento_blocos']

    def find_block_by_id(self, block_id):
        for block in self.blocks:
            if block['id'] == block_id:
                return block
        return None

    def find_block_by_ordem(self, ordem):
        for block in self.blocks:
            if block['ordem'] == ordem:
                return block
        return None

    def block_has_options(self, block):
        if block['respostas']:
            return block['respostas']
        return None

    def processBlock(self, block):
        mensagem = block['conteudo']
        opcoes = self.block_has_options(block)
        return {
            "mensagem": mensagem,
            "opcoes": opcoes
        }

    def process_option(self, option):
        if option['prox_bloco']:
            return self.find_block_by_id(option['prox_bloco'])
        return None

