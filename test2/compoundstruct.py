elements = {"hydrogen" : {"number" : 1,
                          "weight" : 1.00794,
                          "symbol" : "H"},
            "helium": {"number": 2,
                       "weight": 4.002602,
                       "symbol": "He"}}

elements["oxygen"] = {"number":8,
                      "weight":15.999,
                      "symbol":"O"}

elements["hydrogen"]["is_noble_gas"]="False"
elements["helium"]["is_noble_gas"]="True"

print("elements = " ,elements)

print(elements["oxygen"]["weight"])