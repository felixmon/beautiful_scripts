# Asterisks for unpacking into function call
# https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/
fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print(*fruits)
# output lemon pear watermelon tomato

date_info = {'year': "2020", 'month': "01", 'day': "01"}
filename = "{year}-{month}-{day}.txt".format(**date_info)
print(filename)
# output '2020-01-01.txt'
'''
>>> date_info = {'year': "2020", 'month': "01", 'day': "01"}
>>> track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
>>> filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(
...     **date_info,
...     **track_info,
... )
>>> filename
'2020-01-01-Beethoven-Symphony No 5.txt'
'''

# Create dataframe with no header
# https://stackoverflow.com/a/53821770/13130970
df = pd.DataFrame([*zip([1,2,3],[4,5,6])])

# list all files with specific extensions.
path = os.getcwd()
files = os.listdir(path)
files_xls = [f for f in files if f[-3:] == 'xls']
