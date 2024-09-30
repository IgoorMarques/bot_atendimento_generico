import json
import os

from celery import Celery

from app.bot import Bot
from app.dtos import AtendimentoDTO
from app.wpp_message_dto import WhatsappMessage

CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'

CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# Configuração do Celery
celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

wpp_token = "EAALsGcAB8xkBOzAq4oQLuzISgUZB7MA9J7Xy1HizXlyQEqqPsIpN2Cy8aAeXnNa29oymai3Wi6qQXmlpVLSHHtrp06oPyDGY5GKHmTnOj1IjCC0g23V7IZBllXGDyXpKgl2qDzzguZCh3nlNDBA4rMRJHfNaEtjrtELKPGHJiIsDJ2hODG6Q2a5s2rSV0ChGsZAXliWC8jQtTLsT9C4POgkz3o4ZD"
phone_id = "315297828332138"


BARBEARIA = '''
{
  "id": 2,
  "nome": "Barbearia",
  "usuario": 1,
  "atendimento_blocos": [
    {
      "id": 1,
      "tipo": "Start",
      "conteudo": "Bem-vindo à Barbearia X! Como posso ajudá-lo hoje?",
      "bloco_anterior": null,
      "proximo_bloco": 2,
      "respostas": []
    },
    {
      "id": 2,
      "tipo": "Opções",
      "conteudo": "Escolha uma das opções abaixo:",
      "bloco_anterior": 1,
      "proximo_bloco": 3,
      "respostas": [
        {
          "id": 1,
          "texto_resposta": "Agendar um horário",
          "ordem": 1,
          "prox_bloco": 3,
          "tipo": "Resposta"
        },
        {
          "id": 2,
          "texto_resposta": "Ver nossos serviços",
          "ordem": 2,
          "prox_bloco": 4,
          "tipo": "Resposta"
        },
        {
          "id": 3,
          "texto_resposta": "Ver preços",
          "ordem": 3,
          "prox_bloco": 5,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 3,
      "tipo": "Texto",
      "conteudo": "Para agendar um horário, por favor, informe a data e o horário desejado.",
      "bloco_anterior": 2,
      "proximo_bloco": 7,
      "respostas": [
        {
          "id": 5,
          "texto_resposta": "Voltar",
          "ordem": 1,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 4,
      "tipo": "Texto",
      "conteudo": "Nossos serviços incluem: Corte de cabelo, Barba, Hidratação e mais.",
      "bloco_anterior": 2,
      "proximo_bloco": 8,
      "respostas": [
        {
          "id": 6,
          "texto_resposta": "Ver detalhes",
          "ordem": 1,
          "prox_bloco": 8,
          "tipo": "Resposta"
        },
        {
          "id": 7,
          "texto_resposta": "Voltar",
          "ordem": 2,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 5,
      "tipo": "Texto",
      "conteudo": "Nossos preços são: Corte de cabelo - R$ 50, Barba - R$ 30, Hidratação - R$ 70.",
      "bloco_anterior": 2,
      "proximo_bloco": 9,
      "respostas": [
        {
          "id": 8,
          "texto_resposta": "Agendar um horário",
          "ordem": 1,
          "prox_bloco": 3,
          "tipo": "Resposta"
        },
        {
          "id": 9,
          "texto_resposta": "Voltar",
          "ordem": 2,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 6,
      "tipo": "Texto",
      "conteudo": "Um de nossos atendentes estará com você em breve.",
      "bloco_anterior": 2,
      "proximo_bloco": null,
      "respostas": []
    },
    {
      "id": 7,
      "tipo": "Texto",
      "conteudo": "Obrigado! Seu horário foi agendado. Se precisar de mais alguma coisa, estamos aqui para ajudar.",
      "bloco_anterior": 3,
      "proximo_bloco": null,
      "respostas": []
    },
    {
      "id": 8,
      "tipo": "Opções",
      "conteudo": "Escolha um serviço para ver mais detalhes:",
      "bloco_anterior": 4,
      "proximo_bloco": 10,
      "respostas": [
        {
          "id": 10,
          "texto_resposta": "Corte de cabelo",
          "ordem": 1,
          "prox_bloco": 10,
          "tipo": "Resposta"
        },
        {
          "id": 11,
          "texto_resposta": "Barba",
          "ordem": 2,
          "prox_bloco": 11,
          "tipo": "Resposta"
        },
        {
          "id": 12,
          "texto_resposta": "Hidratação",
          "ordem": 3,
          "prox_bloco": 12,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 9,
      "tipo": "Texto",
      "conteudo": "Gostaria de agendar um horário?",
      "bloco_anterior": 5,
      "proximo_bloco": 3,
      "respostas": [
        {
          "id": 13,
          "texto_resposta": "Sim",
          "ordem": 1,
          "prox_bloco": 3,
          "tipo": "Resposta"
        },
        {
          "id": 14,
          "texto_resposta": "Não",
          "ordem": 2,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 10,
      "tipo": "Texto",
      "conteudo": "Corte de cabelo - R$ 50. Agende um horário agora.",
      "bloco_anterior": 8,
      "proximo_bloco": 3,
      "respostas": [
        {
          "id": 15,
          "texto_resposta": "Agendar",
          "ordem": 1,
          "prox_bloco": 3,
          "tipo": "Resposta"
        },
        {
          "id": 16,
          "texto_resposta": "Voltar",
          "ordem": 2,
          "prox_bloco": 8,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 11,
      "tipo": "Texto",
      "conteudo": "Barba - R$ 30. Agende um horário agora.",
      "bloco_anterior": 8,
      "proximo_bloco": 3,
      "respostas": [
        {
          "id": 17,
          "texto_resposta": "Agendar",
          "ordem": 1,
          "prox_bloco": 3,
          "tipo": "Resposta"
        },
        {
          "id": 18,
          "texto_resposta": "Voltar",
          "ordem": 2,
          "prox_bloco": 8,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 12,
      "tipo": "Texto",
      "conteudo": "Hidratação - R$ 70. Agende um horário agora.",
      "bloco_anterior": 8,
      "proximo_bloco": 3,
      "respostas": [
        {
          "id": 19,
          "texto_resposta": "Agendar",
          "ordem": 1,
          "prox_bloco": 3,
          "tipo": "Resposta"
        },
        {
          "id": 20,
          "texto_resposta": "Voltar",
          "ordem": 2,
          "prox_bloco": 8,
          "tipo": "Resposta"
        }
      ]
    }
  ]
}
'''
RESTAURANTE = """
{
  "id": 3,
  "nome": "Restaurante",
  "usuario": 1,
  "atendimento_blocos": [
    {
      "id": 1,
      "tipo": "Start",
      "conteudo": "Bem-vindo ao Restaurante Y! Como posso ajudá-lo hoje?",
      "bloco_anterior": null,
      "proximo_bloco": 2,
      "respostas": []
    },
    {
      "id": 2,
      "tipo": "Opções",
      "conteudo": "Escolha uma das opções abaixo:",
      "bloco_anterior": 1,
      "proximo_bloco": 3,
      "respostas": [
        {
          "id": 1,
          "texto_resposta": "Ver cardápio",
          "ordem": 1,
          "prox_bloco": 3,
          "tipo": "Resposta"
        },
        {
          "id": 2,
          "texto_resposta": "Fazer reserva",
          "ordem": 2,
          "prox_bloco": 4,
          "tipo": "Resposta"
        },
        {
          "id": 3,
          "texto_resposta": "Fazer pedido para entrega",
          "ordem": 3,
          "prox_bloco": 5,
          "tipo": "Resposta"
        },
        {
          "id": 4,
          "texto_resposta": "Falar com um atendente",
          "ordem": 4,
          "prox_bloco": 6,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 3,
      "tipo": "Texto",
      "conteudo": "Aqui está o nosso cardápio: Prato 1 - R$ 50, Prato 2 - R$ 40, Prato 3 - R$ 30.",
      "bloco_anterior": 2,
      "proximo_bloco": 7,
      "respostas": [
        {
          "id": 5,
          "texto_resposta": "Fazer pedido",
          "ordem": 1,
          "prox_bloco": 5,
          "tipo": "Resposta"
        },
        {
          "id": 6,
          "texto_resposta": "Voltar",
          "ordem": 2,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 4,
      "tipo": "Texto",
      "conteudo": "Para fazer uma reserva, por favor, informe a data, o horário e o número de pessoas.",
      "bloco_anterior": 2,
      "proximo_bloco": 8,
      "respostas": [
        {
          "id": 7,
          "texto_resposta": "Voltar",
          "ordem": 1,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 5,
      "tipo": "Texto",
      "conteudo": "Para fazer um pedido para entrega, por favor, informe o seu endereço e o pedido desejado.",
      "bloco_anterior": 2,
      "proximo_bloco": 9,
      "respostas": [
        {
          "id": 8,
          "texto_resposta": "Voltar",
          "ordem": 1,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 6,
      "tipo": "Texto",
      "conteudo": "Um de nossos atendentes estará com você em breve.",
      "bloco_anterior": 2,
      "proximo_bloco": null,
      "respostas": []
    },
    {
      "id": 7,
      "tipo": "Texto",
      "conteudo": "Gostaria de fazer um pedido ou voltar ao menu principal?",
      "bloco_anterior": 3,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 9,
          "texto_resposta": "Fazer pedido",
          "ordem": 1,
          "prox_bloco": 5,
          "tipo": "Resposta"
        },
        {
          "id": 10,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 2,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 8,
      "tipo": "Texto",
      "conteudo": "Obrigado! Sua reserva foi realizada. Se precisar de mais alguma coisa, estamos aqui para ajudar.",
      "bloco_anterior": 4,
      "proximo_bloco": null,
      "respostas": []
    },
    {
      "id": 9,
      "tipo": "Texto",
      "conteudo": "Obrigado! Seu pedido foi realizado e estará a caminho em breve. Se precisar de mais alguma coisa, estamos aqui para ajudar.",
      "bloco_anterior": 5,
      "proximo_bloco": null,
      "respostas": []
    }
  ]
}

"""
CLINICA = """
{
  "id": 5,
  "nome": "Clínica de Saúde",
  "usuario": 1,
  "atendimento_blocos": [
    {
      "id": 1,
      "tipo": "Start",
      "conteudo": "Bem-vindo à Clínica de Saúde ABC! Como posso ajudá-lo hoje?",
      "bloco_anterior": null,
      "proximo_bloco": 2,
      "respostas": []
    },
    {
      "id": 2,
      "tipo": "Opções",
      "conteudo": "Escolha uma das opções abaixo:",
      "bloco_anterior": 1,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 1,
          "texto_resposta": "Agendar consulta",
          "ordem": 1,
          "prox_bloco": 3,
          "tipo": "Resposta"
        },
        {
          "id": 2,
          "texto_resposta": "Ver especialidades",
          "ordem": 2,
          "prox_bloco": 4,
          "tipo": "Resposta"
        },
        {
          "id": 3,
          "texto_resposta": "Informações sobre exames",
          "ordem": 3,
          "prox_bloco": 5,
          "tipo": "Resposta"
        },
        {
          "id": 4,
          "texto_resposta": "Falar com um atendente",
          "ordem": 4,
          "prox_bloco": 6,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 3,
      "tipo": "Texto",
      "conteudo": "Para agendar uma consulta, por favor, informe a data, o horário e a especialidade desejada.",
      "bloco_anterior": 2,
      "proximo_bloco": 7,
      "respostas": [
        {
          "id": 5,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 1,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 4,
      "tipo": "Texto",
      "conteudo": "Nossas especialidades incluem: - Cardiologia - Dermatologia - Ginecologia - Pediatria - Ortopedia",
      "bloco_anterior": 2,
      "proximo_bloco": 8,
      "respostas": [
        {
          "id": 6,
          "texto_resposta": "Agendar consulta",
          "ordem": 1,
          "prox_bloco": 3,
          "tipo": "Resposta"
        },
        {
          "id": 7,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 2,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 5,
      "tipo": "Texto",
      "conteudo": "Para informações sobre exames, escolha uma das opções abaixo:",
      "bloco_anterior": 2,
      "proximo_bloco": 9,
      "respostas": [
        {
          "id": 8,
          "texto_resposta": "Exames laboratoriais",
          "ordem": 1,
          "prox_bloco": 10,
          "tipo": "Resposta"
        },
        {
          "id": 9,
          "texto_resposta": "Exames de imagem",
          "ordem": 2,
          "prox_bloco": 11,
          "tipo": "Resposta"
        },
        {
          "id": 10,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 3,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 6,
      "tipo": "Texto",
      "conteudo": "Um de nossos atendentes estará com você em breve.",
      "bloco_anterior": 2,
      "proximo_bloco": null,
      "respostas": []
    },
    {
      "id": 7,
      "tipo": "Texto",
      "conteudo": "Obrigado! Sua consulta foi agendada. Se precisar de mais alguma coisa, estamos aqui para ajudar.",
      "bloco_anterior": 3,
      "proximo_bloco": null,
      "respostas": []
    },
    {
      "id": 8,
      "tipo": "Opções",
      "conteudo": "Escolha uma especialidade para agendar uma consulta:",
      "bloco_anterior": 4,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 11,
          "texto_resposta": "Cardiologia",
          "ordem": 1,
          "prox_bloco": 3,
          "tipo": "Resposta"
        },
        {
          "id": 12,
          "texto_resposta": "Dermatologia",
          "ordem": 2,
          "prox_bloco": 3,
          "tipo": "Resposta"
        },
        {
          "id": 13,
          "texto_resposta": "Ginecologia",
          "ordem": 3,
          "prox_bloco": 3,
          "tipo": "Resposta"
        },
        {
          "id": 14,
          "texto_resposta": "Pediatria",
          "ordem": 4,
          "prox_bloco": 3,
          "tipo": "Resposta"
        },
        {
          "id": 15,
          "texto_resposta": "Ortopedia",
          "ordem": 5,
          "prox_bloco": 3,
          "tipo": "Resposta"
        },
        {
          "id": 16,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 6,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 9,
      "tipo": "Opções",
      "conteudo": "Escolha uma opção para saber mais sobre exames:",
      "bloco_anterior": 5,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 17,
          "texto_resposta": "Exames laboratoriais",
          "ordem": 1,
          "prox_bloco": 10,
          "tipo": "Resposta"
        },
        {
          "id": 18,
          "texto_resposta": "Exames de imagem",
          "ordem": 2,
          "prox_bloco": 11,
          "tipo": "Resposta"
        },
        {
          "id": 19,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 3,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 10,
      "tipo": "Texto",
      "conteudo": "Os exames laboratoriais disponíveis são: - Hemograma completo - Glicemia - Colesterol - Função hepática",
      "bloco_anterior": 5,
      "proximo_bloco": 12,
      "respostas": [
        {
          "id": 20,
          "texto_resposta": "Voltar ao menu de exames",
          "ordem": 1,
          "prox_bloco": 9,
          "tipo": "Resposta"
        },
        {
          "id": 21,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 2,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 11,
      "tipo": "Texto",
      "conteudo": "Os exames de imagem disponíveis são: - Raio-X - Ultrassonografia- Tomografia - Ressonância magnética",
      "bloco_anterior": 5,
      "proximo_bloco": 12,
      "respostas": [
        {
          "id": 22,
          "texto_resposta": "Voltar ao menu de exames",
          "ordem": 1,
          "prox_bloco": 9,
          "tipo": "Resposta"
        },
        {
          "id": 23,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 2,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 12,
      "tipo": "Opções",
      "conteudo": "Gostaria de saber mais alguma coisa?",
      "bloco_anterior": 10,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 24,
          "texto_resposta": "Ver especialidades",
          "ordem": 1,
          "prox_bloco": 4,
          "tipo": "Resposta"
        },
        {
          "id": 25,
          "texto_resposta": "Informações sobre exames",
          "ordem": 2,
          "prox_bloco": 5,
          "tipo": "Resposta"
        },
        {
          "id": 26,
          "texto_resposta": "Agendar consulta",
          "ordem": 3,
          "prox_bloco": 3,
          "tipo": "Resposta"
        },
        {
          "id": 27,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 4,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    }
  ]
}
"""

