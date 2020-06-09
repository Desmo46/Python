x = 2
y = 2
print(x * y)

print (x % 5)

print(len("Hello g"))

import pandas as pd

cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000]
        }

df = pd.DataFrame(cars, columns = ['Brand', 'Price'])

print (df[0:1])