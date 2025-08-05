# Copyright 2025 Google LLC.
# SPDX-License-Identifier: Apache-2.0
# This file has some style violations for testing the /review-local command.

# Missing type hints and docstring
def myFunction(myVar):
    # Uses a print statement instead of logging
    print(f"The variable is: {myVar}")
    return myVar + 1