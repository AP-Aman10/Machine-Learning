import pandas as pd

Value = {
    "Name": ["Aman", "Shubham", "Preet", "Prince", "Kunal"],
    "State": ["Rajasthan", "Gujarat", "Goa", "Bihar", "Maharashtra"],
    "Color": ["Red", "Green", "Blue", "Yellow", "Pink"],
    "Age": [19, 17, 16, 18, 17]
}

result = pd.Series(Value)
print(f"Series: \n{result}")