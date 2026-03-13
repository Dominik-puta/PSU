unos = input("Upisite ime datoteke: ")
word = "X-DSPAM-Confidence:"
kol = 0
sr = 0
input_file = open(unos, "r")
for line in input_file:
    line = line.rstrip()
  #  print(line)
    if line.startswith("X-DSPAM-Confidence:"):
        #print(line)
        broj = float(line.replace("X-DSPAM-Confidence: ", ""))
        kol += 1
        sr += broj
sr = sr / kol
print(sr)
input_file.close()
