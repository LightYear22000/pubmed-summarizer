# How to run?
- We use Gemini to generate summaries and  reports. So, to run this you need an API Key. "Get API key" on  [Google AI Studio](aistudio.google.com/app/apikey).
- Export the created API Key as environment variable
```
export API_KEY="your-api-key"
```
- Trigger the file generation process using the following command:
```
python3 main.py
```
- Check the summary and tables generated in ```data/summaries``` and ```data/tables``` directories respectively.

# Limitations
- data folder has only one paper at the moment. Auto-downloading of papers is not possible.
- Multiple papers are not concurrently processed. 