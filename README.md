
## Dataset

   I got the dataset from a kaggle project https://www.kaggle.com/datasets/utkarshx27/movies-dataset?resource=download. It was a large data set and I cut it down to 500 movies to fit the requirements. There are no extra steps to load the data set as it is in the repo. 

### Setup

   I use python version 11 but it does not require a specfic version. I have included a requirements.txt file that has the pip requirements.
   - Run the requirements.txt file with the command `pip install -r requirements.txt`


## Running

   In order to run the code it uses the system arguments
   - To run it use python3 recommend.py "then include the descrption"
   - It has error catching if more arguments are added



## Results
   
   
   ```
   jacobgino@MacBook-Pro lumaa-spring-2025-ai-ml % python3 recommend.py "I love thrilling action movies set in space, with a comedic twist."

   Recommendations for query: "I love thrilling action movies set in space, with a comedic twist."


   Title: Gravity | Similarity: 0.0843
   Title: Lost in Space | Similarity: 0.0760
   Title: Mad Max: Fury Road | Similarity: 0.0704
   Title: Up | Similarity: 0.0677
   Title: Treasure Planet | Similarity: 0.0669
   ```

   `







