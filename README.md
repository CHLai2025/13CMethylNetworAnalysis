# 13CMethylNetworAnalysis
This is a file with the Python scripts that read the chemical shifts of methyl groups and create the edges. 

[Introudction of the scripts]

autoGo.py: Execute each program file sequentially

13CCSPs.py: Calculate δ¹³C and δ¹H and normalize them by the spectrum width

pkm2std.py: Calculate the mean and std.. Filter the data

mergepk.py: Merge the data

final.py: Generate the connection document

edge.py: Change the format of the connection document for 3Dlinkp2s_picture.py 

3Dlinkp2s_picture.py: Show the edge connection between the nodes (atom cooridinates from PDB ) by NetworkX.


[How to use]

add a chemical shift litst (.xlsx) into ''CSP_input'' file

>python3 autoGo.py

copy the edges result and paste into 3Dlinkp2s.py

>python3 3Dlinkp2s_picture.py
