# event-stream/agent.py
#faust -A process_event_stream worker -l info 
import json

import faust

app = faust.App(
        'stream-event-app', 
        broker='kafka://kafka-server',
        value_serializer='raw')

# Models describe how messages are serialized:
# {"account_id": "3fae-...", amount": 3}
class Transaction(faust.Record):
    account_status: bool
    available_limit : int

t = Transaction()
t.account_status = False
t.available_limit = 0

# define the source topic to read the “transaction” events from
#every value in this topic is of the Transaction type
transaction_topic = app.topic('transaction', value_type=bytes)

#{"account": {"active-card": "", "available-limit": 0}, "violations": []}

@app.agent(transaction_topic)
async def order(transactions):
    async for transaction in transactions:
        #print("Order processing in agent:")
        # process infinite stream of orders.
        #print(transaction)
        event = json.loads(transaction)
        #print(f'Order for {transaction.account_id}: {transaction.amount}')
        #print(type(event))
        #print(event["account"])
        try:
            account = event["account"]
            if (account):
                card_status = account["active-card"]
                avail_limit = account["available-limit"]
                t.account_status = card_status
                t.available_limit = avail_limit
                print()
        except KeyError: 
            try:
                transaction = event["transaction"]
                if(transaction):
                    merchant = transaction["merchant"]
                    amount = transaction["amount"]
                    time =  transaction["time"]
            except KeyError:
                print("Invalid event: event must be account/transaction related")

def main():
    print("main: stream-event-app")
    app.main()

if __name__ == '__main__':
    main()
