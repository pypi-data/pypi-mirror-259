import pytest
from embed_text_reducer import TextReducer
from unittest.mock import patch, MagicMock


@pytest.fixture
def text_reducer():
    return TextReducer()


# Test splitting text into sentences
def test_split_into_sentences(text_reducer):
    text = "This is the first sentence. This is the second sentence."
    sentences = text_reducer._split_into_sentences(text)
    assert len(sentences) == 2
    assert sentences[0] == "This is the first sentence"
    assert sentences[1] == "This is the second sentence"


# Test filtering short sentences
def test_filter_short_sentences(text_reducer):
    sentences = ["Short", "This is a longer sentence."]
    min_tokens = 3  # Assuming the tokenizer counts "This is a" as 3 tokens
    filtered_sentences = text_reducer._filter_short_sentences(
        sentences,
        min_tokens
    )
    assert len(filtered_sentences) == 1
    assert filtered_sentences[0] == "This is a longer sentence."
