"""
Script with functions to:
1) combine pandas files into single file
2) create wordpiece tokens file from single pandas file to use in tokenizer
3) tokenize sentence with vocabulary file
3) create vocabulary file from single pandas file  with correct words to find misspellings
4) return best match for words with misspellings

"""

import pandas as pd
#import modin.pandas as pd
import glob


class MinHashTool:
    def __init__(self,
                 file_name_csv_output='output.csv',dir_csv_output='./',dataframe_only=False):
        #Combibing function settings
        self.dir_csvs_path=None #Path to directory with csv files to combine
        self.file_name_csv_output=file_name_csv_output #Output csv file name
        self.dir_csv_output=dir_csv_output #Output csv directory
        self.dataframe_only=dataframe_only #If True combibng function returns dataframe as a combining result
        print('Minhash tool loaded')


    def combine_csv_files(self,dir_csvs_path,file_name_csv_output='output.csv',dir_csv_output='./',dataframe_only=False):
        """
        Function to combine vertically csv files.
        The files must have the same number of columns !!!
        Args:
            dir_csvs_path: path to directory with csv files to combine
            file_name_csv_output: output filename with combined files
            dir_out_path: directory to save output file
            dataframe_only: return dataframe if True
                            return csv file if False
        Returns:
            return csv file if dataframe_only False
            return datafrane if dataframe_only True
        """
        self.dir_csvs_path=dir_csvs_path
        self.file_name_csv_output = file_name_csv_output
        self.dataframe_only = dataframe_only

        self.file_name_csv_output=file_name_csv_output

        file_list = glob.glob(self.dir_csvs_path)
        print('CSV files list:',file_list)

        df_list = []
        for file in file_list:
            print(file)
            df = pd.read_csv(file, header=None, delimiter=';', encoding="ISO-8859-1'",error_bad_lines=False)

            df_list.append(df)
        df = pd.concat(df_list, axis=0)
        print(df.head())
        df.to_csv('out.csv', index=False,)


