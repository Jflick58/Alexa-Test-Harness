import requests
import json
import pytest



def load_session_conf(path_to_json_file):
    with open(path_to_json_file, "r") as conf_json:
        conf = json.load(conf_json)
        return conf.values



def test_harness(intent, expected_response, session_context):
    endpoint, userid, locale, applicationId = load_session_conf("alexa-test-harness/conf.json")
    headers = {
        'Content-Type': 'application/json',
    }
    request = {
      "session": {
        "new": True,
        "sessionId": "SessionId.2604160e-34c2-4d27-961e-10e20c7a70c9",
        "application": {
          "applicationId": applicationId
        },
        "attributes": session_context,
        "user": {
          "userId": userid
        }
      },
      "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.e6576f06-34d0-4148-9c47-b08356b8a2ee",
        "intent": {
          "name": intent,
          "slots": {}
        },
        "locale": locale,
        "timestamp": "2018-03-22T04:49:07Z"
      },
      "context": {
        "AudioPlayer": {
          "playerActivity": "IDLE"
        },
        "System": {
          "application": {
            "applicationId": applicationId
          },
          "user": {
            "userId": userid
          },
          "device": {
            "supportedInterfaces": {}
          }
        }
      },
      "version": "1.0"
    }

    endpoint_call = requests.post(endpoint,headers=headers, data=json.dumps(request))

    assert ((endpoint_call['response'])['outputSpeech'])['text'] == expected_response


