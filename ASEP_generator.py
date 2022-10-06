# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 13:50:42 2020

@author: One Jae
"""
import pandas as pd
import os
import numpy as np
from statistics import mean 

project_folder = os.path.expanduser("~/Dropbox/Unfundedpension/src/")
int_folder = os.path.expanduser("~/Dropbox/Unfundedpension/src/int/ASPEP/")

#Converts empst files into DataFrames
def empst_to_df(file_name, year):
    f = open(file_name, "r")
    if int(year) < 2007 or year == None:
        state_code = []
        unit_type = []
        county_code = []
        unit_id = []
        sup_code = []
        sub_code = []
        item_code = []
        full_empl = []
        full_empl_df = []
        full_payroll = []
        full_payroll_df = []
        part_emp = []
        part_emp_df = []
        part_payroll = []
        part_payroll_df = []
        part_hours = []
        part_hours_df = []
        full_equiv_employee = []
    
        unique_id_code = []
        unique_id = []
        id_list = []
        for line in f:
            unique_id_code.append(str(line[:14].replace(" ", "")) + str(year) + str(line[17:20].replace(" ", "")))
            unique_id.append(line[:14].replace(" ", "") + str(year))
            id_list.append(line[:14].replace(" ", ""))
            state_code.append(line[:2].replace(" ", ""))
        
            unit_type.append(line[2:3].replace(" ", ""))
            
            county_code.append(line[3:6].replace(" ", ""))
        
            unit_id.append(line[6:9].replace(" ", ""))
        
            sup_code.append(line[9:12].replace(" ", ""))
        
            sub_code.append(line[12:14].replace(" ", ""))
        
            item_code.append(line[17:20].replace(" ", ""))
        
            full_empl.append(line[20:30].replace(" ", ""))
        
            full_empl_df.append(None)
        
            full_payroll.append(line[30:42].replace(" ", ""))
            
            full_payroll_df.append(None)
        
            part_emp.append(line[42:52].replace(" ", ""))
        
            part_emp_df.append(None)
        
            part_payroll.append(line[52:64].replace(" ", ""))
        
            part_payroll_df.append(None)
            
            part_hours.append(line[64:73].replace(" ", ""))
            
            part_hours_df.append(None)
            
            full_equiv_employee.append(line[74:84].replace(" ", ""))
        
    else:
    
        state_code = []
        unit_type = []
        county_code = []
        unit_id = []
        sup_code = []
        sub_code = []
        item_code = []
        full_empl = []
        full_empl_df = []
        full_payroll = []
        full_payroll_df = []
        part_emp = []
        part_emp_df = []
        part_payroll = []
        part_payroll_df = []
        part_hours = []
        part_hours_df = []
        full_equiv_employee = []
        unique_id_code = []
        unique_id = []
        id_list = []
        for line in f:
            unique_id_code.append(str(line[:14].replace(" ", "")) + str(year) + str(line[17:20].replace(" ", "")))

            unique_id.append(line[:14].replace(" ", "") + str(year))
            id_list.append(line[:14].replace(" ", ""))
            state_code.append(line[:2].replace(" ", ""))
        
            unit_type.append(line[2:3].replace(" ", ""))
            
            county_code.append(line[3:6].replace(" ", ""))
        
            unit_id.append(line[6:9].replace(" ", ""))
        
            sup_code.append(line[9:12].replace(" ", ""))
        
            sub_code.append(line[12:14].replace(" ", ""))
        
            item_code.append(line[17:20].replace(" ", ""))
        
            full_empl.append(line[20:30].replace(" ", ""))
        
            full_empl_df.append(line[31:32].replace(" ", ""))
        
            full_payroll.append(line[32:44].replace(" ", ""))
            
            full_payroll_df.append(line[45:46].replace(" ", ""))
        
            part_emp.append(line[46:56].replace(" ", ""))
        
            part_emp_df.append(line[57:58].replace(" ", ""))
        
            part_payroll.append(line[58:70].replace(" ", ""))
        
            part_payroll_df.append(line[71:72].replace(" ", ""))
            
            part_hours.append(line[72:82].replace(" ", ""))
            
            part_hours_df.append(line[83:84].replace(" ", ""))
            
            full_equiv_employee.append(line[84:94].replace(" ", ""))
    
    
    
    data = {'UniqueIDItem':unique_id_code,
            'UniqueID':unique_id,
            'State Code': state_code,
            'Unit Type Code':unit_type,
            'County Code':county_code,
            'Unit ID':unit_id,
            'Supplement code':sup_code,
            'Sub code':sub_code,
            'Item Code':item_code,
            'Full-Time Employees':full_empl,
            'Full-Time Employees Data Flag':full_empl_df,
            'Full-Time Payroll': full_payroll,
            'Full-Time Payroll Data Flag':full_payroll_df,
            'Part-Time Employees':part_emp,
            'Part-Time Employees Data Flag':part_emp_df,
            'Part-Time Payroll':part_payroll,
            'Part-Time Payroll Data Flag':part_payroll_df,
            'Part-Time Hours':part_hours,
            'Part-Time Hours Data Flag':part_hours_df,
            'Full-Time Equivalent Employees':full_equiv_employee}
    data = pd.DataFrame(data)
    data.set_index('UniqueIDItem', inplace=True, drop=True)
    return pd.DataFrame(data)
#Converts empid to DataFrames
def empid_to_df(file_name, year):
    f = open(file_name, "r")
    

    state_code = []
    unit_type = []
    county_code = []
    unit_id = []
    sup_code = []
    sub_code = []
    
    gov_name = []
    census_region = []
    county_name = []
    fips_state = []
    fips_county = []
    pop = []
    year_pop = []
    school_level = []
    prob = []
    work = []
    

    unique_id = []
    id_list = []
    for line in f:
        unique_id.append(line[:14].replace(" ", "") + str(year))
        id_list.append(line[:14].replace(" ", ""))
        state_code.append(line[:2].replace(" ", ""))
    
        unit_type.append(line[2:3].replace(" ", ""))
        
        county_code.append(line[3:6].replace(" ", ""))
    
        unit_id.append(line[6:9].replace(" ", ""))
    
        sup_code.append(line[9:12].replace(" ", ""))
    
        sub_code.append(line[12:14].replace(" ", ""))
    
        gov_name.append(line[14:78].replace(" ", ""))
    
        census_region.append(line[78:79].replace(" ", ""))
    
        county_name.append(line[79:109].replace(" ", ""))
    
        fips_state.append(line[109:111].replace(" ", ""))
        
        fips_county.append(line[111:114].replace(" ", ""))
    
        pop.append(line[125:134].replace(" ", ""))
    
        year_pop.append(line[134:136].replace(" ", ""))
    
        school_level.append(line[136:138].replace(" ", ""))
    
        prob.append(line[145:151].replace(" ", ""))
                
        work.append(line[204:206].replace(" ", ""))
        
        



    data = {'UniqueID':unique_id,
            'State Code': state_code,
            'Unit Type Code':unit_type,
            'County Code':county_code,
            'Unit ID':unit_id,
            'Supplement code':sup_code,
            'Sub code':sub_code,
            'Name of Government':gov_name,
            'Census Region Code':census_region,
            'County Name':county_name,
            'FIPS State': fips_state,
            'FIPS County':fips_county,
            
            'Population/Enrollment/Function Code':pop,
            'Year of Population/Enrollment':year_pop,
            'School Level Code':school_level,
            'Probability of Selection':prob,
            'Worksheet Code':work}
    data = pd.DataFrame(data)
    data.set_index('UniqueID', inplace=True, drop=False)
    return pd.DataFrame(data)

#Merges two different DataFrames for each corresponding year created from empst and empid into one DataFrame
def merge_st_id(empst,empid):
    new_col = ['Name of Government',
               'Census Region Code',
            'County Name',
            'FIPS State',
            'FIPS County',
            'Population/Enrollment/Function Code',
            'Year of Population/Enrollment',
            'School Level Code',
            'Probability of Selection',
            'Worksheet Code']

    for x in new_col:
        empst[x] = np.nan

    for index in empst.index:
        for x in new_col:

            try:
                empst.loc[index, x] = empid.at[index[:18],x]
            except KeyError:
                
                print(index[:18], "Could not be found in ID")
                break

    print(empst)
    return empst

#Reads folder hosting all empid and empst zip files from FBI to convert into DataFrames
def read_folder(folder_directory):
    st_files = []
    id_files = []
    year_dict = {}
    for i in os.listdir(folder_directory):
        for root, dirs,files in os.walk(folder_directory+i):
            for file in files:
                if ('empid' in file or 'EMPID' in file) and '.zip' not in file:
                    print(os.path.join(root, file))
                    id_files.append((os.path.join(root, file), str(file)[:2]))
                elif ('empst'in file or 'EMPST' in file) and '.zip' not in file:
                    print(os.path.join(root, file))
                    st_files.append((os.path.join(root, file), str(file)[:2]))
    for x in st_files:
        if str(x[1])[0] == '0' or str(x[1])[0] == '1':
            df = empst_to_df(x[0], '20' + str(x[1]))
 
            year_dict['20' + str(x[1])] = [df]
        else:
            df = empst_to_df(x[0], '19' + str(x[1]))

            year_dict['19' + str(x[1])] = [df]
            
    for x in id_files:
        if str(x[1])[0] == '0' or str(x[1])[0] == '1':
            df = empid_to_df(x[0], '20' + str(x[1]))
 
            year_dict['20' + str(x[1])].append(df)
        else:
            df = empid_to_df(x[0], '19' + str(x[1]))

            year_dict['19' + str(x[1])].append(df)
    df_list = []
    i=0
    for x in year_dict.values():

        temp  = merge_st_id(x[0],x[1])
        temp.to_csv(int_folder + '/' + str(i) + 'ASEP.csv')
        
        df_list.append(temp)
        print(int_folder + '/' + str(i) + 'ASEP.csv')
        i+=1
 
        
    append_asep(int_folder)

 


#Combines all years of ASEP files into one large master file
def append_asep(folder_directory):
    l = []
    for i in os.listdir(folder_directory):
        if 'ASEP' in i:
            print(i)
            print(pd.read_csv(folder_directory+'/' + i,index_col = 0))
            l.append(pd.read_csv(folder_directory+'/' + i,index_col = 0))
    indicator = True
    for x in l:
        if indicator:
            master = x
            indicator = False
        else:
            master = master.append(x)
            print(master)
    master.to_csv(folder_directory + '/' + 'Master' +'ASEP.csv')
        
#Reads all the empst and empid files in a folder to create DataFrames
def read_folder_state(folder_directory): 
    
    st_files = []
    id_files = []
    year_dict = {}
    for i in os.listdir(folder_directory):
        for root, dirs,files in os.walk(folder_directory+i):
            for file in files:
                if ('state.dat' in file or 'STATE.dat' in file) and '.zip' not in file:
                    print(os.path.join(root, file))
                    id_files.append((os.path.join(root, file), str(file)[:2]))
                elif ('state.id'in file or 'EMPST.id' in file) and '.zip' not in file:
                    print(os.path.join(root, file))
                    st_files.append((os.path.join(root, file), str(file)[:2]))
    for x in st_files:
        if str(x[1])[0] == '0' or str(x[1])[0] == '1':
            df = empst_to_df(x[0], '20' + str(x[1]))
            year_dict['20' + str(x[1])] = [df]
        else:
            df = empst_to_df(x[0], '19' + str(x[1]))

            year_dict['19' + str(x[1])] = [df]
            
    for x in id_files:
        if str(x[1])[0] == '0' or str(x[1])[0] == '1':
            df = empid_to_df(x[0], '20' + str(x[1]))

            year_dict['20' + str(x[1])].append(df)
        else:
            df = empid_to_df(x[0], '19' + str(x[1]))

            year_dict['19' + str(x[1])].append(df)
    df_list = []
    i=0
    for x in year_dict.values():

        temp  = merge_st_id(x[0],x[1])
        print(temp)
        temp.to_csv(folder_directory + '/' + str(i) +'ASEP.csv')
        
        df_list.append(temp)
        print(folder_directory + '/' + str(i) +'ASEP.csv')
        i+=1

        
    df = None
    for x in df_list:
        if df is None:
            df = x
        else:
            df = df.append(x)
        print(df)
    df.to_csv(folder_directory + '/' + 'Master' +'ASEP.csv')
    return df

#Compares imputed values to values that are known to be not imputed to understand how accurate the imputed data is 
#An attempt at imputing totals that was done before Paul gave the Census Bureau's imputation
def compare_employees(file_directory):
    master = pd.read_csv(file_directory, index_col = 0, low_memory = False)
    
    func = [
    'Financial Adminstration',
    'Other Government Administration',
     'Judicial & Legal',
     'Police Protection - Persons with Power of Arrest',
      'Police Protection - Other',
     'Fire Protection - Firefighters',
     'Fire Protection - Other',
     'Corrections',
       'National Defense and International Relations',
        'Postal Service',
               'Space Research and Technology',
               'Highways',
              'Air Transporation',
               'Water Transports & Terminals',
             'Public Welfare',
              'Health',
             'Hospitals',
               'Social Insurance Administration',
               'Solid Waste Management',
               'Sewerage',
               'Park & Recreation',
               'Housing & Community Development',
              'Natural Resources',
               'Water Supply',
               'Electric Power',
               'Gas Supply',
               'Transit',
               'Education - Elementary and Secondary Instructional',
                'Education - Elementary and Secondary Other',
               # 'Education - Elementary and Secondary Administrative and Clerical',
               # 'Education - Elementary and Secondary Operations and Maintenance',
               # 'Education - Elementary and Secondary Cafeteria',
               # 'Education - Elementary and Secondary Bus Transportation',
               # 'Education - Elementary and Secondary Health and Recreation',
               # 'Education - Elementary and Secondary Student Employees',
               # 'Education - Elementary and Secondary Unallocable',
               'Education - Higher Education Instructional',
               'Education - Higher Education Other',
               'Education - Other',
               'Libraries',
               'State Liquor Stores',
               'All other & unallocable']
    emp_type = ['Full-Time Employees',
            'Full-Time Payroll',
            'Part-Time Employees',
            'Part-Time Payroll',
            'Part-Time Hours',
            'Full-Time Equivalent Employees'
            ]
    emp_dict = {}
    for x in emp_type:
        emp_dict['Total - All Government Employment Functions' + ' ' + x] = []
        for y in func:
            emp_dict['Total - All Government Employment Functions' + ' ' + x].append(y + ' ' + x)
    
    stat_dict = {}
    for x in emp_dict.keys():
        # print(x,emp_dict[x])
        stat_dict[x] = []
    # for x in func:
    #     for y in emp_type:
    #         all_func.append(x+ ' ' +y)
            
    # print(all_func)
    er = 0
    empty = 0
    filler = 0
    t = 0
    mt= 0
    total_filler = 0
    zed = 0
    
    noimputed_yestotal = 0
    #most important is the full-time lines
    for row in master.itertuples():
        i = row.Index
        if str(str(i)[2]) == '2':
            c = 0
            for y in emp_dict.keys():
                imputed = 0
                # print(y)
                total = row[master.columns.get_loc(y)+1]
                # print(i,y, row[master.columns.get_loc(y)+1])
                
                if not pd.isnull(total):
                    
                    if int(total)!= 9999999999 and int(total)!=999999999:
                        total = int(total)
                        for sub in emp_dict[y]:
                            subtotal = row[master.columns.get_loc(sub)+1]
                            if not pd.isnull(subtotal):
                                if int(total) == 9999999999 or int(subtotal) == 9999999999 or int(total) == 999999999 or int(subtotal) ==999999999:
                                    filler +=1
                                else:
                                    imputed += int(subtotal)
                        if imputed != total and imputed != 0:
                            # print(i)
                            # print('Imputed', imputed)
                            # print('Total', total)
                            # print(((total-imputed)/((total+imputed)/2))*100)
                            t += 1
                            er += 1
                            print(total, imputed)
                            print(i, abs(((total-imputed)/((total+imputed)/2))*100))
                            stat_dict[y].append(abs(((total-imputed)/((total+imputed)/2))*100))
                        elif imputed == 0:
                            zed += 1
                            t += 1
                            if total != 0:
                                noimputed_yestotal += 1
                        else:
                            stat_dict[y].append(0)
                            t += 1
                    elif int(total) == 9999999999:
                        total_filler += 1
                else:
                    c+= 1
                    if c > 5:
                        print( i)
                    
                    # print(c)
                    # print(total)
                    empty += 1
    for key in stat_dict.keys():
        print(key, mean(stat_dict[key]))
    print('Error', er)
    print('Total', t)
    print('Empty', empty)
    print('out of ',mt + t)
    print('filler', filler)
    print('filler in total', total_filler)
    print('zed',zed)
    print('noimputed_yestotal', noimputed_yestotal)
    
#Compares imputed values to values that are known to be not imputed to understand how accurate the imputed data is 
#An attempt at imputing totals that was done before Paul gave the Census Bureau's imputation
def compare(file_directory):
    master = pd.read_csv(file_directory, index_col = 0, low_memory = False)
    
    func = [
    'Financial Adminstration',
    'Other Government Administration',
     'Judicial & Legal',
     'Police Protection - Persons with Power of Arrest',
      'Police Protection - Other',
     'Fire Protection - Firefighters',
     'Fire Protection - Other',
     'Corrections',
       'National Defense and International Relations',
        'Postal Service',
               'Space Research and Technology',
               'Highways',
              'Air Transporation',
               'Water Transports & Terminals',
             'Public Welfare',
              'Health',
             'Hospitals',
               'Social Insurance Administration',
               'Solid Waste Management',
               'Sewerage',
               'Park & Recreation',
               'Housing & Community Development',
              'Natural Resources',
               'Water Supply',
               'Electric Power',
               'Gas Supply',
               'Transit',
               'Education - Elementary and Secondary Instructional',
                'Education - Elementary and Secondary Other',
               # 'Education - Elementary and Secondary Administrative and Clerical',
               # 'Education - Elementary and Secondary Operations and Maintenance',
               # 'Education - Elementary and Secondary Cafeteria',
               # 'Education - Elementary and Secondary Bus Transportation',
               # 'Education - Elementary and Secondary Health and Recreation',
               # 'Education - Elementary and Secondary Student Employees',
               # 'Education - Elementary and Secondary Unallocable',
               'Education - Higher Education Instructional',
               'Education - Higher Education Other',
               'Education - Other',
               'Libraries',
               'State Liquor Stores',
               'All other & unallocable']
    emp_type = ['Full-Time Employees',
            'Full-Time Payroll',
            'Part-Time Employees',
            'Part-Time Payroll',
            'Part-Time Hours',
            'Full-Time Equivalent Employees'
            ]
    emp_dict = {}
    for x in emp_type:
        emp_dict['Total - All Government Employment Functions' + ' ' + x] = []
        for y in func:
            emp_dict['Total - All Government Employment Functions' + ' ' + x].append(y + ' ' + x)
    
    stat_dict = {}
    for x in emp_dict.keys():
        stat_dict[x] = []

    no_imputed_list = []
    er = 0
    empty = 0
    filler = 0
    t = 0
    mt= 0
    total_filler = 0
    zed = 0
    filler_list = []
    noimputed_yestotal = 0
    #most important is the full-time lines
    for row in master.itertuples():
        i = row.Index
        ind = int(str(i)[-4:])
        if ind < 2007 and ind > 2001:
            c = 0
            for y in emp_dict.keys():
                imputed = 0
                total = row[master.columns.get_loc(y)+1]
                
                if not pd.isnull(total):
                    if int(total)!= 9999999999 and int(total)!=999999999:
                        total = int(total)
                        for sub in emp_dict[y]:
                            subtotal = row[master.columns.get_loc(sub)+1]
                            if not pd.isnull(subtotal):
                                if int(total) == 9999999999 or int(subtotal) == 9999999999 or int(total) == 999999999 or int(subtotal) ==999999999:
                                    filler +=1
                                else:
                                    imputed += int(subtotal)
                                
                        if imputed != total and imputed != 0:
                            t += 1
                            er += 1
    
                            stat_dict[y].append(abs(((total-imputed)/((total+imputed)/2))*100))
                        elif imputed == 0:
                            zed += 1
                            t += 1
                            if total != 0:
                                noimputed_yestotal += 1
 
                        else:
                            stat_dict[y].append(0)
                            t += 1
                    if int(total) == 9999999999 or int(total) == 999999999:
                        filler_list.append(i)
                else:
                    c+= 1
                    if c > 5:
                        if len(str(i)) < 13:
                            print(i, total, imputed)
                        no_imputed_list.append(str(i))
                    

                    empty += 1
    for key in stat_dict.keys():
        print(key, mean(stat_dict[key]))
    print('Error', er)
    print('Total', t)
    print('Empty', empty)
    print('out of ',mt + t)
    print('filler', filler)
    print('filler in total', total_filler)
    print('zed',zed)
    print('noimputed_yestotal', noimputed_yestotal)
    print(no_imputed_list)
    no_imputed = {}
    
    for i in no_imputed_list:
        if len(i) < 13:
            if str(i)[-4:] in no_imputed:
                no_imputed[str(i)[-4:]].append('0' + i[:-4] + '00000')
            else:
                no_imputed[str(i)[-4:]] = ['0' + i[:-4] + '00000']
        else:
            if str(i)[-4:] in no_imputed:
                no_imputed[str(i)[-4:]].append(i[:-4] + '00000')
            else:
                no_imputed[str(i)[-4:]]= [i[:-4] + '00000']

    for x in no_imputed:
        print(x, len(no_imputed[x]))

#Data from Paul is turned into a usable format that matches previous data
def format_imputation(folder_directory):
    for i in os.listdir(folder_directory):
        print(i)
        if i[-3:] == 'txt':
            reading = open(folder_directory+'/' + i, 'r')
            writing = open(folder_directory+'/modified/' + i[:4] +'modified.txt', 'w')
            lines = reading.readlines()
            for line in lines:
                splt = line.split()
                newline = '{:>13} {:>5} {:>9} {:>11} {:>9} {:>11} {:>9} {:>9}'.format(*splt)
                writing.writelines(newline + '\n')
            reading.close()
            writing.close()
        
if __name__ == '__main__':
    #If you need to make the files from only raw data (from scratch)
    #Then run aspepformat afterwards for the restructured version to merge with CoG data
    read_folder(project_folder + '/raw/aspep/')
    #If you already have every year's ASEP.csv file but need to make the Master file, run the single line below
    #append_asep(project_folder + '/ASEP/')
    
    
    # print(read_folder(project_folder + '/ASEP/'))
    
    #Data given from Paul with imputed data not publically available
    format_imputation(project_folder + '/ASEP/new_imputed/')
    
    #Test accuracy of imputation prior to Census Bureau's own imputation
   ##### compare(project_folder+ '/ASEP_save/Restructured.csv')
    
    #compare_employees(project_folder+ '/ASEP_save/Restructured.csv')
    # append_asep(project_folder + '/ASEP/')
