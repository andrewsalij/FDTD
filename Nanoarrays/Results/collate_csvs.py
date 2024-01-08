import pandas
import os


def collate(directory_path,file_prefix,suffix_list = ["M45_LC","M45_RC","P45_LC","P45_RC"],y_data_label = "T ",init_file_extension = ".txt"):
    collated_dataframe = None
    for i in range(len(suffix_list)):
        current_filepath = os.sep.join((directory_path,file_prefix+suffix_list[i]+init_file_extension))
        current_dataframe = pandas.read_csv(current_filepath)
        if collated_dataframe is None:
            collated_dataframe=  current_dataframe
            collated_dataframe.columns = ["lambda(nm)",y_data_label+suffix_list[i]]
        else:
            current_dataframe.drop(current_dataframe.columns[0],axis = 1,inplace = True)
            current_dataframe.columns = [y_data_label+suffix_list[i]]
            collated_dataframe = pandas.concat((collated_dataframe,current_dataframe),axis = 1)
    return collated_dataframe

directory_path = r"C:\Users\andre\Documents\DeyNanoarray\50nm"
file_prefix = "Trans_S50nm_"

filename_to_save = "50nmVis"

dataframe = collate(directory_path,file_prefix)

dataframe.to_csv(filename_to_save+".csv")
dataframe.to_pickle(filename_to_save+".pkl")

