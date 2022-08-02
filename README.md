# Japanese translation Slack bot

This Slack bot can automatically and manually translate message in chat between Japanese and English. This bot intends to help international students in Computer science department of Toyo University (INIAD) to translate conveniently messages in Japanese.  

## How does the bot work?
- After the bot is added to the Slack workspace, when we click at "More actions" in each message, we have quick options like this:
<p align="center"><img src="./images/more-actions.png" height=50% width=50%></p>
<p align="center"><img src="./images/option-lists.png" height=50% width=50%></p>
- There are 3 options:
    - Manually translate from Japanese to English
    - Manually translate from English to Japanese
    - Automatically translate from Japanese to English

### Manual translation
- When using manual translation, the bot will create translation ephermeral message (which only that person can see, other people cannot) and a translation pop-up modal.

<p align="center"><img src="./images/translation-modal.png" height=50% width=50% > </>

<p align="center"><img src="./images/ephermeral_img.png" height=50% width=50% > </>

### Automatical translation
- When click automatic translation option, the bot will show if auto translation is enabled in this channel or not.

    - If it is not enabled, the turn on button will be shown. After turn on, confirmation message will appear.
    <p align="center"><img src="./images/turn-on-auto.png" height=50% width=50% > </>
    <p align="center"><img src="./images/confirm-on.png" height=50% width=50% > </>
    
    - If it is enabled, the turn off button will be shown. After turn off, confirmation message will appear.
    <p align="center"><img src="./images/turn-off-auto.png" height=50% width=50% > </>
    <p align="center"><img src="./images/confirm-off.png" height=50% width=50% > </>

- When automatic translation is on, if any Japanese message is sent, the bot will auto translate that message.
<p align="center"><img src="./images/auto-trans.png" height=50% width=50% > </>
