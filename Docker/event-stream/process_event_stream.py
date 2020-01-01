# event-stream/agent.py
#faust -A process_event_stream worker -l info
import json
from datetime import datetime

from typing import List
import faust

app = faust.App(
        'stream-event-app',
        broker='kafka://kafka-server',
        value_serializer='raw')

class Transaction(faust.Record):
    merchant: str
    time : datetime

class Account(faust.Record):
    account_status: bool
    available_limit : int
    transaction:List[Transaction]


account = Account(False, 0, [])

# define the source topic to read the “transaction” events from
# every value in this topic is of the Transaction type
transaction_topic = app.topic('transaction', value_type=bytes)

authorize_log={"account": {"active-card": "", "available-limit": 0}, "violations": []}

#Error Strings
acc_not_initialized="account-not-initialized"
acc_already_initialized="account-already-initialized"
acc_not_activated="account-not-activated"
acc_insufficient="insufficient-limit"
# agent: process infinite stream of orders.
@app.agent(transaction_topic)
async def order(transactions):
    async for transaction in transactions:
        print(transaction)
        event = json.loads(transaction)
        #print(type(event))
        try:
            account_event = event["account"]
            #print(account_event)
            if (account_event):
                card_status = account_event["active-card"]
                avail_limit = account_event["available-limit"]

                # Once created, the account should not be updated or recreated
                if (account.account_status ):
                    authorize_log['violations']=[]
                    authorize_log['violations'].append(acc_already_initialized)
                elif not card_status: # account status not set and new event with "active-card": false
                    authorize_log["account"]["active-card"] = account.account_status
                    authorize_log['violations']=[]

                    # First event should be account activation, else violation
                    authorize_log['violations'].append(acc_not_activated)
                else:
                    account.account_status = True
                    account.availble_limit = avail_limit

                    authorize_log["account"]["active-card"] = card_status
                    authorize_log["account"]["available-limit"] = avail_limit
                    authorize_log['violations']=[]

                print(json.dumps(authorize_log))
        except KeyError:
            try:
                transaction_event = event["transaction"]
                if(transaction_event):

                   if account.account_status:
                        amount = transaction_event["amount"]
                        if(amount > account.available_limit):
                            authorize_log["violations"] = []

                            # There is a violation if requested amount is more than available balance
                            authorize_log['violations'].append(acc_insufficient)
                        else:
                            account.available_limit = account.available_limit - amount
                            authorize_log["account"]["available-limit"] = account.available_limit
                   else:
                        authorize_log["account"]["active-card"] = account.account_status
                        authorize_log['violations'] = []

                        # No transaction is allowed unless account is active
                        authorize_log['violations'].append(acc_not_initialized)

                print(json.dumps(authorize_log))
            except KeyError:
                print("Invalid event: event must be account/transaction related")

def main():
    print("main: stream-event-app")
    app.main()

if __name__ == '__main__':
    main()



