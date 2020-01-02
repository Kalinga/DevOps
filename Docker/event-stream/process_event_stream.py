# event-stream/agent.py
#faust -A process_event_stream worker -l info

import json
from datetime import datetime

from typing import List
import faust

app = faust.App(
        'stream-event-app',
        broker='kafka://kafka-server',
        topic_partitions=1,
        value_serializer='raw')


account_table = app.Table('account',
                        partitions=1, 
                        default=int)

#transaction_table = app.Table('transactions', default=int)


# define the source topic to read the “transaction” events from
# every value in this topic is of the Transaction type
transaction_topic = app.topic('transaction', partitions=1, value_type=bytes)

authorize_log={"account": {"active-card": "", "available-limit": 0}, "violations": []}

#Error Strings
acc_not_initialized="account-not-initialized"
acc_already_initialized="account-already-initialized"
acc_not_activated="account-not-activated"
acc_insufficient="insufficient-limit"

# agent: process infinite stream of orders.
@app.agent(transaction_topic)
async def order(transactions):
    global account
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
                print(avail_limit)

                # Once created, the account should not be updated or recreated
                if (account_table["account_status"]):
                    authorize_log['violations']=[]
                    authorize_log['violations'].append(acc_already_initialized)
                elif not card_status: # account status not set and new event with "active-card": false
                    authorize_log["account"]["active-card"] = account_table["account_status"]
                    authorize_log['violations']=[]

                    # First event should be account activation, else violation
                    authorize_log['violations'].append(acc_not_activated)
                else:
                    print("activating account")
                    print(avail_limit)
                    account_table["account_status"] = 1
                    account_table["availble_limit"] = avail_limit

                    print(account_table["availble_limit"])
                    authorize_log["account"]["active-card"] = card_status
                    authorize_log["account"]["available-limit"] = avail_limit
                    authorize_log['violations']=[]

                print(json.dumps(authorize_log))
        except KeyError:
            try:
                transaction_event = event["transaction"]
                if(transaction_event):

                   if account_table["account_status"]:
                        amount = transaction_event["amount"]
                        if(amount > account_table["availble_limit"]):
                            print(amount, account_table["availble_limit"])
                            authorize_log["violations"] = []

                            # There is a violation if requested amount is more than available balance
                            authorize_log['violations'].append(acc_insufficient)
                        else:
                            # Test for requirement: Check doubled-transaction
                            # Test for requirement: Check high-frequency-small-interval

                            account_table["availble_limit"] = account_table["availble_limit"] - amount
                            authorize_log["account"]["available-limit"] = account_table["availble_limit"]
                            
                            # Update the transaction list member of account object with vendor and time infomration 
                            # for implementing above two requirments
                   else:
                        authorize_log["account"]["active-card"] = account_table["account_status"]
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