import google.generativeai as genai
import os
import logging


def remove_first_and_last_lines(text):
    """
    Removes the first and last lines from a multi-line string.

    Args:
        text (str): The input multi-line string.

    Returns:
        str: The modified string with the first and last lines removed.
    """
    # Split the text into lines
    lines = text.splitlines()

    # Remove the first and last lines
    if len(lines) > 2:
        lines = lines[1:-1]
    else:
        return ""  # Return an empty string if there aren't enough lines

    # Join the remaining lines back into a single string
    return "\n".join(lines)


def summarize_paper(pdf_path):
    """Generate a concise summary for the paper."""
    # Extract text from the PDF (simplified example)
    from PyPDF2 import PdfReader
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages[:5]:  # Limit to first 5 pages
        text += page.extract_text()

    # Use Gemini API for summarization
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    pdf_file = genai.upload_file(pdf_path)
    summary_response = model.generate_content(
        ["Give me a summary of this pdf file in 250 words or less.", pdf_file])

    # Use Gemini API to generate results table
    results_table_response = model.generate_content(
        ["Identify and extract the main results table from the file. If there is no results table return \"none\". If there are multiple tables, extract the one that appears to be the primary results table. Return the response in csv.", pdf_file])

    # Remove first and last lines from results table because it seems to return
    # text with backticks. Probably markdown.
    return summary_response.text, remove_first_and_last_lines(results_table_response.text)
