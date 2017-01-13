from Class_Portmanteau_Helper import Portmanteau_Helper as H

h = H()

test = h.get_portmanteaus("Booty")

for thing in test:
    print thing["word1"] + " + " + thing["word2"] + " = " + thing["portmanteau"]
