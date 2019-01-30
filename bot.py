import requests  
from bottle import (  
    run, post, response, request as bottle_request
)

BOT_URL = 'https://api.telegram.org/bot653183379:AAHp9CSLcw6jwDJNoZxZ1Wx-MT-62Rx-aHk/'

def get_chat_id(data):
    """
    Get chat ID from telegram JSON
    """
	
    return data['message']['chat']['id']

def get_message(data):
    """
    Get message fom JSON
    """

    return data['message']['text']

def send_message(prepared_data):  
    """
    Prepared data should be json which includes at least `chat_id` and `text`
    """ 
    message_url = BOT_URL + 'sendMessage'
    requests.post(message_url, json=prepared_data)

def change_text_message(text):  
    """
    To turn our message backwards.
    """
    return text[::-1]

def prepare_data_for_answer(data):  
    answer = change_text_message(get_message(data))

    json_data = {
        "chat_id": get_chat_id(data),
        "text": answer,
    }

    return json_data

@post('/')
def main():  
    data = bottle_request.json

    answer_data = prepare_data_for_answer(data)
    send_message(answer_data)  # <--- function for sending answer

    return response  # status 200 OK by default

if __name__ == '__main__':
	run(host='localhost', port=8080, debug=True)
