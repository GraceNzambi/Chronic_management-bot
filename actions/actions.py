# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionInformDisease(Action):
    def name(self) -> Text:
        return "action_inform_condition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the disease entity
        disease = tracker.latest_message['entities'][0]['value']

        if disease.lower() == 'hypertension':
            # Inform about hypertension
            dispatcher.utter_message("Hypertension is a chronic medical condition where the blood pressure in the arteries is elevated. It's also known as high blood pressure.")
            dispatcher.utter_message("It's important to manage hypertension with medication and lifestyle changes such as reducing salt intake, increasing physical activity, and maintaining a healthy weight.")

        elif disease.lower() == 'diabetes':
            # Inform about diabetes
            dispatcher.utter_message("Diabetes is a chronic medical condition where the body is unable to regulate blood sugar levels. There are two main types of diabetes: type 1 and type 2.")
            dispatcher.utter_message("It's important to manage diabetes with medication, a healthy diet, regular exercise, and monitoring blood sugar levels.")

        else:
            # Inform about unknown disease
            dispatcher.utter_message("I'm sorry, I don't have information about that disease. Please specify hypertension or diabetes.")

        return []


