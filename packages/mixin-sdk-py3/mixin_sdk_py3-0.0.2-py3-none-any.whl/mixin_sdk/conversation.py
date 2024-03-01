from mixin_sdk.request import request


def get_conversation_info(conversation_id, access_token, bot_id):
    uri = '/conversations/' + conversation_id
    custom_headers = {"Authorization": "Bearer " + access_token}
    conversation_info = request(uri=uri, custom_headers=custom_headers)['data']
    if conversation_info:
        category = conversation_info['category']
        participants = {'conversation_id': conversation_id, 'category': category}
        members = []
        if category == 'GROUP':
            for participant in conversation_info['participants']:
                members.append(participant['user_id'])
                if participant['role'] == 'OWNER':
                    participants['owner'] = participant['user_id']
                elif participant['role'] == 'ADMIN':
                    participants['admin'] = participant['user_id']
            participants['members'] = members
        elif category == 'CONTACT':
            for participant in conversation_info['participants']:
                members.append(participant['user_id']) 
                if participant['user_id'] != bot_id:
                    participants['owner'] = participant['user_id']
            participants['members'] = members 
        return participants

