#@title Run me to get `p1.py`!
from google.colab import files
from IPython.display import HTML, clear_output

%rm -f p1.py
%history -l 1 -f p1.py
files.download("p1.py")
clear_output
HTML("""<span style="font-size: larger;">
   IMPORTANT: Please check the content in p1.py before your submission.</span></br>
   <span><a href="https://cool.ntu.edu.tw/courses/19307/assignments/111173#submit"
   target="_blank"
   rel="noopener noreferrer">Go to NTU COOL for submission!</a></span>""")
