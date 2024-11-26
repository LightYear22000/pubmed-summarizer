import requests
import os
from metapub import FindIt


def get_pmid_from_url(url):
    return url.split("/")[-2]


def download_paper(url, output_dir):
    """
    Download a paper from PubMed Central (PMC) using the PMC ID.

    Args:
        url (str): The URL of the paper that needs to be downloaded.
        output_dir (str): The directory where the paper will be saved.

    Returns:
        str: The path to the downloaded paper or an error message if download fails.
    """
    # Base URL for downloading PMC papers
    pm_id = get_pmid_from_url(url)
    metapub_response = FindIt(pm_id)

    if metapub_response.url is None:
        raise Exception(
            f"Could not download paper for {url}: {metapub_response.reason}")

    base_url = metapub_response.url

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Define the output file path
    output_file = os.path.join(output_dir, f"{pm_id}.pdf")

    # Attempt to download the PDF
    response = requests.get(base_url, stream=True)
    if response.status_code == 200:
        # Save the PDF to the output file
        with open(output_file, "wb") as pdf_file:
            for chunk in response.iter_content(chunk_size=8192):
                pdf_file.write(chunk)
        print(f"Downloaded at {output_file}")
        return output_file
    else:
        print(f"Failed to download {pm_id}: HTTP {response.text}")


download_paper("https://pubmed.ncbi.nlm.nih.gov/39201801/?utm_source=Other&utm_medium=rss&utm_campaign=pubmed-2&utm_content=1xUFNDUH9GgcD9fNW6SIziqcwgAz3kWw5uqQ3XvLCRGR9gXMXt&fc=20241006182642&ff=20241006225626&v=2.18.0.post9+e462414",
               "/home/ashishanjan/Desktop/Project/data/papers/")
