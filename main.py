import pandas as pd
import csv

file = 'Categories.csv'
df = pd.read_csv('Financials_Discover.csv')

# grabs headers of a csv file
# returns list of headers and a dictionary with index position as key
def current_headers(file):
    # Grab Current Headers
    header_check_df = pd.read_csv(file)
    pandas_index_headers = header_check_df.columns
    current_headers_dic = {}
    current_headers_list = []
    idx = 0
    for header in pandas_index_headers:
        current_headers_dic[idx] = header
        current_headers_list.append(header)
        idx = idx + 1

    return current_headers_list, current_headers_dic

# add new header
def add_new_category(file, category):
    df = pd.read_csv(file)
    df[category] = None
    df.to_csv(file, index=False)


# Check if value exists in the category file
def check_exists(file, obj):
    df = pd.read_csv(file)
    header_list, _ = current_headers(file)
    exists = False
    for header in header_list:
        exists = df[header].eq(obj).any()
        if exists == True:
            return True
    return False

# append column
def append_column(file, column, obj):
    df = pd.read_csv(file)
    s1 = df[column]
    s_obj = pd.Series(obj)
    s1 = pd.concat([s_obj, s1], ignore_index=True, axis=0)
    df[column] = s1
    df.to_csv(file, index=False)

# returns category header or New to indicate needs a new category
def list_category_options(file):
    headers, dictionary = current_headers(file)
    idx = 0
    for header in headers:
        print(idx, ': ', header)
        idx = idx + 1
    print('n', ': ', 'New Category')
    ans = input('Which category should this belong to?')
    if ans == 'n':
        return 'New'
    else:
        return dictionary[int(ans)]



for element in df.Description:
    headers, _ = current_headers(file)
    if check_exists(file, element):
        continue
    else:
        print('What category should ', element, ' go into?')
        ans = list_category_options(file)
        if ans == 'New':
            new_category = input('What should the new Category be?')
            add_new_category(file, new_category)
            append_column(file, new_category, element)
        else:
            append_column(file, ans, element)









# Create New csv file
def new_csv(file, category_list):
    with open(file,'w') as f:
        writer = csv.writer(f)
        writer.writerow(category_list)

#new_csv('Categories.csv', ['McDonalds'])
