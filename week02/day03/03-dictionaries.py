
accounts = [
	{ 'client_name': 'Igor', 'account_number': 1, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 2, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist
#acc_num = int(input("Szamlaszam: "))

#def balance(items):
 #   for i in items:
  #      if i['account_number'] == acc_num:
   #         print(i['client_name'], i['balance'])



acc_num = int(input("Szamlaszamod: "))
to_acc_num = int(input("Ahova utalni akarsz: "))
amm_num = int(input("Amennyit utalsz: "))

def transfer_money(accounts_list, acc_number):
    for i in accounts_list:
        if i['account_number'] == acc_num:
            take_money(acc_num, amm_num, accounts)
            add_money(to_acc_num, amm_num, accounts)
    print(accounts)
        
def take_money(from_id, by_ammount, accounts_list):
    for i in accounts_list:
        if i["account_number"] == from_id:
            i["balance"] -= by_ammount


def add_money(to_id, by_ammount, accounts_list):
    for i in accounts_list:
        if i["account_number"] == to_id:
            i["balance"] += by_ammount



#balance(accounts)

transfer_money(accounts, acc_num)
