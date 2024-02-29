"""Registers all available dataset formats."""

from ..dataset_format import register_dataset_format
from .openai_json import OpenAIConversationJSON, OpenAIJSON
from .openchat import OpenChat
from .sharegpt import ShareGPT


def register_default_formats() -> None:
  """Register all the default dataset formats."""
  register_dataset_format(ShareGPT)
  register_dataset_format(OpenChat)
  register_dataset_format(OpenAIJSON)
  register_dataset_format(OpenAIConversationJSON)
