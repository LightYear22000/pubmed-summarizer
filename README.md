# How to run?
- We use Gemini to generate summaries and  reports. So, to run this you need an API Key. "Get API key" on  [Google AI Studio](aistudio.google.com/app/apikey).
- Export the created API Key as environment variable
```
export API_KEY="your-api-key"
```
- Create an NCBI API Key as per instructions in [this page](https://ncbiinsights.ncbi.nlm.nih.gov/2017/11/02/new-api-keys-for-the-e-utilities/) and export it using the following command:
```
export NCBI_API_KEY="your-ncbi-api-key"
```
- Trigger the summar and results generation process using the following command:
```
python3 main.py
```
- Check the summary and tables generated in ```data/summaries``` and ```data/tables``` directories respectively.

# Limitations
- data folder has only one hardcoded paper at the moment. Auto-downloading of papers is not possible.
- Multiple papers are not concurrently processed. 