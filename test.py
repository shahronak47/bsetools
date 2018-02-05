from bsetools import bsetools
import pandas as pd
import pdb

#path of the csv file
CSV_FILE_PATH = "C:\\Users\\Ronak Shah\\Google Drive\\Documents\\Shares.csv"


if __name__ == '__main__' :
    share_price = []
    #Read the csv file which has data
    df = pd.read_csv(CSV_FILE_PATH)
    bse_object = bsetools()
    for share in df['Shares'] :
        share_price.append(bse_object.get_quote(share))
    print(share_price)
