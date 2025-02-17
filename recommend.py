import sys
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_dataset(csv_file):
    #Load the dataset from a CSV file
    try:
        df = pd.read_csv(csv_file)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        sys.exit(1)

def preprocess_data(df):
    #Combine the 'overview' and 'keywords' columns into a single text column, and add more weight to the keywords
    df['text'] = df['overview'].astype(str) + " " + (df['keywords'].astype(str) * 2)
    return df

def build_tfidf_matrix(texts):
    #Build the TF-IDF matrix from the text data
    vectorizer = TfidfVectorizer(
        stop_words='english',
        max_df=0.8,    
        ngram_range=(1, 2)
    )
    matrix = vectorizer.fit_transform(texts)
    return matrix, vectorizer

def get_recommendations(query, df, tfidf_matrix, vectorizer, topn=5):

    # Transform the query into the same TF-IDF space
    query_tfidf = vectorizer.transform([query])

    # Compute cosine similarity between the query and all documents
    cosineSim = cosine_similarity(query_tfidf, tfidf_matrix).flatten()

    # Get the indices of the top N most similar documents
    topIndexes = cosineSim.argsort()[-topn:][::-1]

    # Return the top N recommendations
    recommendations = []
    for i in topIndexes:
        recommendations.append({
            'title': df.iloc[i]['title'],
            'similarity': cosineSim[i]
        })
    return recommendations

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("pytho3n recommend.py \"Your movie description query\"")
        sys.exit(1)
    
  
    query = sys.argv[1]
    df = load_dataset('movie_dataset.csv')
    df = preprocess_data(df)
    

    matrix, vectorizer = build_tfidf_matrix(df['text'])
    recommendations = get_recommendations(query, df, matrix, vectorizer, topn=5)
    
    print(f"\nRecommendations for query: \"{query}\"\n")
    for i in recommendations:
        print(f"Title: {i['title']} | Similarity: {i['similarity']:.4f}")
    print("\n")
