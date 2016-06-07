import webbrowser
import time
take_breaks = 1
break_count = 0
print("The program started on "+time.ctime())
while(break_count<take_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=N_KpjLhJa1k")
    break_count = break_count+1
    
