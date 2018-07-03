import requests
import json
import pytest

class Alexa_Test(object):

    def __init__(self,endpoint, userid, applicationId, apitoken, locale="en-US", path_to_intent_json="src/sample.json"):
      
      self.endpoint = endpoint
      self.userid = userid
      self.locale = locale
      self.applicationId = applicationId
      self.apitoken = str(apitoken)
      self.path_to_intent_json = path_to_intent_json

    def test_intent_response(self,intent, expected_response, session_context=""):

      headers = {
          'Content-Type': 'application/json',
      }
      request = {
        "session": {
          "new": True,
          "sessionId": "SessionId.2604160e-34c2-4d27-961e-10e20c7a70c9",
          "application": {
            "applicationId": self.applicationId
          },
          "attributes": session_context,
          "user": {
            "userId": self.userid
          }
        },
        "request": {
          "type": "IntentRequest",
          "requestId": "EdwRequestId.e6576f06-34d0-4148-9c47-b08356b8a2ee",
          "intent": {
            "name": intent,
            "slots": {}
          },
          "locale": self.locale,
          "timestamp": "2018-03-22T04:49:07Z"
        },
        "context": {
          "AudioPlayer": {
            "playerActivity": "IDLE"
          },
          "System": {
            "application": {
              "applicationId": self.applicationId
            },
            "user": {
              "userId": self.userid
            },
            "device": {
              "supportedInterfaces": {}
            }
          }
        },
        "version": "1.0"
      }

      endpoint_call = requests.post(endpoint,headers=headers, data=json.dumps(request))

      print(endpoint_call.text)

      response = str(((endpoint_call['response'])['outputSpeech'])['text'])
      assert expected_response in response
    
    def parse_intents(self):
      voice_json = self.path_to_intent_json
      intents = []
      interaction_model = voice_json['interactionModel']
      language_model = interaction_model['LanguageModel']
      intent_dicts = language_model['intents']
      for intent in intent_dicts:
        intent_name = intent["name"]
        intents.append(intent_name)
      return intents
      
    def test_utterance_intent_match(self, utterance, expected_intent):

      request = {
        "input": {
          "content": utterance
        },
        "device": {
          "locale": self.locale
        }
      }

      url = "https://api.amazonalexa.com/v1/skills/{}/simulations".format(self.applicationId)
      headers = {
        "Authorization": self.apitoken
        "Content-Type": "application/json"
        "Accept": "application/json"
      }

      endpoint_call = requests.post(url,headers=headers, data=json.dumps(request))

      if endpoint_call.code == "200": 
        # id = endpoint_call.json["id"]
        # results_url = url.replace("/simulations", "/simulations/{}".format(id))
        # enpoint_results = requests.get(results_url,headers=headers)
        result = endpoint_call.json["result"]
        skill_execution = result["skillExecutionInfo"]
        invocation_request = skill_execution["invocationRequest"]
        request = invocation_request["request"]
        intent_dict = request["intent"]
        returned_intent = intent_dict["name"]
        assert returned_intent == expected_intent
      
      else: 
        return("error") #add logging and proper handling later










    


