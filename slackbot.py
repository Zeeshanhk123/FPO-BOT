import os
from pathlib import Path
from dotenv import load_dotenv
from slack_sdk import WebClient
# <<<<<<< HEAD
from flask import Flask, request, Response
# =======
from flask import Flask, request,Response
# >>>>>>> 97a2b4c7444760b21f1f890e28270f405be3f293
from slackeventsapi import SlackEventAdapter

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)

client = WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call('auth.test')["user_id"]

@slack_event_adapter.on('message')
def message(payload):
    # try:
        event = payload.get('event', {})
        user_id = event.get('user')
        channel_id = event.get('channel')
        text = event.get('text')

# <<<<<<< HEAD
        # if BOT_ID != user_id:
        #     client.chat_postMessage(channel=channel_id, text=text)
    # except Exception as e:
        # print(f"Error handling message event: {e}")

@app.route("/message-count", methods=['POST'])

    #     if BOT_ID != user_id:
    #         client.chat_postMessage(channel=channel_id, text=text)
    # except Exception as e:
    #     print(f"Error handling message event: {e}")

@app.route("/po-number", methods=['POST'])
# >>>>>>> 97a2b4c7444760b21f1f890e28270f405be3f293
def message_count():
    try:
        data = request.form
        user_id = data.get("user_id")
        channel_id = data.get("channel_id")
        
        alphanumeric_code = generate_code()  # Keep the generated code in alphanumeric_code
        if BOT_ID != user_id:
# <<<<<<< HEAD
            client.chat_postMessage(channel=channel_id, text=f"FPO0000:{alphanumeric_code}")
# =======
            client.chat_postMessage(channel=channel_id, text=f"FPO-0{alphanumeric_code}")

# >>>>>>> 97a2b4c7444760b21f1f890e28270f405be3f293

        return Response(), 200
    except Exception as e:
        print(f"Error handling message count request: {e}")
        return Response(status=500)

# All About the FPO num functionality

txt_path = "text/file.txt"

# <<<<<<< HEAD
# send to txt file
# =======
# send to txt file
# >>>>>>> 97a2b4c7444760b21f1f890e28270f405be3f293
def post_to_text(alphanumeric_code):
    with open(txt_path , 'w') as file:
        file.write(f'{alphanumeric_code}\n')  # Use alphanumeric_code instead of current_number

# read from the text file
# <<<<<<< HEAD
# read from the text file
# =======
# >>>>>>> 97a2b4c7444760b21f1f890e28270f405be3f293
def read_counter():
    try:
        with open(txt_path, 'r') as file:
            content = file.read().strip()
            return int(content) if content else 0
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0
    except Exception as e:
        print(f"Error reading from text file: {e}")
        return 0


# increment from the previous one by reading from the text file
# <<<<<<< HEAD
# increment from the previous one by reading from the text file
# =======
# >>>>>>> 97a2b4c7444760b21f1f890e28270f405be3f293
def generate_code():
    try:
        current_number = read_counter()
        current_number += 1
        post_to_text(current_number)
        return current_number
    except Exception as e:
        print(f"Error generating code: {e}")
        return 0


# if __name__ == '__main__':
# <<<<<<< HEAD
#     app.run(debug=True)

# =======
#    app.run(debug=True)
# >>>>>>> 97a2b4c7444760b21f1f890e28270f405be3f293
