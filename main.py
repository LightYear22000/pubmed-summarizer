from downloader.pdf_downloader import download_paper
from summarizer.paper_summarizer import summarize_paper
from extractor.table_extractor import extract_main_table
from utils.file_utils import ensure_directory, save_text, save_csv
from concurrent.futures import ThreadPoolExecutor
from config import DATA_DIR, PAPER_URLS, SINGLE_URL_FOR_TEST, MAX_THREADS

import os
import logging

# Set up directories
papers_dir = os.path.join(DATA_DIR, "papers")
summaries_dir = os.path.join(DATA_DIR, "summaries")
tables_dir = os.path.join(DATA_DIR, "tables")


def download_paper_and_summarize(url):
    # Download paper
    pdf_path = download_paper(url, papers_dir)

    # Summarize and generate results table from paper
    return summarize_paper(pdf_path)


def process_url(url):
    logging.info(f"Processing: {url}")
    pmid = url.split("/")[-2]  # Extract PMID from URL

    try:
        # Summarize and generate results table from paper
        summary, table = download_paper_and_summarize(url)

        # Write summary to file
        summary_path = os.path.join(summaries_dir, f"{pmid}_summary.txt")
        save_text(summary, summary_path)

        logging.info(f"Genrated summary and results table for {pmid}")

        # Write results to file
        if table:
            table_path = os.path.join(tables_dir, f"{pmid}_table.csv")
            save_csv(table, table_path)

    except Exception as e:
        logging.error(f"Error processing {url}: {e}")


def main():
    # Ensure directories exist
    ensure_directory(papers_dir)
    ensure_directory(summaries_dir)
    ensure_directory(tables_dir)

    # Download PDF for each URL and generate summary
    # Use ThreadPoolExecutor for parallel processing of URLs
    with ThreadPoolExecutor(MAX_THREADS) as executor:
        # Submit tasks to the executor
        results = list(executor.map(process_url, PAPER_URLS))


if __name__ == "__main__":
    main()
