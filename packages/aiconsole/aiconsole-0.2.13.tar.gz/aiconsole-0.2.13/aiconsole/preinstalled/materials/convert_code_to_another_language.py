"""
Use this function to convert code to another language, do not use any other method of doing this.

1. If a directory is specified, list and convert all the files in the directory structure recursively.
2. For each file run this code and attach the output at the begining of the file:

example of code:
```python
convert_language(FILE_PATH, DESIRED_LANGUAGE)
```
"""

import logging
import os
from typing import cast

import litellm  # type: ignore

_log = logging.getLogger(__name__)


def convert_language(file_name, desired_language):
    file_contents = open(file_name, encoding="utf8", errors="replace").read()

    completion: litellm.ModelResponse = cast(
        litellm.ModelResponse,
        litellm.completion(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a master programmer, translate the following code into {desired_language}. "
                    f"Translate what you can, don't complain. "
                    f"This is just a starter so a human programmer can finish the job.",
                },
                {"role": "user", "content": file_contents},
            ],
        ),
    )

    # Create .py file with the same name
    file_name = os.path.splitext(file_name)[0] + "_translated.txt"
    with open(file_name, "w", encoding="utf8", errors="replace") as f:
        f.write(completion.choices[0]["message"]["content"])
        f.write("\\n")
        # Write existing code into multiline comment
        if desired_language == "python":
            f.write(f"'''\\n\\n{file_contents}\\n\\n'''\\n")
        else:
            f.write(f"/*\\n\\n{file_contents}\\n\\n*/\\n")

    _log.info(f"Created {file_name}")

    print(completion.choices[0]["message"]["content"])
