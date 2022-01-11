import os
import os.path
from typing import Text



def open_files_in_sequence():
    number_of_year = 17
    number_of_month = 00
    number_of_day = 00
    folder_address_prefix = "Test_Data_Folder/"
    names_of_cities_to_iterate = ["Ibiza", "Miami", "Venice"]
    number_of_cities = len(names_of_cities_to_iterate)
    
    for iterate_through_years in range(0,2):
        number_of_year = number_of_year + 1
        number_of_month = 00
        folder_address_builder_pt_I = str(number_of_year)

        for iterate_through_months in range(0, 12):
            number_of_month = number_of_month + 1
            number_of_day = 00
            folder_address_builder_pt_II = str(number_of_month).zfill(2) + "." + folder_address_builder_pt_I

            for iterate_through_days in range(0,31):
                number_of_day = number_of_day + 1
                folder_address_builder_pt_III =  str(number_of_day).zfill(2) + "." + folder_address_builder_pt_II
                folder_address = folder_address_prefix + folder_address_builder_pt_I + "/" + folder_address_builder_pt_II + "/" + folder_address_builder_pt_III
                
                for city_iteration_index_number in range(0, number_of_cities):
                    city = names_of_cities_to_iterate[city_iteration_index_number]
                    file_name = folder_address + "/" + city + ".csv"    
                    try:
                        if(open (file_name, "r", encoding="utf-8-sig")):
                            extract_raw_data_from_files(file_name)                            
                    except:
                        pass
                        
                    
                
def extract_raw_data_from_files(file_name):
    with open(file_name,"r") as file_data:
        raw_file_data = file_data.read()
    identify_column_names_and_data_blocks(raw_file_data)

def identify_column_names_and_data_blocks(raw_file_data):
    data_blocks = raw_file_data.split('","')
    column_names = data_blocks[0].split(',')

    pull_useful_data_out_of_blocks(column_names, data_blocks)



def pull_useful_data_out_of_blocks(column_names, data_blocks):
    loop_step_counter = 0
    print(column_names)
    for k in range(0, len(data_blocks)):
        if (loop_step_counter-1) % 8 == 0:
            print(data_blocks[loop_step_counter+1])
            print(data_blocks[loop_step_counter+3])
            if data_blocks[loop_step_counter+3][1:8] == "Selling":
                print(data_blocks[loop_step_counter+5])
                print(data_blocks[loop_step_counter+6])
                print(data_blocks[loop_step_counter+7])
                print("Break 5")
            else:
                print(data_blocks[loop_step_counter+4])
                print(data_blocks[loop_step_counter+5])
                print("Break 4")

        loop_step_counter += 1
        


open_files_in_sequence()


