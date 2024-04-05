from django.shortcuts import render , redirect
import requests
from django.http import HttpResponse
from .forms import ReviewForm
from .models import MovieReviewModel
from movieRecommender.MovieTemplate import getMovie , getMovieDetails , get_movie_area
from .data_pickle.recommendedMovies import get_recommendations , build_chart
from BASE_VAR import OMDB_API , OMDB_KEY

def movie_home(request):
    
    Genre=['Animation' , 'Comedy' , 'Fmaily' , 'Adventure'
           ,'Fantasy' , 'Romance' , 'Drama' , 'Action' , 
           'Thriller' , 'Horror' , 'History' , 'Crime']
    
    Movie_Data = {}
    
    for g in Genre:
        h = build_chart(g)
        s = []
        print(h)
        for k in h:
            res =  requests.get('https://www.omdbapi.com/?i=tt3896198&apikey='+OMDB_KEY+'&t='+str(k))
            
            tempdata = res.json()
            #list
            if (tempdata['Response']=='True'):
                moviedata = tempdata
                moviedata = get_movie_area(moviedata)
                s.append(moviedata)
        Movie_Data[g] = s
    
    return render(request , 'movieRecommender/index.html' , {
        "data":Movie_Data
    })

def movie_search(request):
    
    #Get Quaries from search box
    query = request.GET.get('q')
        
    if query:
       data =  requests.get('https://www.omdbapi.com/?i=tt3896198&apikey='+OMDB_KEY+'&s='+query)
    else:
        return render(request , 'movieRecommender/error.html',{
        "data":"Please Enter A Query"
        })
    
    tempdata = data.json()
    #list
    if (tempdata['Response']=='True'):
        moviedata = tempdata['Search']
        moviedata = getMovie(moviedata)
        return render(request , 'movieRecommender/results.html',{
        "data":moviedata
        })
        
    else:
        return render(request , 'movieRecommender/error.html',{
        "message":"No Items Found"
        })

def movie_view_details(request):
    #Get Quaries from search box
    value = request.GET.get('title')
    query = ''
    for h in range(len(value)):
        if value[h] == '$':
            break
        else:
            query += value[h]
    id = value[h+1:]
    form = ReviewForm()
    RatingValue = 50
    recc_data = get_recommendations(id, query , 10)
    if (request.method=='POST' and request.user):
        form = ReviewForm(request.POST)
        if (MovieReviewModel.objects.filter(user=request.user,movietitle=query)):
            MovieReviewModel.objects.filter(user=request.user,movietitle=query).update(Rating=request.POST['Rating'])
        elif form.is_valid():
            instance = form.save(commit = False)
            instance.user = request.user
            instance.movietitle = query
            instance.save()
            return redirect('/movie_area/movie/?title='+query)
    
    try:
        if (MovieReviewModel.objects.filter(user=request.user,movietitle=query)):
            RatingValue = MovieReviewModel.objects.filter(user=request.user,movietitle=query)[0].Rating    
    except:
        pass
    
    #print(recc_data)
    
    if query:
       data =  requests.get('https://www.omdbapi.com/?i=tt3896198&apikey='+OMDB_KEY+'&t='+query)
    else:
        return render(request , 'movieRecommender/error.html',{
        "data":"No Movie Found"
        })
    recoomaendation_data = []
    for k in recc_data:
        
        res =  requests.get('https://www.omdbapi.com/?i=tt3896198&apikey='+OMDB_KEY+'&t='+str(k))
        
        tempsdata = res.json()
        #list
        if (tempsdata['Response']=='True'):
            moviedata = tempsdata
            moviedata = get_movie_area(moviedata)
            recoomaendation_data.append(moviedata)
        
    tempdata = data.json()
    #list
    if (tempdata['Response']=='True'):
        moviedata = tempdata
        moviedata = getMovieDetails(moviedata)
        return render(request , 'movieRecommender/moviedetails.html',{
        "data":moviedata,
        "title":query,
        "RatingValue":RatingValue,
        "rec_data":recoomaendation_data
        })
        
    else:
        return render(request , 'movieRecommender/error.html',{
        "message":"No Items Found"
        })
    
    
