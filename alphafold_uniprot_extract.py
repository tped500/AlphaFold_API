import json
import pandas as pd
from alphafold_load_table import full_table

"""
File to extract data column from initial file
Data column is a JSON object
Inner JSON "outlinks" in data might not always exist
If exists, extract value of "uniprot" key
"""


def outlinks_extract(table):
    """
    :param table: csv table with Gene data from MySQL database
    :return: List of combinations of Id's and Outlinks
    """

    df_data_json = pd.DataFrame(table["id"])
    df_data_json = df_data_json.join(table["data"])

    list_outlink = []
    counter = 0
    for row in df_data_json["data"]:
        json_row = json.loads(row)
        if "outlinks" in json_row:
            if "uniprot" in json_row["outlinks"]:
                list_outlink.append((df_data_json["id"][counter], json_row["outlinks"]["uniprot"]))
            counter += 1
        else:
            counter += 1

    return list_outlink

#outlinks_extract(full_table)

