from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.types import DomainDict
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="chatbotdb"
)

mycursor = mydb.cursor()

class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_membership_form"

    def validate_nama(self,slot_value: Any,dispatcher: CollectingDispatcher,tracker: Tracker,domain: DomainDict,) -> Dict[Text, Any]:
        print(slot_value)
        if len(slot_value) < 3:
            dispatcher.utter_message(text="Apa benar ini nama mu? Coba di cek kembali.")
            return {"nama": None}
        return {"nama": slot_value}

    def validate_no_telp(self,slot_value: Any,dispatcher: CollectingDispatcher,tracker: Tracker,domain: DomainDict,) -> Dict[Text, Any]:
        print(slot_value)
        if len(slot_value) < 3:
            dispatcher.utter_message(text="No telp yang anda isi terlalu pendek. Coba di cek kembali.")
            return {"no_telp": None}
        return {"no_telp": slot_value}
    
    def validate_email(self,slot_value: Any,dispatcher: CollectingDispatcher,tracker: Tracker,domain: DomainDict,) -> Dict[Text, Any]:
        print(slot_value)
        if len(slot_value) < 3:
            dispatcher.utter_message(text="Email yang anda isi terlalu pendek. Coba di cek kembali.")
            return {"email": None}
        return {"email": slot_value}
    
    def validate_alamat(self,slot_value: Any,dispatcher: CollectingDispatcher,tracker: Tracker,domain: DomainDict,) -> Dict[Text, Any]:
        print(slot_value)
        if len(slot_value) < 3:
            dispatcher.utter_message(text="Alamat yang anda isi terlalu pendek. Coba di cek kembali.")
            return {"alamat": None}
        return {"alamat": slot_value}

class SubmitToDB(Action):

    def name(self) -> Text:
        return "action_submit_to_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response = "utter_selesai_membership")
        full_name = tracker.get_slot('nama')
        phone_number = str(tracker.get_slot('no_telp'))
        email = tracker.get_slot('email')
        alamat = tracker.get_slot('alamat')
        sql = "Insert into customers VALUES (%s, %s, %s, %s, %s)"
        val = (0, full_name, phone_number, email, alamat)
        print(val)
        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        return [AllSlotsReset()]
