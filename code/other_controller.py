import random

from localstack_christmas_countdown.models.joke import Joke  # noqa: E501

jokes = [
    Joke(question="Why is Santa using LocalStack?", answer="Because he's working in the clouds!")
]


def joke_get():  # noqa: E501
    """Get a Christmas joke

    Returns a joke object (question and answer). # noqa: E501


    :rtype: Union[Joke, Tuple[Joke, int], Tuple[Joke, int, Dict[str, str]]
    """
    return random.choice(jokes)


def jokes_get():  # noqa: E501
    """Get all available Christmas jokes

    Returns an array of joke objects. # noqa: E501


    :rtype: Union[List[Joke], Tuple[List[Joke], int], Tuple[List[Joke], int, Dict[str, str]]
    """
    return jokes
