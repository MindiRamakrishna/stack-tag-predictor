# StackOverflow Tag Predictor (Top 10 Tags)

This project performs multi-label classification to predict tags associated with StackOverflow questions using title and body text.

## Steps:
1. Load and clean question data.
2. Extract top 10 most frequent tags.
3. Vectorize the text with TF-IDF.
4. Train a multi-label classifier using Logistic Regression.

## Files:
- `Questions.xlsx`, `Tags.xlsx`, `Answers.xlsx` (optional)
- `tag_predictor.py`: main script
- `requirements.txt`: dependencies
  ## 📁 Data Files Note

The original dataset files (`Questions.xlsx`, `Answers.xlsx`, `Tags.xlsx`) were not included in this repository due to GitHub’s 100 MB file size limit.

You may request access to the dataset if needed for reproduction or further analysis.


## 🛠️ How to Run:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the tag prediction script
python tag_predictor.py

