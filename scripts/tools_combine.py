import modin.pandas as pd
import glob

class CsvTool:
    def __init__(self):
        self.dir_src_path=None
        self.file_name_out=None
        self.dir_out_path=None
        self.dataframe_only=False
        pass
    def combine_csvs(self,dir_src_path,file_name_out='output.csv',dir_out_path=None,dataframe_only=False):
        """
        Function to combine vertically csv files.
        The files must have the same number of columns !!!
        Args:
            dir_src_path: path to directory with csv files to combine
            file_name_out: output filename with combined files
            dir_out_path: directory to save output file
            dataframe_only: return dataframe if True
                            return csv file if False
        Returns:
            return csv file if dataframe_only False
            return datafrane if dataframe_only True
        """
        self.dir_src_path=dir_src_path
        self.file_name_out=file_name_out
        self.dir_out_path=dir_out_path
        self.dataframe_only=dataframe_only

        path_csv = './data/csv_source/*.csv'
        file_list = glob.glob(path_csv)
        print(file_list)

        df_list = []
        for file in file_list:
            print(file)
            df = pd.read_csv(file, header=None, delimiter=';', encoding="ISO-8859-1'",error_bad_lines=False)

            df_list.append(df)
        df = pd.concat(df_list, axis=0)
        print(df.head())
        df.to_csv('out.csv', index=False,)

