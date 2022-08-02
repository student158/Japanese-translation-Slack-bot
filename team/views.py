from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import urllib.parse
import json
from .helper_functions.event_manager import EventManager
from asgiref.sync import sync_to_async
from dotenv import load_dotenv
import os

load_dotenv()
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
VERIFICATION_TOKEN = os.getenv("VERIFICATION_TOKEN")
ACTION_HOW_ARE_YOU = os.getenv("ACTION_HOW_ARE_YOU")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

event_manager = EventManager()

##################################
##################################

def index(request):
    return render(request, "index.html")

@csrf_exempt
@sync_to_async
def slack_url_auth(request):
    if request.method == "POST":
        print("RECEIVED POST REQUEST")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        if "challenge" in body:
            response = {"challenge": body["challenge"]}
            return JsonResponse(response)
        elif ("bot_id" in body["event"]):
            print("bot msg")
            return HttpResponse()
        else:
            event_manager.handle_auto_translate(body)
            return HttpResponse()
    else:
        print("RECEIVED GET METHOD")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        return HttpResponse()


@csrf_exempt
def user_interact_button(request):
    print("RECEIVED POST REQUEST")
    # print(request.body)
    body_unicode = request.body.decode('utf-8')
    # print("body unicode: ", body_unicode)
    # print(body_unicode[8:])
    decoded_body = urllib.parse.unquote(body_unicode[8:])
    # print(decoded_body)
    body_dict = json.loads(decoded_body)
    # print(body_dict)

    if "type" in body_dict:
        action_type = body_dict["type"]
        if action_type == "shortcut":
            pass
        if action_type == "message_action":
            event_manager.handle_click_translate(body_dict)
        if action_type == "block_actions":
            print(body_dict)
            btn_click_action = body_dict["actions"][0]["value"]
            if btn_click_action == "translation_on":
                event_manager.handle_click_turn_on_auto_trans(body_dict)
                print("Click me button clicked")
            else:
                event_manager.handle_click_turn_off_auto_trans(body_dict)
            print("\n\n")
        if action_type == "view_submission":
            # print(body_dict)
            print("\n\n")
        return HttpResponse()
    else:
        return HttpResponse()
