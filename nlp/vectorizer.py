from sklearn.feature_extraction.text import TfidfVectorizer


class NewsVectorizer:

    def __init__(
        self,
        max_features=5000
    ):

        self.vectorizer = TfidfVectorizer(
            max_features=max_features,
            ngram_range=(1, 2),
            min_df=1
        )


    def fit(self, texts):

        self.vectorizer.fit(texts)


    def transform(self, texts):

        return self.vectorizer.transform(texts)


    def fit_transform(self, texts):

        return self.vectorizer.fit_transform(texts)


    def get_feature_names(self):

        return self.vectorizer.get_feature_names_out()