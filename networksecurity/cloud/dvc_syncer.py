import os
import sys

class DVCSync:

    def sync_to_remote(self, folder: str, message: str):
        try:
            os.system(f"dvc add {folder}")
            os.system(f"git add {folder}.dvc .gitignore")
            os.system(f'git commit -m "{message}"')
            os.system("dvc push")

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def sync_from_remote(self):
        try:
            os.system("dvc pull")
        except Exception as e:
            raise NetworkSecurityException(e, sys)