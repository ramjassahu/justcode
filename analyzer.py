import re
import pandas as pd
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

vader_analyzer = SentimentIntensityAnalyzer()

def get_ensemble_sentiment(comment):
    """Analyzes a comment using an ensemble of VADER and TextBlob."""
    vader_score = vader_analyzer.polarity_scores(comment)['compound']
    textblob_score = TextBlob(comment).sentiment.polarity
    combined_score = (vader_score + textblob_score) / 2
    
    if combined_score > 0.05: return 'positive'
    if combined_score < -0.05: return 'negative'
    return 'neutral'

def analyze_data(df, competitors, mention_weights):
    """Main function to analyze the scraped data for mentions, sentiment, and SoV."""
    if df.empty: return None, None

    results = []
    for _, row in df.iterrows():
        video_results = {'video_id': row['video_id'], 'keyword': row['keyword']}
        video_results['engagement_score'] = row['views'] + (row['likes'] * 5) + (row['comment_count'] * 10)
        
        text_title = row['title'].lower()
        text_desc = row['description'].lower()
        
        for brand in competitors.keys():
            video_results[f'{brand}_mention_score'] = 0
            video_results[f'{brand}_positive_mentions'] = 0
            video_results[f'{brand}_neutral_mentions'] = 0
            video_results[f'{brand}_negative_mentions'] = 0

        for brand, patterns in competitors.items():
            if any(re.search(p, text_title) for p in patterns): video_results[f'{brand}_mention_score'] += mention_weights['title']
            if any(re.search(p, text_desc) for p in patterns): video_results[f'{brand}_mention_score'] += mention_weights['description']

        for comment in row['comments']:
            sentiment_label = get_ensemble_sentiment(comment)
            text_comment = comment.lower()
            for brand, patterns in competitors.items():
                if any(re.search(p, text_comment) for p in patterns):
                    video_results[f'{brand}_mention_score'] += mention_weights['comments']
                    if sentiment_label == 'positive': video_results[f'{brand}_positive_mentions'] += 1
                    elif sentiment_label == 'negative': video_results[f'{brand}_negative_mentions'] += 1
                    else: video_results[f'{brand}_neutral_mentions'] += 1
        results.append(video_results)
        
    analysis_df = pd.DataFrame(results)

    final_metrics = {}
    for keyword in df['keyword'].unique():
        keyword_df = analysis_df[analysis_df['keyword'] == keyword]
        
        brand_weighted_scores = {brand: (keyword_df[f'{brand}_mention_score'] * np.log1p(keyword_df['engagement_score'])).sum() for brand in competitors}
        total_weighted_score = sum(brand_weighted_scores.values())
        
        e_sov = {brand: (score / total_weighted_score * 100) if total_weighted_score > 0 else 0 for brand, score in brand_weighted_scores.items()}

        sopv = {}
        for brand in competitors:
            positive = keyword_df[f'{brand}_positive_mentions'].sum()
            total_mentions = positive + keyword_df[f'{brand}_neutral_mentions'].sum() + keyword_df[f'{brand}_negative_mentions'].sum()
            sopv[brand] = (positive / total_mentions * 100) if total_mentions > 0 else 0
        
        final_metrics[keyword] = {'e_sov': e_sov, 'sopv': sopv}
        
    return analysis_df, final_metrics