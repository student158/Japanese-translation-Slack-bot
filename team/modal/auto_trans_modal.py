auto_translate_modal = {
	"type": "modal",
	"title": {
		"type": "plain_text",
		"text": "Auto translation",
		"emoji": True
	},
	"close": {
		"type": "plain_text",
		"text": "Cancel",
		"emoji": True
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit",
		"emoji": True
	},
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Choose language for auto translate"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "日本語",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "English",
							"emoji": True
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "*this is plain_text text*",
							"emoji": True
						},
						"value": "value-2"
					}
				],
				"action_id": "static_select-action"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "radio_buttons",
					"options": [
						{
							"text": {
								"type": "plain_text",
								"text": "Turn on",
								"emoji": True
							},
							"value": "value-0"
						},
						{
							"text": {
								"type": "plain_text",
								"text": "Off",
								"emoji": True
							},
							"value": "value-1"
						}
					],
					"action_id": "actionId-0"
				}
			]
		}
	]
}