import os
if not os.path.exists('/content/DeOldify/video'):
    os.makedirs('/content/DeOldify/video/source')
%cd "/content/DeOldify/video/source"

from google.colab import files
import subprocess
import subprocess
import shlex

uploaded = files.upload()

filenames = uploaded.keys()
if len(filenames) > 1:
  display(IPython.display.HTML('''<b style='color:red'>Error: You can upload only one video</b>'''))
  for file in filenames:
    os.remove([file][0])
  quit()
else:
  for file in filenames:
      file_extension = os.path.splitext([file][0])[1]
      
      if file_extension != '.mp4':
        display(IPython.display.HTML('''Please wait, we are converting your video'''))
 
        file_name = [file][0]
        shell_cmd = ("ffmpeg -i %s -f mp4 -vcodec libx264 -preset veryfast -acodec aac -movflags +faststart video.mp4 -hide_banner" % file_name)
        subprocess_cmd = shlex.split(shell_cmd)
        subprocess.call(subprocess_cmd)
        #!ffmpeg -i /content/[file][0]

  if uploaded:
    display(IPython.display.HTML('''<b style='color:green'>Done! Please Go to the next cell</b>'''))
  else:
    display(IPython.display.HTML('''<b style='color:red'>Error: Please rerun the cell to upload your video</b>'''))
