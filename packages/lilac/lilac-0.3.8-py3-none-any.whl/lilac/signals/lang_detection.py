"""Language detection of a document."""
import re
from typing import Any, ClassVar, Optional

from pydantic import Field as PydanticField
from typing_extensions import override

from ..schema import Field, Item, SignalInputType, field, span
from ..signal import TextSignal
from ..tasks import TaskExecutionType

LANG_CODE = 'lang_code'
TEXT_LEN_THRESHOLD = 40


class LangDetectionSignal(TextSignal):
  """Detects the language code in text.

  \

  Supports 55 languages returning their
  [ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
  """

  name: ClassVar[str] = 'lang_detection'
  display_name: ClassVar[str] = 'Language detection'

  input_type: ClassVar[SignalInputType] = SignalInputType.TEXT

  split_by_paragraph: bool = PydanticField(
    default=False, description='Compute language scores for each paragraph.'
  )

  local_batch_size: ClassVar[Optional[int]] = 1024
  local_parallelism: ClassVar[int] = -1
  local_strategy: ClassVar[TaskExecutionType] = 'processes'

  def _detect(self, text: str, langdetect: Any) -> Optional[str]:
    if len(text) < TEXT_LEN_THRESHOLD:
      return 'TOO_SHORT'
    try:
      return langdetect.detect(text)
    except langdetect.LangDetectException:
      return None

  @override
  def setup(self) -> None:
    try:
      import langdetect

      langdetect.DetectorFactory.seed = 42  # For consistent results.
    except ImportError:
      raise ImportError(
        'Could not import the "langdetect" python package. '
        'Please install it with `pip install langdetect`.'
      )

  @override
  def fields(self) -> Field:
    if self.split_by_paragraph:
      return field(fields=[field('string_span', fields={LANG_CODE: 'string'})])
    return field('string')

  @override
  def compute(self, data: list[str]) -> list[Optional[Item]]:
    import langdetect

    # Split on paragraphs.
    split_symbol = re.compile('(\r?\n){2,}')
    results: list[Optional[Item]] = []

    for text in data:
      if not self.split_by_paragraph:
        results.append(self._detect(text, langdetect))
        continue

      prev_end = 0
      result: list[Item] = []
      for m in split_symbol.finditer(text):
        start, end = m.span()
        text_span = text[prev_end:start]
        text_span = text_span.strip()
        if text_span:
          lang_code = self._detect(text_span, langdetect)
          if lang_code:
            result.append(span(prev_end, start, {LANG_CODE: lang_code}))
        prev_end = end

      # Process the last chunk.
      text_span = text[prev_end:]
      if text_span.strip():
        lang_code = self._detect(text_span, langdetect)
        if lang_code:
          result.append(span(prev_end, len(text), {LANG_CODE: lang_code}))

      results.append(result)

    return results
