from typing import Tuple, List
import tiktoken
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('TextSimplifier')


class TextProcessingError(Exception):
    """
    Custom exception class for handling errors
    during text processing operations.
    """


class TextReducer:
    """
    A class for simplifying text by filtering and summarizing based
    on relevance to a given query.
    """

    def __init__(
        self,
        tokenizer_model: str = 'gpt-3.5-turbo',
        transformer_model: str = 'all-MiniLM-L6-v2'
    ):
        """
        Initializes the TextSimplifier class with specified tokenizer
        and transformer models.

        Args:
            tokenizer_model (str): The model name for the tokenizer.
            transformer_model (str): The model name for sentence transformer.
        """
        self.tokenizer = self._initialize_tokenizer(tokenizer_model)
        self.transformer = self._initialize_transformer(transformer_model)

    def _initialize_tokenizer(self, model_name: str):
        """
        Initializes the tokenizer based on the specified model name.

        Args:
            model_name (str): The model name for the tokenizer.

        Returns:
            The initialized tokenizer.
        """
        try:
            return tiktoken.encoding_for_model(model_name)
        except Exception as e:
            raise TextProcessingError(
                f"Failed to initialize tokenizer with model {model_name}"
            ) from e

    def _initialize_transformer(self, model_name: str):
        """
        Initializes the transformer based on the specified model name.

        Args:
            model_name (str): The model name for the transformer.

        Returns:
            SentenceTransformer: The initialized transformer.
        """
        try:
            return SentenceTransformer(model_name)
        except Exception as e:
            raise TextProcessingError(
                f"Failed to initialize transformer with model {model_name}"
            ) from e

    def _split_into_sentences(self, text: str) -> List[str]:
        """
        Splits the given text into individual sentences.

        Args:
            text (str): The text to be split.

        Returns:
            List[str]: A list of sentences extracted from the text.
        """
        return [sentence.strip() for sentence in text.split('.') if sentence]

    def _filter_short_sentences(
        self,
        sentences: List[str],
        min_tokens: int
    ) -> List[str]:
        """
        Filters out sentences shorter than a specified number of tokens.

        Args:
            sentences (List[str]): The list of sentences to filter.
            min_tokens (int): The minimum number of tokens a sentence.

        Returns:
            List[str]: The filtered list of sentences.
        """
        return [
            sentence
            for sentence in sentences
            if self._count_tokens(sentence) >= min_tokens
        ]

    def _count_tokens(self, sentence: str) -> int:
        """
        Counts the number of tokens in a given sentence.

        Args:
            sentence (str): The sentence to count tokens in.

        Returns:
            int: The number of tokens found in the sentence.
        """
        return len(self.tokenizer.encode(sentence))

    def _compute_cosine_similarity(self, query: str) -> np.ndarray:
        """
        Computes the cosine similarity between the query
        and each sentence embedding.

        Args:
            query (str): The query sentence to compare against the text.

        Returns:
            np.ndarray: An array of cosine similarity scores.
        """
        try:
            query_embedding = self.transformer.encode([query])
            return cosine_similarity(self.embeddings, query_embedding)
        except Exception as e:
            raise TextProcessingError(
                "Failed to compute cosine similarity"
            ) from e

    def _format_summary(self, sentences: List[str]) -> str:
        """
        Formats the selected sentences into a summary string.

        Args:
            sentences (List[str]): The sentences to format into a summary.

        Returns:
            str: The formatted summary.
        """
        return '. '.join(sentences).strip().replace('\n', '')

    def fit(self, text: str, min_tokens_per_sentence: int = 0):
        """
        Prepares the text for simplification by encoding
        and filtering sentences.

        Args:
            text (str): The text to be simplified.
            min_tokens_per_sentence (int, optional)
        """
        sentences = self._split_into_sentences(text)
        if min_tokens_per_sentence:
            sentences = self._filter_short_sentences(
                sentences,
                min_tokens_per_sentence
            )
        self.embeddings = self.transformer.encode(sentences)
        self.filtered_sentences = sentences

    def find_relevant(
        self,
        query: str,
        max_tokens: int,
        min_similarity: float = 0.1
    ) -> Tuple[str, int]:
        """
        Finds and formats sentences from the text relevant to the given query.

        Args:
            query (str): The query to find relevant sentences for.
            max_tokens (int): The maximum number of tokens for the summary.
            min_similarity (float, optional): The minimum similarity score

        Returns:
            Tuple[str, int]: A tuple containing the summary of relevant
            sentences and the total number of tokens used.
        """
        accumulated_tokens = 0
        selected_sentences = []
        try:
            similarities = self._compute_cosine_similarity(query).flatten()
        except TextProcessingError:
            raise

        sorted_indices = np.argsort(-similarities)

        for index in sorted_indices:
            if similarities[index] < min_similarity:
                break

            sentence = self.filtered_sentences[index]
            sentence_tokens = self._count_tokens(sentence)
            if accumulated_tokens + sentence_tokens > max_tokens:
                continue

            accumulated_tokens += sentence_tokens
            selected_sentences.append(sentence)

        return self._format_summary(selected_sentences), accumulated_tokens
