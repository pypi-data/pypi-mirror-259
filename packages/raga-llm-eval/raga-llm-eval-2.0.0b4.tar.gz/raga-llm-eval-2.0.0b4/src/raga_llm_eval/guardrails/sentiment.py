import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


class Sentiment:
    """
    A sentiment scanner based on the NLTK's SentimentIntensityAnalyzer. It is used to detect if a prompt
    has a sentiment score lower than the threshold, indicating a negative sentiment.
    """

    def __init__(self, response: str, threshold: float = -0.1):
        """
        Initializes Sentiment with a threshold and a chosen lexicon.

        Parameters:
            prompt (str): The prompt to scan for sentiment.
           threshold (float): Threshold for the sentiment score (from -1 to 1). Default is -0.1.

        Raises:
           None.
        """

        nltk.download("vader_lexicon")
        self.response = response
        self._sentiment_analyzer = SentimentIntensityAnalyzer()
        self._threshold = threshold

    def run(self) -> (str, bool, float):  # type: ignore
        result = {
            "response": self.response,
            "is_passed": True,
            "score": 0.0,
        }
        
        sentiment_score = self._sentiment_analyzer.polarity_scores(self.response)
        sentiment_score_compound = sentiment_score["compound"]
        if sentiment_score_compound > self._threshold:
            result["is_passed"] = True
            result["score"] = 0.0
            result["sanitized_prompt"] = self.response

            return result

        # Normalize such that -1 maps to 1 and threshold maps to 0
        score = round((sentiment_score_compound - (-1)) / (self._threshold - (-1)), 2)

        result["is_passed"] = False
        result["score"] = score
        result["sanitized_prompt"] = self.response
        return result
