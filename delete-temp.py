import asyncio
import os
import shutil
import tempfile


async def delete_temp_file():
    temp_dir = tempfile.gettempdir()

    # Iterate over the files and directories in the temporary directory
    for root, dirs, files in os.walk(temp_dir):
        for filename in files:
            # Delete any file with a "tmp" prefix
            if filename.startswith('tmp') and filename.endswith('.txt') and filename.endswith('.tmp') and filename.endswith('.log') and filename.endswith('.ses') and filename.endswith('.xml'):
                try:
                    os.remove(os.path.join(root, filename))
                except OSError:
                    raise OSError(
                        f"Could not delete temporary file: {filename}")

        for dirname in dirs:
            # Delete any subdirectory with a "_MEI" or "tmp" prefix
            if dirname.startswith('_MEI') or dirname.startswith('tmp'):
                subdir_path = os.path.join(root, dirname)
                try:
                    shutil.rmtree(subdir_path)
                except OSError:
                    raise OSError(
                        f"Could not delete temporary directory: {subdir_path}")

asyncio.run(delete_temp_file())
