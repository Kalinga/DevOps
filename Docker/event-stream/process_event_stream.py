# This file implements an agent for the processing of streaming event
# Use the below command to start the faust application for the processing
#faust -A process_event_stream worker -l info 

import json

from datetime import datetime
from datetime import timedelta

from typing import List
import faust

app = faust.App(
        'stream-event-app',
        broker='kafka://kafka-server',
        topic_partitions=1,
        value_serializer='raw')


#kafka log based persistent data storage as Faust Table API
account_table = app.Table('account',
                        partitions=1, 
                        default=int)

transaction_table = app.Table('transactions',
                            partitions=1, 
                            default=list)


# define the source topic to read the “transaction” events from
# every value in this topic is of the Transaction type
transaction_topic = app.topic('transaction', partitions=1, value_type=bytes)

authorize_log = {"account": {"active-card": "", "available-limit": 0}, "violations": []}

#Application constants
VALID_HIGH_FREQUENCY = 3

#Error Strings
acc_not_initialized = "account-not-initialized"
acc_already_initialized = "account-already-initialized"
acc_not_activated = "account-not-activated"

high_frequency_small_interval = "high-frequency-small-interval"
doubled_transaction = "doubled-transaction"
acc_insufficient = "insufficient-limit"

def acceptTransaction(transaction):
    amount_ = transaction["amount"]
    account_table["availble_limit"] = account_table["availble_limit"] - amount_
    
    transactions_list = transaction_table["transactions"]
    transactions_list.append(transaction)
    transaction_table["transactions"] = transactions_list                     


def validateTransaction(transaction, earliest):
    new_transaction_time = datetime.strptime( transaction["time"], '%Y-%m-%dT%H:%M:%S.%fZ')
    transactions_list = transaction_table["transactions"]

    if (new_transaction_time - earliest  < timedelta(minutes=2) ):
        #print("A new transaction with in 2 minutes, check for simillarity")
        merchant = transaction["merchant"]
        amount = transaction["amount"]

        # check for doubled-transaction
        is_doubled_transaction =  False
        transaction_freq = 1 # consider the incoming transaction

        for t in transactions_list:
            time_stamp = t["time"]
            date_time = datetime.strptime(time_stamp, '%Y-%m-%dT%H:%M:%S.%fZ')

            if (new_transaction_time - date_time)  < timedelta(minutes=2):
                transaction_freq += 1
                merchant_ = t["merchant"]
                amount_ = t["amount"]
                if ( amount == amount_ and merchant == merchant_):
                    is_doubled_transaction =  True
        
        #print("transaction_freq", transaction_freq)
        #print("doubled_transaction", is_doubled_transaction)

        # check for high-frequency-small-interval
        if transaction_freq <= VALID_HIGH_FREQUENCY:
            if not is_doubled_transaction:
                acceptTransaction(transaction)
            else:
                authorize_log['violations']=[]
                authorize_log['violations'].append(doubled_transaction)
        elif transaction_freq == VALID_HIGH_FREQUENCY + 1: 
            #high-frequency-small-interval
            authorize_log['violations']=[]
            authorize_log['violations'].append(high_frequency_small_interval)

        assert transaction_freq < (VALID_HIGH_FREQUENCY + 2), \
                                    ("This should never happen, we can not have \
                                    more than 3 authorized transactions with in 2 minutes.")

    else:
        acceptTransaction(transaction)
        authorize_log['violations']=[]

    authorize_log["account"]["available-limit"] = account_table["availble_limit"]


def doTransaction(transaction):
    #print("Previous authorized transaction: ", transaction_table["transactions"])

    transactions_list = list()
    transactions_list = transaction_table["transactions"]

    if (not transactions_list): # TODO: If a better default than int can be given for app table 
        transactions_list.append(transaction)
        transaction_table["transactions"] = transactions_list
    else:
        transactions_time_stamps = list()
        for t in transactions_list:
            time_stamp = t["time"]
            date_time = datetime.strptime(time_stamp, '%Y-%m-%dT%H:%M:%S.%fZ')
            transactions_time_stamps.append(date_time)

        transactions_time_stamps.sort(reverse=True)
        oldest = transactions_time_stamps[-1]
        earliest = transactions_time_stamps[0]
        #print(earliest, oldest )

        validateTransaction(transaction, earliest)
        
        # purge unnecesarry old transactions else the list shall grow, 
        # 3-hrs old than earliest could be purged

        # purgeTransaction()


# agent: process infinite stream of orders.
@app.agent(transaction_topic)
async def order(transactions):
    global account
    async for transaction in transactions:
        event = json.loads(transaction)
        print(event)
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
                    authorize_log["account"]["active-card"] = "true" if account_table["account_status"] else "false"
                    authorize_log['violations']=[]

                    # First event should be account activation, else violation
                    authorize_log['violations'].append(acc_not_activated)
                else:
                    print("activating account")
                    print(avail_limit)
                    account_table["account_status"] = 1
                    account_table["availble_limit"] = avail_limit

                    print(account_table["availble_limit"])
                    authorize_log["account"]["active-card"] = "true" if account_table["account_status"] else "false"

                    authorize_log['violations']=[]

        except KeyError: #incoming event is not related to account
            try:
                transaction_event = event["transaction"]
                if(transaction_event):
                    authorize_log["account"]["active-card"] = "true" if account_table["account_status"] else "false"
                    authorize_log['violations'] = []

                    if account_table["account_status"]:
                        amount = transaction_event["amount"]
                        if(amount > account_table["availble_limit"]):
                            authorize_log["violations"] = []

                            # There is a violation if requested amount is more than available balance
                            authorize_log['violations'].append(acc_insufficient)
                        else:
                            doTransaction(transaction_event, )
                    else:                        
                        # No transaction is allowed unless account is active
                        authorize_log['violations'].append(acc_not_initialized)

            except KeyError:
                print("Invalid event: event must be account/transaction related")

        authorize_log["account"]["available-limit"] = account_table["availble_limit"]
        print(json.dumps(authorize_log))


def main():
    print("main: stream-event-app")
    app.main()

if __name__ == '__main__':
    main()