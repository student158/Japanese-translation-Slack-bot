msg_turn_on_auto_trans = {
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "現在、自動翻訳がOFFになっています\nAuto translation is currently turned OFF"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Turn on",
					"emoji": True
				},
				"value": "translation_on",
				"action_id": "button-action"
			}
		}
	]
}

msg_turn_off_auto_trans = {
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "現在、自動翻訳がONになっています\nAuto translation is currently turned ON"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Turn off",
					"emoji": True
				},
				"value": "translation_off",
				"action_id": "button-action"
			}
		}
	]
}

msg_test = {
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Auto-translation for this channel is currently OFF"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Turn on",
					"emoji": True
				},
				"value": "translation_on",
				"action_id": "button-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "This is a section block with a button."
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Click Me",
					"emoji": True
				},
				"value": "click_me_123",
				"action_id": "button-action"
			}
		}
	]
}









