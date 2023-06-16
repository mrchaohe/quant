
import os

import pymongo

client = pymongo.MongoClient("localhost", 27017, username=os.getenv('mongo_user'), password=os.getenv('mongo_pwd'))


A_DB = client["A"]    
B_DB = client["B"]    
H_DB = client["H"]    
U_DB = client["U"]  

# def create_collection():
#     A_DB.create_collection("stock")   
#     B_DB.create_collection("coin")   
#     H_DB.create_collection("h_stock")
#     U_DB.create_collection("u_stock")




 


if __name__ == "__main__":
  pass