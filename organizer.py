import os
import shutil

extensions = {".ipynb":"/home/kurtymittens/Downloads/PythonNotebooks",
              ".docx":"/home/kurtymittens/Downloads/WordFiles",
              ".pptx":"/home/kurtymittens/Downloads/PowerPointFiles",
              ".jpeg":"/home/kurtymittens/Pictures",
              ".jpg":"/home/kurtymittens/Pictures",
              ".png":"/home/kurtymittens/Pictures",
              ".pdf":"/home/kurtymittens/Downloads/PDF",
              }
files = os.listdir("/home/kurtymittens/Downloads") # Focuses in every file you want to organize

"""

"""
for i in files:
  try:
    if os.path.splitext(i)[1] != "":
      shutil.move(f"/home/kurtymittens/Downloads/{i}", extensions[os.path.splitext(i)[1]])
  except KeyError:
    shutil.move(f"/home/kurtymittens/Downloads/{i}", "/home/kurtymittens/Downloads/Others")

