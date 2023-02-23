database_record = {"name": "Grisha Brenden", "number": "12395", "address": "995 Regent Dr"}
transaction = {"name": "Grisha Brenden", "number": "12395", "address": "995 Regent Dr"}

def match(_database_record: dict, _transaction: dict) -> bool:
  if transaction["name"] == database_record["name"]:
    if transaction["number"] == database_record["number"]:
      if transaction["address"] == database_record["address"]:
        return True
    else:
      return False
match(database_record, transaction)


if database_record['name'] == database_record['number'] == database_record == ['adress']:
  raise NotImplementedError("Two fields in the dictionary are identical and should not be")
  
assert type(database_record) == dict

assert database_record['address'] == transaction['address']

assert match(database_record, transaction)
