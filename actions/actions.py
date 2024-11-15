from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class ActionHitungBhp(Action):
    def hitung_bhp(self) -> Text:
        return "hitung_bhp"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        frequency = tracker.get_latest_entity_values("frequency")

        # You can do any computations or processing here
        # and store the result in a variable

        result = f"Frequency: {frequency}"

        dispatcher.utter_message(text=result)
        print(frequency)

        return []
