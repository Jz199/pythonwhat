import unittest
from urllib.request import urlretrieve
import os.path
import sys

def download(fromfile, tofile):
    if not os.path.isfile(tofile):
        fn = 'http://s3.amazonaws.com/assets.datacamp.com/production/' + fromfile
        urlretrieve(fn, tofile)    

if __name__ == "__main__":
    
    # change path to tests
    os.chdir(os.path.dirname(sys.argv[0]))

    download('course_998/datasets/moby_opens.txt', 'moby_dick.txt')
    download('course_998/datasets/moby_opens.txt', 'not_moby_dick.txt')
    download('course_998/datasets/sales.sas7bdat', 'sales.sas7bdat')
    download('course_998/datasets/data.p', 'data.p')
    download('course_998/datasets/ja_data2.mat', 'albeck_gene_expression.mat')
    download('course_998/datasets/battledeath.xlsx', 'battledeath.xlsx')
    download('course_998/datasets/Chinook.sqlite', 'Chinook.sqlite')
    download('course_998/datasets/titanic_sub.csv', 'titanic.csv')
    download('course_998/datasets/tweets3.txt', 'tweets.txt')
    download('course_1115/datasets/census.sqlite', 'census.sqlite')
    download('course_998/datasets/mnist_kaggle_some_rows.csv', 'digits.csv')

    f = open('cars.csv', "w")
    f.write(""",cars_per_cap,country,drives_right
    US,809,United States,True
    AUS,731,Australia,False
    JAP,588,Japan,False
    IN,18,India,False
    RU,200,Russia,True
    MOR,70,Morocco,True
    EG,45,Egypt,True""")
    f.close()

    unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.discover("."))
