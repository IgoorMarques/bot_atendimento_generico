from typing import List, Optional


class RespostaDTO:
    def __init__(self, id: int, texto_resposta: str, ordem: int, prox_bloco: Optional[int], tipo: str):
        self.id = id
        self.texto_resposta = texto_resposta
        self.ordem = ordem
        self.prox_bloco = prox_bloco
        self.tipo = tipo


class BlocoMensagemDTO:
    def __init__(self, id: int, tipo: str, conteudo: str, bloco_anterior: Optional[int], proximo_bloco: Optional[int],
                 respostas: List[RespostaDTO]):
        self.id = id
        self.tipo = tipo
        self.conteudo = conteudo
        self.bloco_anterior = bloco_anterior
        self.proximo_bloco = proximo_bloco
        self.respostas = respostas


class AtendimentoDTO:
    def __init__(self, data):
        self.id = data['id']
        self.nome = data['nome']
        self.usuario = data['usuario']
        self.atendimento_blocos = self.create_atendimento_dto(data['atendimento_blocos'])

        print(self.atendimento_blocos)

    def create_atendimento_dto(self, blocos_data):
        atendimento_blocos = []
        for bloco in blocos_data:
            respostas = [RespostaDTO(**resposta) for resposta in bloco['respostas']]
            bloco_dto = BlocoMensagemDTO(
                id=bloco['id'],
                tipo=bloco['tipo'],
                conteudo=bloco['conteudo'],
                bloco_anterior=bloco['bloco_anterior'],
                proximo_bloco=bloco['proximo_bloco'],
                respostas=respostas
            )
            atendimento_blocos.append(bloco_dto)
        return atendimento_blocos

    def get_first_bloco(self):
        for bloco in self.atendimento_blocos:
            if bloco.tipo == 'Start':
                return bloco
        return None

    def get_bloco_by_id(self, id):
        for bloco in self.atendimento_blocos:
            if bloco.id == int(id):
                return bloco
        return None

    def process_resposta_bloco(self, respostas: List[RespostaDTO], user_resposta):
        for resposta in respostas:
            if str(user_resposta) == str(resposta.texto_resposta):
                return resposta.prox_bloco
        return None
