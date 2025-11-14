import pandas as pd

Value = {
    "Name": ["Aman", "Shubham", "Preet", "Prince", "Kunal"],
    "State": ["Rajasthan", "Gujarat", "Goa", "Bihar", "Maharashtra"],
    "Color": ["Red", "Green", "Blue", "Yellow", "Pink"],
    "Age": [19, 17, 16, 18, 17]
}

result = pd.DataFrame(Value)
print(f"DataFrame of Value: \n{result}")
print("-." * 20)
print(f"Rajasthan ['State', 0]: {result.loc[0, 'State']}")