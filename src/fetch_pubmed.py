import requests 
import time 
BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def search_pubmed(term, max_results=200):
    params = {
        "db": "pubmed",
        "term": term,
        "retmax": max_results,
        "retmode": "json",
    }
    response = requests.get(BASE + "esearch.fcgi", params=params, timeout=30)
    response.raise_for_status()  # stops with an error if the request failed
    result = response.json()["esearchresult"]
    return int(result["count"]), result["idlist"]

if __name__ == "__main__":
    searches = {
        "exercise": '"Exercise"[MeSH] AND "Neoplasms"[MeSH]',
        "mindfulness": '"Mindfulness"[MeSH] AND "Neoplasms"[MeSH]',
        "curcumin": '"Curcumin"[MeSH] AND "Neoplasms"[MeSH]',
    }

    for name, term in searches.items():
        total, pmids = search_pubmed(term)
        print(f"{name}: {total} total matches, got {len(pmids)} IDs")
        time.sleep(0.5)