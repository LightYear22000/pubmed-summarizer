from downloader.pdf_downloader import download_paper
from summarizer.paper_summarizer import summarize_paper
from extractor.table_extractor import extract_main_table
from utils.file_utils import ensure_directory, save_text, save_csv
from config import DATA_DIR, PAPER_URLS, SINGLE_URL_FOR_TEST

import os


def main():
    # Set up directories
    papers_dir = os.path.join(DATA_DIR, "papers")
    summaries_dir = os.path.join(DATA_DIR, "summaries")
    tables_dir = os.path.join(DATA_DIR, "tables")
    ensure_directory(papers_dir)
    ensure_directory(summaries_dir)
    ensure_directory(tables_dir)

    # Download PDF for each URL and generate summary

    for url in PAPER_URLS:
        print(f"Processing: {url}")
        pmid = url.split("/")[-2]  # Extract PMID from URL

        try:
            # Download paper
            pdf_path = download_paper(url, papers_dir)
            print(f"pdf_path: {pdf_path}")

            # Summarize and generate results table from paper
            summary, table = summarize_paper(pdf_path)

            # Write summary to file
            summary_path = os.path.join(summaries_dir, f"{pmid}_summary.txt")
            save_text(summary, summary_path)

            print(f"Genrated summary and results table for {url}")

            # Write results to file
            if table:
                table_path = os.path.join(tables_dir, f"{pmid}_table.csv")
                save_csv(table, table_path)

        except Exception as e:
            print(f"Error processing {url}: {e}")


if __name__ == "__main__":
    main()