ACAITERIA = """{
  "id": 5,
  "nome": "Clínica de Saúde",
  "usuario": 1,
  "atendimento_blocos": [
    {
      "id": 1,
      "tipo": "Start",
      "conteudo": "Bem-vindo ao Point do Açaí!\\nOlá! Que bom ter você aqui! Somos apaixonados por oferecer o melhor açaí, sempre fresquinho e delicioso, preparado com todo carinho.\\nComo podemos tornar seu dia mais doce hoje?",
      "bloco_anterior": null,
      "proximo_bloco": 2,
      "respostas": []
    },
    {
      "id": 2,
      "tipo": "list_button",
      "conteudo": "No que podemos ajudar hoje? Escolha uma das opções abaixo:",
      "bloco_anterior": 1,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 1,
          "texto_resposta": "Ver cardápio",
          "ordem": 1,
          "prox_bloco": 3,
          "tipo": "Resposta"
        },
        {
          "id": 2,
          "texto_resposta": "Saber mais",
          "ordem": 2,
          "prox_bloco": 5,
          "tipo": "Resposta"
        },
        {
          "id": 3,
          "texto_resposta": "Ver promoções",
          "ordem": 3,
          "prox_bloco": 6,
          "tipo": "Resposta"
        },
        {
          "id": 4,
          "texto_resposta": "Falar com atendente",
          "ordem": 4,
          "prox_bloco": 7,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 3,
      "tipo": "list_button",
      "conteudo": "Cardápio Point do Açaí:\\nEscolha o seu tamanho preferido e veja os detalhes:",
      "bloco_anterior": 2,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 5,
          "texto_resposta": "Copo 300ml",
          "ordem": 1,
          "prox_bloco": 8,
          "tipo": "Resposta"
        },
        {
          "id": 6,
          "texto_resposta": "Copo 400ml",
          "ordem": 2,
          "prox_bloco": 8,
          "tipo": "Resposta"
        },
        {
          "id": 7,
          "texto_resposta": "Copo 500ml",
          "ordem": 3,
          "prox_bloco": 8,
          "tipo": "Resposta"
        },
        {
          "id": 8,
          "texto_resposta": "Marmita 750ml",
          "ordem": 4,
          "prox_bloco": 8,
          "tipo": "Resposta"
        },
        {
          "id": 9,
          "texto_resposta": "Sorvete 5 bolas",
          "ordem": 5,
          "prox_bloco": 8,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 4,
      "tipo": "opcoes",
      "conteudo": "Açaí 300ml com 2 Acompanhamentos  \\n  \\n   – R$ 10,00 \\n\\nDelicie-se com o nosso açaí de 300ml, perfeito para qualquer hora do dia! Escolha dois acompanhamentos irresistíveis entre:\\n\\n- Amendoim Granulado\\n- Amendoim Banda\\n- Floco de Arroz\\n- Ovo Maltine\\n- Granola\\n- Chokoboll\\n\\nQuer dar um toque ainda mais especial? Adicione os extras por apenas R$ 3,00 cada:\\n\\n- Morango Fresco\\n- Creme de Ninho\\n- M&M’s Coloridos\\n- Creme de Avelã\\n- Leite Ninho\\n\\nMonte o açaí do seu jeito e aproveite um sabor incomparável por apenas R$ 10,00 (sem adicionais). Garanta essa delícia agora mesmo!",
      "bloco_anterior": 3,
      "proximo_bloco": 9,
      "respostas": [
        {
          "id": 6,
          "texto_resposta": "Montar meu açaí",
          "ordem": 1,
          "prox_bloco": 10,
          "tipo": "Resposta"
        },
        {
          "id": 7,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 2,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 5,
      "tipo": "list_button",
      "conteudo": "Nossos produtos são feitos com os melhores ingredientes, garantindo uma experiência deliciosa em cada pedido.\\nO açaí que usamos é 100% natural, sem adição de conservantes, e trabalhamos com os melhores acompanhamentos e extras para você personalizar do jeito que quiser.\\nQuer saber mais sobre como nossos produtos são feitos ou sobre os benefícios do açaí? Escolha uma das opções abaixo.",
      "bloco_anterior": 2,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 8,
          "texto_resposta": "Processo de produção",
          "ordem": 1,
          "prox_bloco": 11,
          "tipo": "Resposta"
        },
        {
          "id": 9,
          "texto_resposta": "Benefícios do açaí",
          "ordem": 2,
          "prox_bloco": 12,
          "tipo": "Resposta"
        },
        {
          "id": 10,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 3,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 6,
      "tipo": "list_button",
      "conteudo": "Promoções do dia:\\nAproveite nossas ofertas especiais para hoje!",
      "bloco_anterior": 2,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 11,
          "texto_resposta": "Promoção Açaí 500ml + 2 Acompanhamentos - R$ 15,00",
          "ordem": 1,
          "prox_bloco": 13,
          "tipo": "Resposta"
        },
        {
          "id": 12,
          "texto_resposta": "Promoção Açaí 400ml + 3 Acompanhamentos - R$ 12,00",
          "ordem": 2,
          "prox_bloco": 14,
          "tipo": "Resposta"
        },
        {
          "id": 13,
          "texto_resposta": "Promoção Marmita 750ml + 3 Acompanhamentos - R$ 20,00",
          "ordem": 3,
          "prox_bloco": 15,
          "tipo": "Resposta"
        },
        {
          "id": 14,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 4,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 7,
      "tipo": "list_button",
      "conteudo": "Um de nossos atendentes estará disponível para te ajudar em instantes.\\nPor favor, aguarde enquanto conectamos você.",
      "bloco_anterior": 2,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 15,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 1,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 8,
      "tipo": "list_button",
      "conteudo": "Por favor, selecione o tamanho do copo que você gostaria para o seu açaí:",
      "bloco_anterior": 3,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 16,
          "texto_resposta": "300ml",
          "ordem": 1,
          "prox_bloco": 4,
          "tipo": "Resposta"
        },
        {
          "id": 17,
          "texto_resposta": "400ml",
          "ordem": 2,
          "prox_bloco": 4,
          "tipo": "Resposta"
        },
        {
          "id": 18,
          "texto_resposta": "500ml",
          "ordem": 3,
          "prox_bloco": 4,
          "tipo": "Resposta"
        },
        {
          "id": 19,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 4,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 9,
      "tipo": "list_button",
      "conteudo": "Seu açaí de 300ml está quase pronto! Escolha os dois acompanhamentos que você deseja incluir:",
      "bloco_anterior": 4,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 20,
          "texto_resposta": "Amendoim Granulado e Floco de Arroz",
          "ordem": 1,
          "prox_bloco": 16,
          "tipo": "Resposta"
        },
        {
          "id": 21,
          "texto_resposta": "Amendoim Banda e Ovo Maltine",
          "ordem": 2,
          "prox_bloco": 16,
          "tipo": "Resposta"
        },
        {
          "id": 22,
          "texto_resposta": "Granola e Chokoboll",
          "ordem": 3,
          "prox_bloco": 16,
          "tipo": "Resposta"
        },
        {
          "id": 23,
          "texto_resposta": "Escolher outros tamanhos",
          "ordem": 4,
          "prox_bloco": 8,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 10,
      "tipo": "list_button",
      "conteudo": "Agora que você montou o seu açaí, vamos finalizar o pedido.\\nDeseja adicionar algum extra por R$ 3,00 cada?",
      "bloco_anterior": 9,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 24,
          "texto_resposta": "Sim, adicionar extras",
          "ordem": 1,
          "prox_bloco": 17,
          "tipo": "Resposta"
        },
        {
          "id": 25,
          "texto_resposta": "Não, finalizar pedido",
          "ordem": 2,
          "prox_bloco": 18,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 11,
      "tipo": "list_button",
      "conteudo": "Nosso processo de produção é cuidadosamente planejado para garantir que cada açaí chegue até você com a máxima qualidade.\\nDesde a escolha das frutas até o armazenamento e o preparo, seguimos padrões rigorosos de higiene e frescor.\\nSe quiser saber mais detalhes ou ver um vídeo do processo, escolha abaixo.",
      "bloco_anterior": 5,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 26,
          "texto_resposta": "Ver vídeo processo",
          "ordem": 1,
          "prox_bloco": 19,
          "tipo": "Resposta"
        },
        {
          "id": 27,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 2,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 12,
      "tipo": "list_button",
      "conteudo": "O açaí é uma superfruta repleta de benefícios para a saúde. Rico em antioxidantes, vitaminas e minerais, ele ajuda a fortalecer o sistema imunológico, melhora a saúde do coração e é uma excelente fonte de energia.\\nQuer saber mais? Escolha abaixo para ver um artigo completo ou assistir a um vídeo.",
      "bloco_anterior": 5,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 28,
          "texto_resposta": "Mais sobre os benefícios",
          "ordem": 1,
          "prox_bloco": 20,
          "tipo": "Resposta"
        },
        {
          "id": 29,
          "texto_resposta": "Assistir um vídeo",
          "ordem": 2,
          "prox_bloco": 21,
          "tipo": "Resposta"
        },
        {
          "id": 30,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 3,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 13,
      "tipo": "list_button",
      "conteudo": "Você escolheu a promoção Açaí 500ml + 2 Acompanhamentos por R$ 15,00.\\nQuais acompanhamentos você deseja adicionar?",
      "bloco_anterior": 6,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 31,
          "texto_resposta": "Amendoim Granulado",
          "ordem": 1,
          "prox_bloco": 22,
          "tipo": "Resposta"
        },
        {
          "id": 32,
          "texto_resposta": "Amendoim Banda e Ovo Maltine",
          "ordem": 2,
          "prox_bloco": 22,
          "tipo": "Resposta"
        },
        {
          "id": 33,
          "texto_resposta": "Granola e Chokoboll",
          "ordem": 3,
          "prox_bloco": 22,
          "tipo": "Resposta"
        },
        {
          "id": 34,
          "texto_resposta": "Escolher outra promoção",
          "ordem": 4,
          "prox_bloco": 6,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 14,
      "tipo": "list_button",
      "conteudo": "Você escolheu a promoção Açaí 400ml + 3 Acompanhamentos por R$ 12,00.\\nQuais acompanhamentos você deseja adicionar?",
      "bloco_anterior": 6,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 35,
          "texto_resposta": "Amendoim Granulado, Floco de Arroz e Granola",
          "ordem": 1,
          "prox_bloco": 22,
          "tipo": "Resposta"
        },
        {
          "id": 36,
          "texto_resposta": "Amendoim Banda, Ovo Maltine e Chokoboll",
          "ordem": 2,
          "prox_bloco": 22,
          "tipo": "Resposta"
        },
        {
          "id": 37,
          "texto_resposta": "Granola, Chokoboll e Ovo Maltine",
          "ordem": 3,
          "prox_bloco": 22,
          "tipo": "Resposta"
        },
        {
          "id": 38,
          "texto_resposta": "Escolher outra promoção",
          "ordem": 4,
          "prox_bloco": 6,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 15,
      "tipo": "list_button",
      "conteudo": "Você escolheu a promoção Marmita 750ml + 3 Acompanhamentos por R$ 20,00.\\nQuais acompanhamentos você deseja adicionar?",
      "bloco_anterior": 6,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 39,
          "texto_resposta": "Amendoim Granulado, Floco de Arroz e Ovo Maltine",
          "ordem": 1,
          "prox_bloco": 22,
          "tipo": "Resposta"
        },
        {
          "id": 40,
          "texto_resposta": "Amendoim Banda, Granola e Chokoboll",
          "ordem": 2,
          "prox_bloco": 22,
          "tipo": "Resposta"
        },
        {
          "id": 41,
          "texto_resposta": "Granola, Chokoboll e Morango Fresco",
          "ordem": 3,
          "prox_bloco": 22,
          "tipo": "Resposta"
        },
        {
          "id": 42,
          "texto_resposta": "Escolher outra promoção",
          "ordem": 4,
          "prox_bloco": 6,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 16,
      "tipo": "list_button",
      "conteudo": "Seu açaí está quase pronto! Vamos finalizar o seu pedido?\\nVocê gostaria de adicionar algum extra?",
      "bloco_anterior": 9,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 43,
          "texto_resposta": "Adicionar Morango Fresco",
          "ordem": 1,
          "prox_bloco": 23,
          "tipo": "Resposta"
        },
        {
          "id": 44,
          "texto_resposta": "Adicionar Creme de Avelã",
          "ordem": 2,
          "prox_bloco": 23,
          "tipo": "Resposta"
        },
        {
          "id": 45,
          "texto_resposta": "Não adicionar extras",
          "ordem": 3,
          "prox_bloco": 18,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 17,
      "tipo": "list_button",
      "conteudo": "Extras adicionados!\\nSeu açaí será finalizado com os seguintes extras: \\n\\n- Morango Fresco\\n- Creme de Avelã\\n\\nDeseja finalizar o pedido agora?",
      "bloco_anterior": 10,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 46,
          "texto_resposta": "Finalizar pedido",
          "ordem": 1,
          "prox_bloco": 18,
          "tipo": "Resposta"
        },
        {
          "id": 47,
          "texto_resposta": "Adicionar mais extras",
          "ordem": 2,
          "prox_bloco": 16,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 18,
      "tipo": "list_button",
      "conteudo": "Seu pedido foi finalizado com sucesso!\\nAgradecemos por escolher o Point do Açaí. Em breve, você receberá seu pedido.\\nGostaria de receber uma notificação quando o pedido estiver a caminho?",
      "bloco_anterior": 10,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 48,
          "texto_resposta": "Sim, receber notificações",
          "ordem": 1,
          "prox_bloco": 24,
          "tipo": "Resposta"
        },
        {
          "id": 49,
          "texto_resposta": "Não, obrigado",
          "ordem": 2,
          "prox_bloco": 24,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 19,
      "tipo": "list_button",
      "conteudo": "Aqui está o vídeo sobre o nosso processo de produção.\\n[Clique aqui para assistir ao vídeo]",
      "bloco_anterior": 11,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 50,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 1,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 20,
      "tipo": "list_button",
      "conteudo": "Aqui está o artigo completo sobre os benefícios do açaí.\\n[Clique aqui para ler o artigo]",
      "bloco_anterior": 12,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 51,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 1,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 21,
      "tipo": "list_button",
      "conteudo": "Aqui está o vídeo sobre os benefícios do açaí.\\n[Clique aqui para assistir ao vídeo]",
      "bloco_anterior": 12,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 52,
          "texto_resposta": "Voltar ao menu principal",
          "ordem": 1,
          "prox_bloco": 2,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 22,
      "tipo": "list_button",
      "conteudo": "Acompanhamentos selecionados com sucesso!\\nSeu açaí está sendo preparado.\\nGostaria de adicionar extras antes de finalizar?",
      "bloco_anterior": 13,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 53,
          "texto_resposta": "Sim, adicionar extras",
          "ordem": 1,
          "prox_bloco": 16,
          "tipo": "Resposta"
        },
        {
          "id": 54,
          "texto_resposta": "Não, finalizar pedido",
          "ordem": 2,
          "prox_bloco": 18,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 23,
      "tipo": "list_button",
      "conteudo": "Extras adicionados com sucesso!\\nSeu açaí será finalizado com os seguintes extras: \\n- Morango Fresco\\n- Creme de Avelã\\n\\nDeseja finalizar o pedido agora?",
      "bloco_anterior": 17,
      "proximo_bloco": null,
      "respostas": [
        {
          "id": 55,
          "texto_resposta": "Finalizar pedido",
          "ordem": 1,
          "prox_bloco": 18,
          "tipo": "Resposta"
        },
        {
          "id": 56,
          "texto_resposta": "Adicionar mais extras",
          "ordem": 2,
          "prox_bloco": 16,
          "tipo": "Resposta"
        }
      ]
    },
    {
      "id": 24,
      "tipo": "list_button",
      "conteudo": "Obrigado por escolher o Point do Açaí!\\nEsperamos que tenha uma excelente experiência com o nosso açaí.\\nSe precisar de mais alguma coisa, estamos aqui para ajudar!",
      "bloco_anterior": 18,
      "proximo_bloco": null,
      "respostas": []
    }
  ]
}
"""

