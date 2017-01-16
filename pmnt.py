from Class_Portmanteau_Helper import Portmanteau_Helper as H

h = H()

test = h.get_portmanteaus("mustache")

for thing in test:
    print thing["word1"] + " + " + thing["word2"] + " = " + thing["portmanteau"]


# Why was R AE2 SH AH0 N AE1 L a match for [BCDFGHJKLMNPQRSTVWXZ]+ AE2 [BCDFGHJKLMNPQRSTVWXZ]+?
