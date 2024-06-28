import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head() # так не хочет выводить
print(data.head())

# one hot с get_dummie()
data_onehot = pd.get_dummies(data, columns=['whoAmI'])
print(data_onehot.head())

# one hot без get_dummie()
data = data.assign(whoAmI_human=data['whoAmI'] == 'human',whoAmI_robot=data['whoAmI'] == 'robot').drop('whoAmI',axis=1)
print(data.head())
