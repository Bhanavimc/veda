from transformers import pipeline

def summarize_text(content):
    summarizer = pipeline('summarization')
    summary = summarizer(content, max_length=50, min_length=20, do_sample=False)
    return summary[0]['summary_text']
