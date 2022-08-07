import fuzzywuzzy
from fuzzywuzzy import process
import chardet




def replace_matches_in_column(df, column, string_to_match, min_ratio = 47):
    
    """Example: Replace close matches to "southkorea" with "south korea":

    replace_matches_in_column(df=professors, column='Country', string_to_match="south korea")

    """

    
    # get a list of unique strings
    strings = df[column].unique()
    
    # get the top 10 closest matches to our input string
    matches = fuzzywuzzy.process.extract(string_to_match, strings, 
                                         limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

    # only get matches with a ratio > 90
    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]

    # get the rows of all the close matches in our dataframe
    rows_with_matches = df[column].isin(close_matches)

    # replace all rows with close matches with the input matches 
    df.loc[rows_with_matches, column] = string_to_match
    
    # let us know the function's done
    print("All done!")
    
    
def busca_similares(columna_unique,cantidad):
    """Example: 
    Input: Columna de un dataframe al que se le ha aplicado el método .unique()
           y una "cantidad" de coincidencias a mostrar por palabra.  

    Output: Las strings más cercanas entre sí de toda la columna. 

    """    
    
    
    for i in range(len(columna_unique)):
        #print(df["colonia"].unique()[i])
        matches = fuzzywuzzy.process.extract(columna_unique[i], columna_unique, limit=cantidad, scorer=fuzzywuzzy.fuzz.token_sort_ratio)
        print(i,matches)