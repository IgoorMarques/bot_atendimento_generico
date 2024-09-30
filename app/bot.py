import json

import requests


class Bot:
    def __init__(self, wpp_api_token, phone_number_id):
        self.phone_number_id = phone_number_id
        self.wpp_api_token = wpp_api_token

    def send_message(self, to, message, buttons=None, list_menu=None):
        url = f"https://graph.facebook.com/v12.0/{self.phone_number_id}/messages"
        headers = {
            "Authorization": f"Bearer {self.wpp_api_token}",
            "Content-Type": "application/json"
        }

        print(f"message: {message}")

        if buttons:
            data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": to,
                "type": "interactive",
                "interactive": {
                    "type": "button",
                    "body": {
                        "text": message
                    },
                    "action": {
                        "buttons": buttons
                    }
                }
            }
        elif list_menu:
            data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": to,
                "type": "interactive",
                "interactive": {
                    "type": "list",
                    "body": {
                        "text": message
                    },

                    "action": {
                        "button": "Ver opções",
                        "sections": [
                            {
                                "title": "Opções",
                                "rows": list_menu
                            }
                        ]
                    }
                }
            }
        else:
            data = {
                "messaging_product": "whatsapp",
                "to": to,
                "text": {
                    "body": message
                }
            }

        response = requests.post(url, json=data, headers=headers)
        print(response.json())
        return response.json()

    def validar_cpf(self, cpf):
        # Verifica se o CPF tem 11 dígitos e se todos são números
        if not cpf.isdigit() or len(cpf) != 11:
            return False

        # Calcula o primeiro dígito verificador
        def calcular_digito(cpf, fator):
            soma = 0
            for i in range(fator - 1):
                soma += int(cpf[i]) * (fator - i)
            resto = soma % 11
            return 0 if resto < 2 else 11 - resto

        # Calcula os dois dígitos verificadores
        primeiro_digito = calcular_digito(cpf, 10)
        segundo_digito = calcular_digito(cpf, 11)

        # Verifica se os dígitos verificadores são válidos
        return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"

    def format_phone_number(self, phone_number):
        if len(phone_number) > 13:
            raise ValueError("Número de telefone deve ter 12 dígitos.")

        country_code = phone_number[:2]
        area_code = phone_number[2:4]
        part1 = phone_number[4:8]
        part2 = phone_number[8:]
        part1 = '9' + part1
        formatted_number = f"+{country_code} ({area_code}) {part1}-{part2}"
        return formatted_number
