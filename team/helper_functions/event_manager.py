from slack_sdk import WebClient
import translators as ts
from langdetect import detect
from ..slack_msg_template.msg_template import msg_turn_on_auto_trans, msg_test, msg_turn_off_auto_trans
from .post_msg import post_translation_modal_en_to_jp, post_warning_model_bot_not_in_channel, post_msg_to_channel
from ..models import ChannelTranslation
from dotenv import load_dotenv
import os

load_dotenv()
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
VERIFICATION_TOKEN = os.getenv("VERIFICATION_TOKEN")
ACTION_HOW_ARE_YOU = os.getenv("ACTION_HOW_ARE_YOU")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

client = WebClient(token=ACCESS_TOKEN)

class EventManager:
    def __init__(self) -> None:
        pass

    def handle_click_translate(self, request):
        channel_id = request["channel"]["id"]
        print("channel id: ", channel_id)
        user_wants_translate_id = request["user"]["id"]
        print("user wants translate id: ", user_wants_translate_id)
        token = request["token"]
        print("token: ", token)
        msg_to_translate = request["message"]["text"].replace("+", " ")
        print(msg_to_translate)
        translate_option = request["callback_id"]
        trigger_id = request["trigger_id"]
        if translate_option == "auto_translate":
            channel_auto_trans_on = len(ChannelTranslation.objects.filter(channel_id=channel_id))
            if (channel_auto_trans_on):
                client.chat_postMessage(
                    channel=channel_id,
                    text="Hello",
                    blocks=msg_turn_off_auto_trans["blocks"]
                )
            else:
                client.chat_postMessage(
                    channel=channel_id,
                    text="Hello",
                    blocks=msg_turn_on_auto_trans["blocks"]
                )
            # try:
            #     result = client.chat_postMessage(
            #         channel=channel_id,
            #         text="Hello",
            #         blocks=msg_test["blocks"]
            #     )
            #     print(result)
            # except Exception as e:
            #     print(f"Error: {e}")
        else:
            if translate_option == "trans_jp_to_en":
                translate_msg = ts.google(msg_to_translate, to_language='en')
            else:
                translate_msg = ts.google(msg_to_translate, to_language='ja')

            try:
                client.chat_postEphemeral(channel=channel_id, text=translate_msg, user=user_wants_translate_id)
            except Exception as e:
                # raise Exception()
                post_warning_model_bot_not_in_channel(trigger_id, ACCESS_TOKEN)
                # return HttpResponse()
            #######
            ##Try to show modal
            post_translation_modal_en_to_jp(trigger_id, ACCESS_TOKEN, translate_msg)

    def handle_click_turn_on_auto_trans(self, request):
        channel_id = request["channel"]["id"]
        print("channel id: ", channel_id)
        channel_already_auto_trans = len(ChannelTranslation.objects.filter(channel_id=channel_id))
        if (channel_already_auto_trans):
            client.chat_postMessage(
                    channel=channel_id,
                    text="現在、自動翻訳がONになっています\nAuto translation is currently turned ON"
                )
        else:
            new_record = ChannelTranslation(channel_id=channel_id)
            new_record.save()
            client.chat_postMessage(
                    channel=channel_id,
                    text="自動翻訳をONにする\nActivate auto translation"
                )

    def handle_click_turn_off_auto_trans(self, request):
        channel_id = request["channel"]["id"]
        print("channel id: ", channel_id)
        channel_already_auto_trans = len(ChannelTranslation.objects.filter(channel_id=channel_id))
        if (channel_already_auto_trans):
            current_channel = ChannelTranslation.objects.filter(channel_id=channel_id)
            current_channel.delete()
            client.chat_postMessage(
                    channel=channel_id,
                    text="自動翻訳をOFFにする\nDeactivate Auto Translation"
                )
        else:
            client.chat_postMessage(
                    channel=channel_id,
                    text="現在、自動翻訳がOFFになっています\nAuto translation is currently turned OFF"
                )

    def handle_auto_translate(self, request):
        msg_from_bot = False
        channel_id = request["event"]["channel"]
        print(channel_id)
        msg = request["event"]["text"]
        print(msg)
        if ("bot_id" in request["event"]):
            msg_from_bot = True
            return
        channel_turn_auto_trans_on = len(ChannelTranslation.objects.filter(channel_id=channel_id))
        if ((channel_turn_auto_trans_on == 1) and (not msg_from_bot)):
            detected_lang = detect(msg)
            print("Auto translation, detect lang:", detected_lang)
            input_lang = ['ja', 'ko', 'zh-cn', 'zh-tw']
            if (detected_lang in input_lang):
                translate_text = ts.google(msg, to_language='en')
            else:
                translate_text = ts.google(msg, to_language='ja')
            post_msg_to_channel(channel_id, ACCESS_TOKEN, translate_text)
            
