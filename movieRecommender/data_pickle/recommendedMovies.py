import pickle
import pandas as pd
import os
import numpy as np
import random
#trending page
def build_chart(genre, percentile=0.85):
    curr_dir = os.getcwd()
    with open(curr_dir+'\movieRecommender\data_pickle\\trending.pkl' , 'rb') as obj:
      gen_md = pickle.load(obj)
    df = gen_md[gen_md['genre'] == genre]
    vote_counts = df[df['vote_count'].notnull()]['vote_count'].astype('int')
    vote_averages = df[df['vote_average'].notnull()]['vote_average'].astype('int')
    C = vote_averages.mean()
    m = vote_counts.quantile(percentile)
    
    qualified = df[(df['vote_count'] >= m) & (df['vote_count'].notnull()) & (df['vote_average'].notnull())][['title', 'year', 'vote_count', 'vote_average', 'popularity']]
    qualified['vote_count'] = qualified['vote_count'].astype('int')
    qualified['vote_average'] = qualified['vote_average'].astype('int')
    
    qualified['wr'] = qualified.apply(lambda x: (x['vote_count']/(x['vote_count']+m) * x['vote_average']) + (m/(m+x['vote_count']) * C), axis=1)
    qualified = qualified.sort_values('wr', ascending=False).head(100)
    movies = qualified['title'].tolist()
    movies = list(movies)
    random_movies = []
    try:
        random_movies = random.sample(movies, k=1)
    except:
        pass
    return random_movies

def build_chart_2(genre, percentile=0.85):
    curr_dir = os.getcwd()
    with open(curr_dir+'\movieRecommender\data_pickle\\trending.pkl' , 'rb') as obj:
      gen_md = pickle.load(obj)
    df = gen_md[gen_md['genre'] == genre]
    vote_counts = df[df['vote_count'].notnull()]['vote_count'].astype('int')
    vote_averages = df[df['vote_average'].notnull()]['vote_average'].astype('int')
    C = vote_averages.mean()
    m = vote_counts.quantile(percentile)
    
    qualified = df[(df['vote_count'] >= m) & (df['vote_count'].notnull()) & (df['vote_average'].notnull())][['title', 'year', 'vote_count', 'vote_average', 'popularity']]
    qualified['vote_count'] = qualified['vote_count'].astype('int')
    qualified['vote_average'] = qualified['vote_average'].astype('int')
    
    qualified['wr'] = qualified.apply(lambda x: (x['vote_count']/(x['vote_count']+m) * x['vote_average']) + (m/(m+x['vote_count']) * C), axis=1)
    qualified = qualified.sort_values('wr', ascending=False).head(100)
    movies = qualified['title'].tolist()
    movies = list(movies)
    random_movies = []
    try:
        random_movies = random.sample(movies, k=5)
    except:
        pass
    return random_movies

def get_recommendations(id ,t, num):
    try:
        curr_dir = os.getcwd()
        with open(curr_dir+'\movieRecommender\data_pickle\\moviedata.pkl' , 'rb') as obj:
            df = pickle.load(obj)
        title = df.loc[df['imdb_id'] == id, 'title'].iloc[0]
        print(title)
        with open(curr_dir+'\movieRecommender\data_pickle\\title_cosine.pkl' , 'rb') as obj:
            titles = pickle.load(obj)
        with open(curr_dir+'\movieRecommender\data_pickle\\indicies_cosine.pkl' , 'rb') as obj:
            indices = pickle.load(obj)
        with open(curr_dir+'\movieRecommender\data_pickle\\cosin_sim.pkl' , 'rb') as obj:
            cosine_sim = pickle.load(obj)
        idx = indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        #sim_scores = [(i, np.sum(row)) for i, row in enumerate(cosine_sim)]
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:31]
        movie_indices = [i[0] for i in sim_scores]
        return titles.iloc[movie_indices].head(6)
    except:
        return build_chart_2('Adventure')
    
