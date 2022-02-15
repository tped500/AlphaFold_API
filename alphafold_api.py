import requests
from alphafold_uniprot_extract import outlinks_extract
from alphafold_load_table import full_table

"""
Consuming AlphaFold API
API in the form of:
https://alphafold.ebi.ac.uk/api/prediction/{UniProt ID}
Response of API in JSON format
"""

# Load dataset with Gene ID and UniProt ID
# Input from outlinks_extract function from alphafold_uniprot_extract.py file
uniprot_list = outlinks_extract(full_table)


def pdb_extract(api_json):
    """
    Function to extract PDB files URL
    :param api_json: receives a list with ("id", "uniprot_id") format
    :return: list with the format ("id", "alphafold api link")
    """
    # Create list with all responses from API
    append_data = []

    # Iterate through input to fetch data from API
    for uni_id in api_json:
        api_url = f"https://alphafold.ebi.ac.uk/api/prediction/{uni_id[1]}"
        api_response = requests.get(api_url)
        append_data.append((uni_id[0], api_response.json()[0]["pdbUrl"]))

    return append_data


for row in pdb_extract(uniprot_list):
    pdb_url = row[1]  # contains link to API response
    trimmed_url = list(pdb_url.split("/"))[-1]
    open_request = requests.get(f"https://alphafold.ebi.ac.uk/files/{trimmed_url}")
    print(f"https://alphafold.ebi.ac.uk/files/{trimmed_url}")
    open(f"./AlphafoldResults/{row[0]}.pdb", 'wb').write(open_request.content)

