from can import Message
from can.io.generic import MessageReader
from pathlib import Path
from typing import BinaryIO, Dict, Optional, Union


class CanMsgExtension(Message):
    ...


class LogFile(MessageReader):
    def __init__(self, file: Union[BinaryIO, Path, str], passwords: Optional[Dict] = None):
        ...

    def get_metadata(self) -> Dict[str, Dict[str, str]]:
        ...

    ...
