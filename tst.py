dados = {"Brazil":15682, "Colombia":3726, "Venezuela":1804, "Guyana":17, "Suriname":10, "Ecuador":2079, "Peru":1543, "Bolivia":125, "Chile":1282, "Paraguay":391, "Argentina":3815, "Uruguay":331, "Canada":17574, "United States":193617, "Mexico":32082, "Australia":1451, "New Zealand":154, "Papua New Guinea":322, "Solomon Islands":14, "Vanuatu":3, "Fiji":19, "Samoa":1}

maior = max(dados.values())

maior2 = 0 
for m in dados.values():
     if(m>maior2 and m<maior):
        maior2 = m 

print(maior2)       