data = json.loads(ACAITERIA)
bot = Bot(wpp_api_token=wpp_token, phone_number_id=phone_id)
atendimento = AtendimentoDTO(data)


class ButtonFactory:
    @staticmethod
    def create_button(button_id, title):
        return {
            "type": "reply",
            "reply": {
                "id": button_id,
                "title": title
            }
        }

    @staticmethod
    def create_list_option(option_id, title, description=None):
        option = {
            "id": option_id,
            "title": title,
        }
        if description:
            option["description"] = description

        return option


buttons = []


# Função para salvar o atendimento_step em um arquivo JSON
def save_atendimento_step(blocoID, status, filename='atendimento_step.json'):
    with open(filename, 'w') as file:
        json.dump({'idBlocoAtual': blocoID, 'aguardando_resposta': status}, file)


# Função para carregar o atendimento_step de um arquivo JSON
def load_atendimento_step(filename='atendimento_step.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return data.get('idBlocoAtual', atendimento.atendimento_blocos[
                0].id)  # Retorna 1 se o arquivo estiver vazio ou não tiver o campo
    else:
        return atendimento.atendimento_blocos[0].id  # Valor padrão se o arquivo não existir


def load_atendimento_status(filename='atendimento_step.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return data.get('aguardando_resposta', False)  # Retorna 1 se o arquivo estiver vazio ou não tiver o campo
    else:
        return False  # Valor padrão se o arquivo não existir


save_atendimento_step(0, False)


@celery.task
def process_message(message):
    wpp_message = WhatsappMessage(message)

    if wpp_message.message_body or wpp_message.interactive_type:
        print(f"Mensagem do usuário: {wpp_message.message_body}")
        print(f"Opção escolhida: {wpp_message.list_reply_id}")
        print(f"message_type: {wpp_message.interactive_type}")
        i = load_atendimento_step()
        if i == 0:
            bloco_atual = atendimento.get_first_bloco()
            bot.send_message(to=bot.format_phone_number(wpp_message.message_from), message=bloco_atual.conteudo)
            bloco_atual = bloco_atual.proximo_bloco
            bloco_atual = atendimento.get_bloco_by_id(bloco_atual)
            opcoes = []
            ids_usados = set()  # Usado para garantir que os IDs são únicos
            if bloco_atual.respostas:
                for resposta in bloco_atual.respostas:
                    prox_bloco_id = resposta.prox_bloco
                    if prox_bloco_id in ids_usados:
                        prox_bloco_id = f"{prox_bloco_id}_{len(ids_usados)}"  # Gera um ID único
                    ids_usados.add(prox_bloco_id)

                    if bloco_atual.tipo == "opcoes":
                        opcoes.append(ButtonFactory.create_button(prox_bloco_id, resposta.texto_resposta))
                    elif bloco_atual.tipo == "list_button":
                        opcoes.append(ButtonFactory.create_list_option(prox_bloco_id, resposta.texto_resposta))

                save_atendimento_step(bloco_atual.id, True)
            else:
                save_atendimento_step(bloco_atual.id, False)

            bot.send_message(to=bot.format_phone_number(wpp_message.message_from),
                             message=f"{bloco_atual.conteudo}",
                             buttons=opcoes if bloco_atual.tipo == "opcoes" else None,
                             list_menu=opcoes if bloco_atual.tipo == "list_button" else None)
        else:
            prox_bloco_id = None
            if wpp_message.interactive_type == "button_reply":
                prox_bloco_id = wpp_message.button_reply_id
            elif wpp_message.interactive_type == "list_reply":
                prox_bloco_id = wpp_message.list_reply_id.split('_')[0]
            else:
                prox_bloco_id = atendimento.get_first_bloco().proximo_bloco

            print(f"prox_bloco_id {prox_bloco_id}")
            bloco_atual = atendimento.get_bloco_by_id(prox_bloco_id)
            opcoes = []
            ids_usados = set()  # Usado para garantir que os IDs são únicos
            if bloco_atual.respostas:
                for resposta in bloco_atual.respostas:
                    prox_bloco_id = resposta.prox_bloco
                    if prox_bloco_id in ids_usados:
                        prox_bloco_id = f"{prox_bloco_id}_{len(ids_usados)}"  # Gera um ID único
                    ids_usados.add(prox_bloco_id)

                    if bloco_atual.tipo == "opcoes":
                        opcoes.append(ButtonFactory.create_button(prox_bloco_id, resposta.texto_resposta))
                    elif bloco_atual.tipo == "list_button":
                        opcoes.append(ButtonFactory.create_list_option(prox_bloco_id, resposta.texto_resposta))

            bot.send_message(to=bot.format_phone_number(wpp_message.message_from),
                             message=f"{bloco_atual.conteudo}",
                             buttons=opcoes if bloco_atual.tipo == "opcoes" else None,
                             list_menu=opcoes if bloco_atual.tipo == "list_button" else None)

    return "finalizado"
