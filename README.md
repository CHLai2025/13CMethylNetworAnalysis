# 13CMethylNetworkAnalysis
This is a file with the Python scripts that read the chemical shifts of methyl groups and create the edges. 
The highly perturbed nodes within the protein can be visualized by this tool.

[Introudction of the scripts]

autoGo.py: Execute each program file sequentially

13CCSPs.py: Calculate δ¹³C and δ¹H and normalize them by the spectrum width

pkm2std.py: Calculate the mean and std.. Filter the data with the thresholds

mergepk.py: Merge the data

final.py: Generate the connection document

edge.py: Change the format of the connection document for 3Dlinkp2s_picture.py 

3Dlinkp2s_picture.py: Show the edge connection between the nodes by NetworkX.
(The user who want to use 3Dlinkp2s_picture.py need to extract the atom cooridinates from PDB file)

[Libraries]

Please install pandas, matplotlib, and networkx.

[How to use]

add a chemical shift litst (.xlsx) into ''CSP_input'' file

>python3 autoGo.py

copy the edges result and paste into 3Dlinkp2s.py

>python3 3Dlinkp2s_picture.py

[Test run]

Download CSPc_4E_example.zip  

An example is in the CSP_input file

Run the scripts to get the connection information
