import pandas as pd
from collections import defaultdict

def find_common_words(tdm):

    finding_most_common_words_dict = defaultdict(int)
    
    # columns in tdm are # of documents
    # want this for showing word to doc pct

    num_docs = len(tdm.columns)

    for col in tdm.columns:
        
        top_20 = tdm[col].sort_values(ascending=False).head(20)

        for word, count in top_20.items():

            # check if count > 0 to verify only counting words that are actually in review

            if count > 0:

                finding_most_common_words_dict[word] += 1

    return {word: count/num_docs for word, count in sorted(finding_most_common_words_dict.items(), key=lambda item: item[1], reverse=True)}
