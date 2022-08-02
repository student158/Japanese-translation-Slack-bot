import json
import requests

def post_translation_modal_en_to_jp(trigger_id, access_token, translate_msg):
    '''Pop up a modal with translation text'''
    url = "https://slack.com/api/views.open"
    headers = {
        "Content-type": "application/json",
        "Authorization": "Bearer " + access_token
    }
    content = {
        "trigger_id": trigger_id,
        "view": {
            "title": {
                "type": "plain_text",
                "text": "翻訳"
            },
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": translate_msg,
                        "emoji": True
                    }
                }
            ],
            "type": "modal"
        }
    }
    content_json = json.dumps(content)
    res = requests.post(url, headers=headers, data=content_json)

def post_translation_modal_jp_to_en(trigger_id, access_token, translate_msg):
    '''Pop up a modal with translation text from japanese -> english'''
    url = "https://slack.com/api/views.open"
    headers = {
        "Content-type": "application/json",
        "Authorization": "Bearer " + access_token
    }
    content = {
        "trigger_id": trigger_id,
        "view": {
            "title": {
                "type": "plain_text",
                "text": "Translation"
            },
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": translate_msg,
                        "emoji": True
                    }
                }
            ],
            "type": "modal"
        }
    }
    content_json = json.dumps(content)
    res = requests.post(url, headers=headers, data=content_json)

def post_warning_model_bot_not_in_channel(trigger_id, access_token):
    url = "https://slack.com/api/views.open"
    headers = {
        "Content-type": "application/json",
        "Authorization": "Bearer " + access_token
    }
    content = {
        "trigger_id": trigger_id,
        "view": {
            "title": {
                "type": "plain_text",
                "text": "Translation"
            },
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": "The bot not in the workplace",
                        "emoji": True
                    }
                }
            ],
            "type": "modal"
        }
    }
    content_json = json.dumps(content)
    res = requests.post(url, headers=headers, data=content_json)

def post_msg_to_channel(channel_id, access_token, msg):
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        'Content-type': 'application/json',
        "Authorization": "Bearer " + access_token
        }
    data = {"text": msg, "channel": channel_id}
    data_json = json.dumps(data)
    res = requests.post(url, data=data_json, headers=headers)
    # print(res.content)




