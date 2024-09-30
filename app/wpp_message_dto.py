class WhatsappMessage:
    def __init__(self, data):
        self.object = data.get('object', None)
        self.entry_id = None
        self.messaging_product = None
        self.display_phone_number = None
        self.phone_number_id = None
        self.contact_name = None
        self.wa_id = None
        self.message_from = None
        self.message_id = None
        self.timestamp = None
        self.message_body = None
        self.message_type = None
        self.interactive_type = None
        self.button_reply_id = None
        self.button_reply_title = None
        self.list_reply_id = None
        self.list_reply_title = None

        if 'entry' in data and isinstance(data['entry'], list) and len(data['entry']) > 0:
            entry = data['entry'][0]
            self.entry_id = entry.get('id', None)

            if 'changes' in entry and isinstance(entry['changes'], list) and len(entry['changes']) > 0:
                changes = entry['changes'][0]
                value = changes.get('value', {})

                self.messaging_product = value.get('messaging_product', None)

                metadata = value.get('metadata', {})
                self.display_phone_number = metadata.get('display_phone_number', None)
                self.phone_number_id = metadata.get('phone_number_id', None)

                contacts = value.get('contacts', [])
                if len(contacts) > 0:
                    self.contact_name = contacts[0].get('profile', {}).get('name', None)
                    self.wa_id = contacts[0].get('wa_id', None)

                messages = value.get('messages', [])
                if len(messages) > 0:
                    message = messages[0]
                    self.message_from = message.get('from', None)
                    self.message_id = message.get('id', None)
                    self.timestamp = message.get('timestamp', None)
                    self.message_type = message.get('type', None)

                    if self.message_type == 'interactive':
                        self.interactive_type = message.get('interactive', {}).get('type', None)

                        if self.interactive_type == 'button_reply':
                            button_reply = message.get('interactive', {}).get('button_reply', {})
                            self.button_reply_id = button_reply.get('id', None)
                            self.button_reply_title = button_reply.get('title', None)

                        elif self.interactive_type == 'list_reply':
                            list_reply = message.get('interactive', {}).get('list_reply', {})
                            self.list_reply_id = list_reply.get('id', None)
                            self.list_reply_title = list_reply.get('title', None)

                    else:
                        self.message_body = message.get('text', {}).get('body', None)
