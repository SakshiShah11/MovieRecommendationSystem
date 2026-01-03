# Movie Recommendation System (Streamlit Web Application)

This project implements a **content-based movie recommendation system** using **Python** and **Streamlit**.  
The application recommends movies similar to a selected title by analyzing movie metadata such as genres, keywords, cast, crew, and plot overview.

## 1. Introduction

Recommender systems play a crucial role in modern digital platforms by helping users discover relevant content efficiently.  
This project focuses on a **content-based filtering approach**, where recommendations are generated based on the similarity between movies rather than user behavior or ratings.

The system is implemented as an interactive web application using Streamlit, making it accessible and easy to use.


## 2. Dataset Description

The project uses the **TMDB 5000 Movies Dataset**, which consists of two main files:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

These datasets contain detailed metadata for each movie, including:
- Movie ID and title
- Plot overview
- Genres
- Keywords
- Cast details
- Crew details

The datasets are merged using the movie title to form a single unified dataset.


## 3. Methodology

### 3.1 Data Collection and Merging
The movies and credits datasets are loaded and merged to combine all relevant information for each movie into a single dataframe.

### 3.2 Feature Selection
The following features are selected as they best represent the content of a movie:
- **Overview**: Describes the movie plot.
- **Genres**: Indicates the thematic category of the movie.
- **Keywords**: Captures important concepts related to the movie.
- **Cast**: Top three lead actors are selected.
- **Crew**: Director information is extracted.

These features collectively define the creative and narrative aspects of a movie.


### 3.3 Data Cleaning and Preprocessing
To ensure consistency and accuracy, the following preprocessing steps are applied:

- Removal of rows with missing values
- Conversion of JSON-like strings into Python lists
- Extraction of the top three cast members
- Extraction of the director from the crew list
- Tokenization of the plot overview
- Removal of spaces in multi-word entities (e.g., "Science Fiction" → "ScienceFiction")
- Conversion of all text to lowercase


### 3.4 Feature Engineering
All processed features are combined into a single column called **`tags`**:


The `tags` column represents the complete content profile of a movie and is used for similarity computation.


### 3.5 Text Vectorization
The textual data in the `tags` column is transformed into numerical vectors using **Bag-of-Words vectorization**.

Each movie is represented as a vector where:
- Each dimension corresponds to a word in the vocabulary
- Values represent word frequencies

This allows mathematical comparison between movies.


### 3.6 Similarity Computation
**Cosine similarity** is used to measure similarity between movie vectors.

- A similarity score closer to 1 indicates high similarity
- A score closer to 0 indicates low similarity

A similarity matrix is computed where each movie is compared against every other movie.


### 3.7 Recommendation Generation
When a user selects a movie:
1. The similarity scores for the selected movie are retrieved
2. Movies are sorted in descending order of similarity
3. The top N most similar movies are recommended (excluding the selected movie)


### 3.8 Web Application Integration
The recommendation logic is integrated into a Streamlit web application:
- Users select a movie title from a dropdown menu
- Recommendations are generated in real time
- Results are displayed in a simple and intuitive interface



## 4. Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn


## 5. Installation and Setup

### Clone the Repository
```bash
git clone https://github.com/sakshishah02/MovieRecommendationSystemWeb.git
cd MovieRecommendationSystemWeb
