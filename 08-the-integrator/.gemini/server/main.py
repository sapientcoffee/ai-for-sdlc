# Copyright 2025 Google LLC.
# SPDX-License-Identifier: Apache-2.0
import argparse
import datetime

def add_note(note_content):
    """
    Appends a new note with a timestamp to the notes.txt file.
    This simulates a custom tool interacting with an internal service.
    """
    timestamp = datetime.datetime.now().isoformat()
    note_entry = f"[{timestamp}] {note_content}\n"

    with open("notes.txt", "a") as f:
        f.write(note_entry)

    return f"Successfully added note: {note_content}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server for an internal notes service.")
    parser.add_argument("--add-note", help="The content of the note to add.")

    args = parser.parse_args()

    if args.add_note:
        result = add_note(args.add_note)
        print(result)