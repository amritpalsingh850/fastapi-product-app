import os
import uuid

UPLOAD_DIR = "uploads"

def save_file(file):

    ext = file.filename.split(".")[-1]

    filename = f"{uuid.uuid4()}.{ext}"

    path = os.path.join(
        UPLOAD_DIR,
        filename
    )

    with open(path, "wb") as buffer:
        buffer.write(file.file.read())

    return filename