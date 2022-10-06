# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 10:09:19 2020

@author: One Jae
"""
import pandas as pd
import os
dropbox = os.path.expanduser("~/Dropbox/Unfundedpension/src/int/")

#Converts ASEP DataFrames created from ASEP_generator.py to one that matches the formats of the CoG project DataFrames
def restructure_employee(master):
    code_dict = {'000':'Total - All Government Employment Functions',
                '023':'Financial Adminstration',
               '029':'Other Government Administration',
               '025':'Judicial & Legal',
               '062':'Police Protection - Persons with Power of Arrest',
                '162':'Police Protection - Other',
               '024':'Fire Protection - Firefighters',
                '124':'Fire Protection - Other',
               '005':'Corrections',
               '006':'National Defense and International Relations',
               '014':'Postal Service',
               '002':'Space Research and Technology',
               '044':'Highways',
               '001':'Air Transporation',
               '087':'Water Transports & Terminals',
               '079':'Public Welfare',
               '032':'Health',
               '040':'Hospitals',
               '022':'Social Insurance Administration',
               '081':'Solid Waste Management',
               '080':'Sewerage',
               '061':'Park & Recreation',
               '050':'Housing & Community Development',
               '059':'Natural Resources',
               '091':'Water Supply',
               '092':'Electric Power',
               '093':'Gas Supply',
               '094':'Transit',
               '012':'Education - Elementary and Secondary Instructional',
                '112':'Education - Elementary and Secondary Other',
               '212':'Education - Elementary and Secondary Administrative and Clerical',
               '312':'Education - Elementary and Secondary Operations and Maintenance',
               '412':'Education - Elementary and Secondary Cafeteria',
               '512':'Education - Elementary and Secondary Bus Transportation',
               '612':'Education - Elementary and Secondary Health and Recreation',
               '712':'Education - Elementary and Secondary Student Employees',
               '812':'Education - Elementary and Secondary Unallocable',
               '018':'Education - Higher Education Instructional',
               '016':'Education - Higher Education Other',
               '021':'Education - Other',
               '052':'Libraries',
               '090':'State Liquor Stores',
               '089':'All other & unallocable'}
    asep_data = ['Full-Time Employees',
            'Full-Time Employees Data Flag',
            'Full-Time Payroll',
            'Full-Time Payroll Data Flag',
            'Part-Time Employees',
            'Part-Time Employees Data Flag',
            'Part-Time Payroll',
            'Part-Time Payroll Data Flag',
            'Part-Time Hours',
            'Part-Time Hours Data Flag',
            'Full-Time Equivalent Employees'
            ]
    id_col =['Name of Government',
            'Census Region Code',
            'County Name',
            'FIPS State',
            'FIPS County',
            'Population/Enrollment/Function Code',
            'Year of Population/Enrollment',
            'School Level Code',
            'Probability of Selection',
            'Worksheet Code']
    employee_dict = {}
    cols = [i for i in id_col]
    
    master = master.drop(columns = ['UniqueID'])
    cols.append('UniqueID')
    for row in master.itertuples():
        i = row.Index
        print(i)
        if i[:9] + i[14:18] not in employee_dict:
            employee_dict[i[:9] + i[14:18]] = {}
            for col in id_col:
                employee_dict[i[:9] + i[14:18]][col] = row[master.columns.get_loc(col)+1]
            employee_dict[i[:9] + i[14:18]]['Year4'] = i[14:18]
            print('year4',i[14:18] )
            print('UniqueID', i[:9] + i[14:18])
        for data in asep_data:
            code = code_dict[str(i)[18:21]] + ' ' + data
     
            employee_dict[i[:9] + i[14:18]][code] = row[master.columns.get_loc(data)+1]
            if code not in cols:
                cols.append(code)
        
    cols.append('Year4')
    df = pd.DataFrame(columns = cols)
    df.set_index('UniqueID', inplace=True, drop=False)
    i = 0
    row_list = []
    row_list.append(df)
    print(len(employee_dict))
    for key,value in employee_dict.items():
        row_list.append(pd.DataFrame(value,index = [key]))
        i+= 1
        if i%100 == 0:
            print(i)

    df = pd.concat(row_list)
    print(df)
    df.to_csv(dropbox + '/ASPEP/Restructured.csv')
    
 #Merges CoG Government Finance data to ASPEP DataFrame
def merge_employee_finances(employee,finance):
    columns = employee.columns.values.tolist()
    columns.remove('Year4')
    for row in employee.itertuples():
        i = row.Index
        for col in columns:
            try:
                finance.loc[i,col] = row[employee.columns.get_loc(col) + 1]
            except KeyError:
                print(i, 'Could not be found in finance file')
                break
    print(finance)
    finance.to_csv(dropbox + '/ASPEP/merged_master.csv')

def check_sup_sub_code(master):
    for index in master.index:
        if index[9:14] != '00000':
            print(index)
        # else:
        #     print(index[9:14])
if __name__ == '__main__':
    df1 = pd.read_csv('C:/Users/ligna/Documents/Econproj/ASEP/Restructured.csv', index_col = 0, low_memory = False)
    #Name of CoG Government Finance data to merge with
    df2 = pd.read_csv('C:/Users/ligna/Documents/Econproj/master_v4.csv',index_col = 0, low_memory=False)
    df = pd.read_csv(dropbox + '/ASEP/MasterASEP.csv', index_col = 0)
    restructure_employee(df)

    # check_sup_sub_code(df)

    #This merges the CoG with ASEP
    merge_employee_finances(df1,df2)
