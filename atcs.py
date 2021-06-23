# a list of drug names with their ATC codes
ranolazin = {'C01EB18'}

organic_nitrates = {
    'C01DA',  # Organische Nitrate
    'C01DA02',  # Glyceroltrinitrat
    'C01DA04',  # Methylpropylpropanedioldinitrat
    'C01DA05',  # Pentaerythrityltetranitrat
    'C01DA07',  # Propatylnitrat
    'C01DA08',  # Isosorbiddinitrat
    'C01DA09',  # Trolnitrat
    'C01DA13',  # Erythrityltetranitrat
    'C01DA14',  # Isosorbidmononitrat
    'C01DA20',  # Organische Nitrate in Kombination
    'C01DA38',  # Tenitramin
    'C01DA52',  # Glyceroltrinitrat, Kombinationen
    'C01DA54',  # Methylpropylpropanedioldinitrat, Kombinationen
    'C01DA55',  # Pentaerythrityltetranitrat, Kombinationen
    'C01DA57',  # Propatylnitrat, Kombinationen
    'C01DA58',  # Isosorbiddinitrat, Kombinationen
    'C01DA59',  # Trolnitrat, Kombinationen
    'C01DA63',  # Erythrityltetranitrat, Kombinationen
    'C01DA70'  # Organische Nitrate in Kombination mit Psycholeptika
}

molsidomin = {'C01DX12'}

nicorandil = {'C01DX16'}

trimetazidin = {'C01EB15'}

trapidil = {'C01DX11'}

platelet_aggregation_inhibitor = {
    'B01AC',  # Thrombozytenaggregationshemmer, exkl. Heparin
    'B01AC01',  # Ditazol
    'B01AC02',  # Cloricromen
    'B01AC03',  # Picotamid
    'B01AC04',  # Clopidogrel
    'B01AC05',  # Ticlopidin
    'B01AC06',  # Acetylsalicylsäure
    'B01AC07',  # Dipyridamol
    'B01AC08',  # Carbasalat calcium
    'B01AC09',  # Epoprostenol
    'B01AC10',  # Indobufen
    'B01AC11',  # Iloprost
    'B01AC12',  # Sulfinpyrazon
    'B01AC13',  # Abciximab
    'B01AC15',  # Aloxiprin
    'B01AC16',  # Eptifibatid
    'B01AC17',  # Tirofiban
    'B01AC18',  # Triflusal
    'B01AC19',  # Beraprost
    'B01AC21',  # Treprostinil
    'B01AC22',  # Prasugrel
    'B01AC23',  # Cilostazol
    'B01AC24',  # Ticagrelor
    'B01AC25',  # Cangrelor
    'B01AC26',  # Vorapaxar
    'B01AC27',  # Selexipag
    'B01AC30',  # Kombinationen
    'B01AC34',  # Clopidogrel und Acetylsalicylsäure
    'B01AC36',  # Dipyridamol und Acetylsalicylsäure
    'B01AC56',  # Acetylsalicylsäure, Kombinationen mit Protonenpumpenhemmern
    'B01AC86',  # Acetylsalicylsäure und Esomeprazol
    'A01AD05',  # Acetylsalicylsäure (Mittel zur oralen Lokalbehandlung)
    'C07FX02',  # Sotalol und Acetylsalicylsäure
    'C07FX03',  # Metoprolol und Acetylsalicylsäure
    'C07FX04',  # Bisoprolol und Acetylsalicylsäure
    'C10BX01',  # Simvastatin und Acetylsalicylsäure
    'C10BX02',  # Pravastatin und Acetylsalicylsäure
    'C10BX04',  # Simvastatin, Acetylsalicylsäure und Ramipril
    'C10BX05',  # Rosuvastatin und Acetylsalicylsäure
    'C10BX06',  # Atorvastatin, Acetylsalicylsäure und Ramipril
    'C10BX08',  # Atorvastatin und Acetylsalicylsäure
    'C10BX12',  # Atorvastatin, Acetylsalicylsäure und Perindopril
    'M01BA03',  # Acetylsalicylsäure und Corticosteroide
    'N02AJ02',  # Dihydrocodein und Acetylsalicylsäure
    'N02AJ07',  # Codein und Acetylsalicylsäure
    'N02AJ18',  # Oxycodon und Acetylsalicylsäure
    'N02BA01',  # Acetylsalicylsäure (Salicylsäure und Derivate)
    'N02BA51',  # Acetylsalicylsäure, Kombinationen exkl. Psycholeptika
    'N02BA71',  # Acetylsalicylsäure, Kombinationen mit Psycholeptika
    'R05XA02',  # Acetylsalicylsäure Kombinationen
    'R05XA22'  # Acetylsalicylsäure und Pseudoephedrin
}

selective_betablocker = {
    'C07AB',  # Beta-Adrenozeptorantagonisten, selektiv
    'C07AB01',  # Practolol
    'C07AB02',  # Metoprolol
    'C07AB03',  # Atenolol
    'C07AB04',  # Acebutolol
    'C07AB05',  # Betaxolol
    'C07AB06',  # Bevantolol
    'C07AB07',  # Bisoprolol
    'C07AB08',  # Celiprolol
    'C07AB09',  # Esmolol
    'C07AB10',  # Epanolol
    'C07AB11',  # S-Atenolol
    'C07AB12',  # Nebivolol
    'C07AB13',  # Talinolol
    'C07AB14',  # Landiolol
    'C07BB02',  # Metoprolol und Thiazide
    'C07BB22',  # Metoprolol und Hydrochlorothiazid
    'C07BB52',  # Metoprolol und Thiazide, Kombinationen
    'C07CB02',  # Metoprolol und andere Diuretika
    'C07CB22',  # Metoprolol und Chlortalidon
    'C07FB02',  # Metoprolol und Felodipin
    'C07FB13',  # Metoprolol und Amlodipin
    'C07FB22',  # Metoprolol und Nifedipin
    'C07FX03',  # Metoprolol und Acetylsalicylsäure
    'C07FX05',  # Metoprolol und Ivabradin
    'C07BB03',  # Atenolol und Thiazide
    'C07CB03',  # Atenolol und andere Diuretika
    'C07CB23',  # Atenolol und Chlortalidon
    'C07CB53',  # Atenolol und andere Diuretika, Kombinationen
    'C07DB01',  # Atenolol, Thiazide und andere Diuretika
    'C07FB03',  # Atenolol und Nifedipin
    'C07FX18',  # Atenolol, Chlortalidon und Hydralazin
    'C07BB04',  # Acebutolol und Thiazide
    'C07CB04',  # Acebutolol und andere Diuretika
    'C07FB26',  # Acebutolol und Nifedipin
    'C07BB06',  # Bevantolol und Thiazide
    'C07BB07',  # Bisoprolol und Thiazide
    'C07BB27',  # Bisoprolol und Hydrochlorothiazid
    'C07FB07',  # Bisoprolol und Amlodipin
    'C07FX04',  # Bisoprolol und Acetylsalicylsäure
    'C09BX02',  # Perindopril und Bisoprolol
    'C09BX04',  # Perindopril, Bisoprolol und Amlodipin
    'C09BX05',  # Ramipril und Bisoprolol
    'C07CB08',  # Celiprolol und andere Diuretika
    'C07BB12',  # Nebivolol und Thiazide
    'C07FB12',  # Nebivolol und Amlodipin
    'C09DX05'  # Valsartan und Nebivolol
}

propranolol = {
    'C07AA05',  # Propranolol
    'C07BA05',  # Propranolol und Thiazide
    'C07CA05',  # Propranolol und andere Diuretika
    'C07DA25',  # Propranolol, Hydrochlorothiazid und Triamteren
    'C07EA05',  # Propranolol und Vasodilatatoren
    'C07FX01'  # Propranolol und andere Kombinationen
}

betablocker = {
    'C07AB',  # Beta-Adrenozeptorantagonisten, selektiv
    'C07AB01',  # Practolol
    'C07AB02',  # Metoprolol
    'C07AB03',  # Atenolol
    'C07AB04',  # Acebutolol
    'C07AB05',  # Betaxolol
    'C07AB06',  # Bevantolol
    'C07AB07',  # Bisoprolol
    'C07AB08',  # Celiprolol
    'C07AB09',  # Esmolol
    'C07AB10',  # Epanolol
    'C07AB11',  # S-Atenolol
    'C07AB12',  # Nebivolol
    'C07AB13',  # Talinolol
    'C07AB14',  # Landiolol
    'C07BB02',  # Metoprolol und Thiazide
    'C07BB22',  # Metoprolol und Hydrochlorothiazid
    'C07BB52',  # Metoprolol und Thiazide, Kombinationen
    'C07CB02',  # Metoprolol und andere Diuretika
    'C07CB22',  # Metoprolol und Chlortalidon
    'C07FB02',  # Metoprolol und Felodipin
    'C07FB13',  # Metoprolol und Amlodipin
    'C07FB22',  # Metoprolol und Nifedipin
    'C07FX03',  # Metoprolol und Acetylsalicylsäure
    'C07FX05',  # Metoprolol und Ivabradin
    'C07BB03',  # Atenolol und Thiazide
    'C07CB03',  # Atenolol und andere Diuretika
    'C07CB23',  # Atenolol und Chlortalidon
    'C07CB53',  # Atenolol und andere Diuretika, Kombinationen
    'C07DB01',  # Atenolol, Thiazide und andere Diuretika
    'C07FB03',  # Atenolol und Nifedipin
    'C07FX18',  # Atenolol, Chlortalidon und Hydralazin
    'C07BB04',  # Acebutolol und Thiazide
    'C07CB04',  # Acebutolol und andere Diuretika
    'C07FB26',  # Acebutolol und Nifedipin
    'C07BB06',  # Bevantolol und Thiazide
    'C07BB07',  # Bisoprolol und Thiazide
    'C07BB27',  # Bisoprolol und Hydrochlorothiazid
    'C07FB07',  # Bisoprolol und Amlodipin
    'C07FX04',  # Bisoprolol und Acetylsalicylsäure
    'C09BX02',  # Perindopril und Bisoprolol
    'C09BX04',  # Perindopril, Bisoprolol und Amlodipin
    'C09BX05',  # Ramipril und Bisoprolol
    'C07CB08',  # Celiprolol und andere Diuretika
    'C07BB12',  # Nebivolol und Thiazide
    'C07FB12',  # Nebivolol und Amlodipin
    'C09DX05',  # Valsartan und Nebivolol
    'C07AA05',  # Propranolol
    'C07BA05',  # Propranolol und Thiazide
    'C07CA05',  # Propranolol und andere Diuretika
    'C07DA25',  # Propranolol, Hydrochlorothiazid und Triamteren
    'C07EA05',  # Propranolol und Vasodilatatoren
    'C07FX01',  # Propranolol und andere Kombinationen
    'C07AG02',  # Carvedilol
    'C07BG02',  # Carvedilol und Thiazide
    'C07FX06'  # Carvedilol und Ivabradin
}

sotalol = {
    'C07AA07',  # Sotalol
    'C07BA07',  # Sotalol und Thiazide
    'C07FX02'  # Sotalol und Acetylsalicylsäure
}

dextrometorphan = {
    'N07XX59',  # Dextromethorphan, Kombinationen
    'R05DA09',  # Dextromethorphan
    'R05DA59'  # Dextromethorphan, Kombinationen
}

carvedilol = {
    'C07AG02',  # Carvedilol
    'C07BG02',  # Carvedilol und Thiazide
    'C07FX06'  # Carvedilol und Ivabradin
}

metoprolol = {
    'C07AB02',  # Metoprolol
    'C07BB02',  # Metoprolol und Thiazide
    'C07BB22',  # Metoprolol und Hydrochlorothiazid
    'C07BB52',  # Metoprolol und Thiazide, Kombinationen
    'C07CB02',  # Metoprolol und andere Diuretika
    'C07CB22',  # Metoprolol und Chlortalidon
    'C07FB02',  # Metoprolol und Felodipin
    'C07FB13',  # Metoprolol und Amlodipin
    'C07FB22',  # Metoprolol und Nifedipin
    'C07FX03',  # Metoprolol und Acetylsalicylsäure
    'C07FX05',  # Metoprolol und Ivabradin
}

atenolol = {
    'C07AB03',  # Atenolol
    'C07AB11',  # S-Atenolol
    'C07BB03',  # Atenolol und Thiazide
    'C07CB03',  # Atenolol und andere Diuretika
    'C07CB23',  # Atenolol und Chlortalidon
    'C07CB53',  # Atenolol und andere Diuretika, Kombinationen
    'C07DB01',  # Atenolol, Thiazide und andere Diuretika
    'C07FB03',  # Atenolol und Nifedipin
    'C07FX18',  # Atenolol, Chlortalidon und Hydralazin
}

statin = {
    'C10AA',  # HMG-CoA-Reduktasehemmer
    'C10AA01',  # Simvastatin
    'C10AA02',  # Lovastatin
    'C10AA03',  # Pravastatin
    'C10AA04',  # Fluvastatin
    'C10AA05',  # Atorvastatin
    'C10AA06',  # Cerivastatin
    'C10AA07',  # Rosuvastatin
    'C10AA08',  # Pitavastatin
    'C10BA',  # HMG-CoA-Reduktasehemmer in Kombination mit anderen Mitteln, die den Lipidstoffwechsel beeinflussen
    'C10BA01',  # Lovastatin und Nicotinsäure
    'C10BA02',  # Simvastatin und Ezetimib
    'C10BA03',  # Pravastatin und Fenofibrat
    'C10BA04',  # Simvastatin und Fenofibrat
    'C10BA05',  # Atorvastatin und Ezetimib
    'C10BA06',  # Rosuvastatin und Ezetimib
    'C10BA07',  # Rosuvastatin und Omega-3-Fettsäuren
    'C10BA08',  # Atorvastatin und Omega-3-Fettsäuren
    'C10BA09',  # Rosuvastatin und Fenofibrat
    'C10BX',  # HMG-CoA-Reduktasehemmer, andere Kombinationen
    'C10BX01',  # Simvastatin und Acetylsalicylsäure
    'C10BX02',  # Pravastatin und Acetylsalicylsäure
    'C10BX03',  # Atorvastatin und Amlodipin
    'C10BX04',  # Simvastatin, Acetylsalicylsäure und Ramipril
    'C10BX05',  # Rosuvastatin und Acetylsalicylsäure
    'C10BX06',  # Atorvastatin, Acetylsalicylsäure und Ramipril
    'C10BX07',  # Rosuvastatin, Amlodipin und Lisinopril
    'C10BX08',  # Atorvastatin und Acetylsalicylsäure
    'C10BX09',  # Rosuvastatin und Amlodipin
    'C10BX10',  # Rosuvastatin und Valsartan
    'C10BX11',  # Atorvastatin, Amlodipin und Perindopril
    'C10BX12',  # Atorvastatin, Acetylsalicylsäure und Perindopril
    'C10BX13',  # Rosuvastatin, Perindopril und Indapamid
    'C10BX14',  # Rosuvastatin, Amlodipin und Perindopril
    'C10BX15',  # Atorvastatin und Perindopril
    'C10BX16',  # Rosuvastatin und Fimasartan
    'C10BX17',  # Rosuvastatin und Ramipril
    'C10BX18',  # Atorvastatin, Amlodipin und Ramipril
    'A10BH51',  # Sitagliptin und Simvastatin
    'A10BH52'  # Gemigliptin und Rosuvastatin
}

ezetimib = {
    'C10AX09',  # Ezetimib
    'C10BA02',  # Simvastatin und Ezetimib
    'C10BA05',  # Atorvastatin und Ezetimib
    'C10BA06'  # Rosuvastatin und Ezetimib
}

at1_antagonist = {
    'C09C',  # ANGIOTENSIN-II-REZEPTORBLOCKER (ARB), REIN
    'C09CA',  # Angiotensin-II-Rezeptorblocker (ARB), rein
    'C09CA01',  # Losartan
    'C09CA02',  # Eprosartan
    'C09CA03',  # Valsartan
    'C09CA04',  # Irbesartan
    'C09CA05',  # Tasosartan
    'C09CA06',  # Candesartan
    'C09CA07',  # Telmisartan
    'C09CA08',  # Olmesartanmedoxomil
    'C09CA09',  # Azilsartanmedoxomil
    'C09CA10',  # Fimasartan
    'C09D',  # ANGIOTENSIN-II-REZEPTORBLOCKER (ARB), KOMBINATIONEN
    'C09DA',  # Angiotensin-II-Rezeptorblocker (ARB) und Diuretika
    'C09DA01',  # Losartan und Diuretika
    'C09DA02',  # Eprosartan und Diuretika
    'C09DA03',  # Valsartan und Diuretika
    'C09DA04',  # Irbesartan und Diuretika
    'C09DA06',  # Candesartan und Diuretika
    'C09DA07',  # Telmisartan und Diuretika
    'C09DA08',  # Olmesartanmedoxomil und Diuretika
    'C09DA09',  # Azilsartanmedoxomil und Diuretika
    'C09DA10',  # Fimasartan und Diuretika
    'C09DA21',  # Losartan und Hydrochlorothiazid
    'C09DA22',  # Eprosartan und Hydrochlorothiazid
    'C09DA23',  # Valsartan und Hydrochlorothiazid
    'C09DA24',  # Irbesartan und Hydrochlorothiazid
    'C09DA26',  # Candesartan und Hydrochlorothiazid
    'C09DA27',  # Telmisartan und Hydrochlorothiazid
    'C09DA28',  # Olmesartanmedoxomil und Hydrochlorothiazid
    'C09DB',  # Angiotensin-II-Rezeptorblocker (ARB) und Calciumkanalblocker
    'C09DB01',  # Valsartan und Amlodipin
    'C09DB02',  # Olmesartanmedoxomil und Amlodipin
    'C09DB04',  # Telmisartan und Amlodipin
    'C09DB05',  # Irbesartan und Amlodipin
    'C09DB06',  # Losartan und Amlodipin
    'C09DB07',  # Candesartan und Amlodipin
    'C09DB08',  # Valsartan und Lercanidipin
    'C09DB09',  # Fimasartan und Amlodipin
    'C09DX',  # Angiotensin-II-Rezeptorblocker (ARB), andere Kombinationen
    'C09DX01',  # Valsartan, Amlodipin und Hydrochlorothiazid
    'C09DX02',  # Valsartan und Aliskiren
    'C09DX03',  # Olmesartanmedoxomil, Amlodipin und Hydrochlorothiazid
    'C09DX04',  # Valsartan und Sacubitril
    'C09DX05',  # Valsartan und Nebivolol
    'C09DX06',  # Candesartan, Amlodipin und Hydrochlorothiazid
    'C09DX07',  # Irbesartan, Amlodipin und Hydrochlorothiazid
    'C10BX10',  # Rosuvastatin und Valsartan
    'C10BX16'  # Rosuvastatin und Fimasartan
}

sacubitril_valsartan = {'C09DX04'}

eplerenon = {'C03DA04'}

ace_inhibitor = {
    'C09A',  # ACE-HEMMER, REIN
    'C09AA',  # ACE-Hemmer, rein
    'C09AA01',  # Captopril
    'C09AA02',  # Enalapril
    'C09AA03',  # Lisinopril
    'C09AA04',  # Perindopril
    'C09AA05',  # Ramipril
    'C09AA06',  # Quinapril
    'C09AA07',  # Benazepril
    'C09AA08',  # Cilazapril
    'C09AA09',  # Fosinopril
    'C09AA10',  # Trandolapril
    'C09AA11',  # Spirapril
    'C09AA12',  # Delapril
    'C09AA13',  # Moexipril
    'C09AA14',  # Temocapril
    'C09AA15',  # Zofenopril
    'C09AA16',  # Imidapril
    'C09B',  # ACE-HEMMER, KOMBINATIONEN
    'C09BA',  # ACE-Hemmer und Diuretika
    'C09BA01',  # Captopril und Diuretika
    'C09BA02',  # Enalapril und Diuretika
    'C09BA03',  # Lisinopril und Diuretika
    'C09BA04',  # Perindopril und Diuretika
    'C09BA05',  # Ramipril und Diuretika
    'C09BA06',  # Quinapril und Diuretika
    'C09BA07',  # Benazepril und Diuretika
    'C09BA08',  # Cilazapril und Diuretika
    'C09BA09',  # Fosinopril und Diuretika
    'C09BA12',  # Delapril und Diuretika
    'C09BA13',  # Moexipril und Diuretika
    'C09BA15',  # Zofenopril und Diuretika
    'C09BA21',  # Captopril und Hydrochlorothiazid
    'C09BA22',  # Enalapril und Hydrochlorothiazid
    'C09BA23',  # Lisinopril und Hydrochlorothiazid
    'C09BA25',  # Ramipril und Hydrochlorothiazid
    'C09BA26',  # Quinapril und Hydrochlorothiazid
    'C09BA27',  # Benazepril und Hydrochlorothiazid
    'C09BA28',  # Cilazapril und Hydrochlorothiazid
    'C09BA29',  # Fosinopril und Hydrochlorothiazid
    'C09BA33',  # Moexipril und Hydrochlorothiazid
    'C09BA35',  # Zofenopril und Hydrochlorothiazid
    'C09BA54',  # Perindopril und Indapamid
    'C09BA55',  # Ramipril und Piretanid
    'C09BB',  # ACE-Hemmer und Calciumkanalblocker
    'C09BB02',  # Enalapril und Lercanidipin
    'C09BB03',  # Lisinopril und Amlodipin
    'C09BB04',  # Perindopril und Amlodipin
    'C09BB05',  # Ramipril und Felodipin
    'C09BB06',  # Enalapril und Nitrendipin
    'C09BB07',  # Ramipril und Amlodipin
    'C09BB10',  # Trandolapril und Verapamil
    'C09BB12',  # Delapril und Manidipin
    'C09BX',  # ACE-Hemmer, andere Kombinationen
    'C09BX01',  # Perindopril, Amlodipin und Indapamid
    'C09BX02',  # Perindopril und Bisoprolol
    'C09BX03',  # Ramipril, Amlodipin und Hydrochlorothiazid
    'C09BX04',  # Perindopril, Bisoprolol und Amlodipin
    'C09BX05',  # Ramipril und Bisoprolol
    'C10BX04',  # Simvastatin, Acetylsalicylsäure und Ramipril
    'C10BX06',  # Atorvastatin, Acetylsalicylsäure und Ramipril
    'C10BX07',  # Rosuvastatin, Amlodipin und Lisinopril
    'C10BX11',  # Atorvastatin, Amlodipin und Perindopril
    'C10BX12',  # Atorvastatin, Acetylsalicylsäure und Perindopril
    'C10BX13',  # Rosuvastatin, Perindopril und Indapamid
    'C10BX14',  # Rosuvastatin, Amlodipin und Perindopril
    'C10BX15',  # Atorvastatin und Perindopril
    'C10BX17',  # Rosuvastatin und Ramipril
    'C10BX18'  # Atorvastatin, Amlodipin und Ramipril
}

furosemid = {
    'C03CA01',  # Furosemid
    'C03EB31',  # Furosemid und Amilorid
    'C03CB01',  # Furosemid und Kalium
    'C03EB01',  # Furosemid und Kalium sparende Mittel
    'C03EB21',  # Furosemid und Triamteren
    'C07CA51',  # Penbutolol und Furosemid
    'C03ED01'  # Spironolacton und Furosemid
}

torasemid = {'C03CA04'}

aliskiren = {
    'C09XA02',  # Aliskiren
    'C09XA54',  # Aliskiren, Amlodipin und Hydrochlorothiazid
    'C09XA53',  # Aliskiren und Amlodipin
    'C09XA52',  # Aliskiren und Hydrochlorothiazid
    'C09DX02'  # Valsartan und Aliskiren
}

celecoxib = {
    'M01AH01',  # Celecoxib
    'C08CA51',  # Amlodipin und Celecoxib
    'L01XX33'  # Celecoxib
}

desmopressin = {'H01BA02'}

diclofenac = {
    'M01AB05',  # Diclofenac
    'M01AB55',  # Diclofenac, Kombinationen
    'M01AB68',  # Diclofenac und Omeprazol
    'N02AJ05',  # Codein und Diclofenac
}

etoricoxib = {'M01AH05'}

parecoxib = {'M01AH04'}

triptan = {
    'N02CC',  # Selektive Serotonin-5HT1-Rezeptoragonisten
    'N02CC01',  # Sumatriptan
    'N02CC02',  # Naratriptan
    'N02CC03',  # Zolmitriptan
    'N02CC04',  # Rizatriptan
    'N02CC05',  # Almotriptan
    'N02CC06',  # Eletriptan
    'N02CC07'  # Frovatriptan
}

fludrocortison = {
    'H02AA02',  # Fludrocortison
    'R01AD64'  # Fludrocortison, Kombinationen
}

domperidon = {'A03FA03'}

dronedaron = {'C01BD07'}

eletriptan = {'N02CC06'}

flecainid = {'C01BC04'}

methylphenidat = {'N06BA04'}

moxonidin = {
    'C02AC05',  # Moxonidin
    'C02LC05'  # Moxonidin und Diuretika
}

pioglitazon = {
    'A10BG03',  # Pioglitazon
    'A10BD06',  # Glimepirid und Pioglitazon
    'A10BD09',  # Pioglitazon und Alogliptin
    'A10BD12',  # Pioglitazon und Sitagliptin
    'A10BD05'  # Pioglitazon und Metformin
}

tadalafil = {
    'C02KX07',  # Tadalafil
    'C02KX52',  # Ambrisentan und Tadalafil
    'G04BE08',  # Tadalafil
    'G04CA54'  # Tamsulosin und Tadalafil
}

naftidrofuryl = {'C04AX21'}

cilostazol = {'B01AC23'}

allopurinol = {
    'M04AA01',  # Allopurinol
    'M04AA51'  # Allopurinol, Kombinationen
}

febuxostat = {'M04AA03'}

probenecid = {'M04AB01'}

benzbromaron = {'M04AB03'}

colchicin = {'M04AC01'}

xipamid = {
    'C03BA10',  # Xipamid
    'C03EA15'  # Xipamid und Triamteren
}

hydrochlorothiazid = {
    'C03AA03',  # Hydrochlorothiazid
    'C03AB03',  # Hydrochlorothiazid und Kalium
    'C03AX01',  # Hydrochlorothiazid, Kombinationen
    'C03EA01',  # Hydrochlorothiazid und Kalium sparende Mittel'
    'C03EA21',  # Hydrochlorothiazid und Triamteren
    'C03EA41',  # Hydrochlorothiazid und Amilorid
    'C03EC21',  # Spironolacton und Hydrochlorothiazid
    'C07BB22',  # Metoprolol und Hydrochlorothiazid
    'C07BB27',  # Bisoprolol und Hydrochlorothiazid
    'C07DA25',  # Propranolol, Hydrochlorothiazid und Triamteren
    'C07DA26',  # Timolol, Hydrochlorothiazid und Amilorid
    'C08GA23',  # Verapamil und Hydrochlorothiazid
    'C08GA53',  # Verapamil, Hydrochlorothiazid und Triamteren
    'C09BA21',  # Captopril und Hydrochlorothiazid
    'C09BA22',  # Enalapril und Hydrochlorothiazid
    'C09BA23',  # Lisinopril und Hydrochlorothiazid
    'C09BA25',  # Ramipril und Hydrochlorothiazid
    'C09BA26',  # Quinapril und Hydrochlorothiazid
    'C09BA27',  # Benazepril und Hydrochlorothiazid
    'C09BA28',  # Cilazapril und Hydrochlorothiazid
    'C09BA29',  # Fosinopril und Hydrochlorothiazid
    'C09BA33',  # Moexipril und Hydrochlorothiazid
    'C09BA35',  # Zofenopril und Hydrochlorothiazid
    'C09BX03',  # Ramipril, Amlodipin und Hydrochlorothiazid
    'C09DA21',  # Losartan und Hydrochlorothiazid
    'C09DA22',  # Eprosartan und Hydrochlorothiazid
    'C09DA23',  # Valsartan und Hydrochlorothiazid
    'C09DA24',  # Irbesartan und Hydrochlorothiazid
    'C09DA26',  # Candesartan und Hydrochlorothiazid
    'C09DA27',  # Telmisartan und Hydrochlorothiazid
    'C09DA28',  # Olmesartanmedoxomil und Hydrochlorothiazid
    'C09DX01',  # Valsartan, Amlodipin und Hydrochlorothiazid
    'C09DX03',  # Olmesartanmedoxomil, Amlodipin und Hydrochlorothiazid
    'C09DX06',  # Candesartan, Amlodipin und Hydrochlorothiazid
    'C09DX07',  # Irbesartan, Amlodipin und Hydrochlorothiazid
    'C09XA52',  # Aliskiren und Hydrochlorothiazid
    'C09XA54'  # Aliskiren, Amlodipin und Hydrochlorothiazid
}

baclofen = {'M03BX01'}

bethanechol = {'N07AB02'}

buspiron = {'N05BE01'}

diphenhydramin = {
    'A04AB05',  # Diphenhydramin
    'A04AB55',  # Diphenhydramin, Kombinationen
    'D04AA32',  # Diphenhydramin
    'D04AA33',  # Diphenhydraminmethylbromid
    'D04AA82',  # Diphenhydramin, Kombinationen
    'N01BX06',  # Diphenhydramin
    'N05CM20',  # Diphenhydramin
    'N05CX07',  # Diphenhydramin, Kombinationen
    'R06AA02',  # Diphenhydramin
    'R06AA52',  # Diphenhydramin, Kombinationen
    'S01GX16'  # Diphenhydramin
}

doxylamin = {
    'A04AB56',  # Doxylamin, Kombinationen
    'N05CM21',  # Doxylamin
    'R06AA09',  # Doxylamin
    'R06AA59'  # Doxylamin, Kombinationen
}

dimenhydrinat = {
    'A04AB02',  # Dimenhydrinat
    'A04AB52',  # Dimenhydrinat, Kombinationen
    'N07CA22'  # Cinnarizin und Dimenhydrinat
}

levofloxacin = {
    'A02BD10',  # Lansoprazol, Amoxicillin und Levofloxacin
    'J01MA12',  # Levofloxacin
    'J01RA05'  # Levofloxacin und Ornidazol
}

methocarbamol = {
    'M03BA03',  # Methocarbamol
    'M03BA53',  # Methocarbamol, Kombinationen exkl. Psycholeptika
    'M03BA73'  # Methocarbamol, Kombinationen mit Psycholeptika
}

metoclopramid = {
    'A03FA01',  # Metoclopramid
    'A03FA51',  # Metoclopramid, Kombinationen
    'N02CX69'  # Metoclopramid und Paracetamol
}

ofloxacin_oral = {
    'J01MA01',  # Ofloxacin
    'J01RA09'  # Ofloxacin und Ornidazol
}

sulpirid = {
    'N07CA05',  # Sulpirid
    'N05AL01'  # Sulpirid
}

terizidon = {'J04AK03'}

lamotrigin = {'N03AX09'}

brivaracetam = {'N03AX23'}

ethosuximide = {
    'N03AD01',  # Ethosuximid
    'N03AD51'  # Ethosuximid, Kombinationen
}

lacosamide = {'N03AX18'}

perampanel = {'N03AX22'}

primidone = {'N03AA03'}

zonisamide = {'N03AX15'}

levetiracetam = {'N03AX14'}

valproat = {'N03AG01'}

carbamazepin = {'N03AF01'}

montelukast = {
    'R03DC03',  # Montelukast
    'R03DC53'  # Montelukast, Kombinationen
}

ics = {
    'R03BA',  # Glucocorticoide
    'R03BA01',  # Beclometason
    'R03BA02',  # Budesonid
    'R03BA03',  # Flunisolid
    'R03BA04',  # Betamethason
    'R03BA05',  # Fluticason
    'R03BA06',  # Triamcinolon
    'R03BA07',  # Mometason
    'R03BA08',  # Ciclesonid
    'R03BA09',  # Fluticasonfuroat
    'R03BA19'  # Dexamethason
}

aclidinium = {
    'R03AL05',  # Formoterol und Aclidiniumbromid
    'R03BB05'  # Aclidiniumbromid
}

aminophylline = {
    'R03DA05',  # Aminophyllin
    'R03DA55',  # Aminophyllin, Kombinationen
    'R03DB05'  # Aminophyllin und Sympathomimetika
}

ciclesonide = {
    'R01AD13',  # Ciclesonid
    'R03BA08'  # Ciclesonid
}

fenoterol = {
    'G02CA03',  # Fenoterol
    'R03AC04',  # Fenoterol
    'R03AL01',  # Fenoterol und Ipratropiumbromid
    'R03CC04',  # Fenoterol
    'R03CC54'  # Fenoterol, Kombinationen
}

formoterol = {
    'R03AC13',  # Formoterol
    'R03AK07',  # Formoterol und Budesonid
    'R03AK08',  # Formoterol und Beclometason
    'R03AK09',  # Formoterol und Mometason
    'R03AK11',  # Formoterol und Fluticason
    'R03AL05',  # Formoterol und Aclidiniumbromid
    'R03AL07',  # Formoterol und Glycopyrroniumbromid
    'R03AL09',  # Formoterol, Glycopyrroniumbromid und Beclometason
    'R03AL10',  # Formoterol und Tiotropiumbromid
    'R03AL11'  # Formoterol, Glycopyrroniumbromid und Budesonid
}

indacaterol = {
    'R03AC18',  # Indacaterol
    'R03AK14',  # Indacaterol und Mometason
    'R03AL04',  # Indacaterol und Glycopyrroniumbromid
    'R03AL12'  # Indacaterol, Glycopyrroiniumbromid und Mometason
}

ipratropium = {
    'C01CX10',  # Ipratropiumbromid
    'R01AX03',  # Ipratropiumbromid
    'R03AL01',  # Fenoterol und Ipratropiumbromid
    'R03AL02',  # Salbutamol und Ipratropiumbromid
    'R03BB01'  # Ipratropiumbromid
}

olodaterol = {
    'R03AC19',  # Olodaterol
    'R03AL06'  # Olodaterol und Tiotropiumbromid
}

reproterol = {
    'R03AC15',  # Reproterol
    'R03AK05',  # Reproterol und Cromoglicinsäure, Dinatriumsalz
    'R03CC14'  # Reproterol
}

roflumilast = {'R03DX07'}

salbutamol = {
    'R03AC02',  # Salbutamol
    'R03CC02',  # Salbutamol
    'R03AK13',  # Salbutamol und Beclometason
    'R03AK04',  # Salbutamol und Cromoglicinsäure, Dinatriumsalz
    'R03AL02'  # Salbutamol und Ipratropiumbromid
}

salmeterol = {
    'R03AC12',  # Salmeterol
    'R03AK12',  # Salmeterol und Budesonid
    'R03AK06'  # Salmeterol und Fluticason
}

terbutaline = {
    'R03AC03',  # Terbutalin
    'R03CC03',  # Terbutalin
    'R03CC53'  # Terbutalin, Kombinationen
}

theophylline = {
    'C01EB28',  # Theophyllin
    'R03DA04',  # Theophyllin
    'C01EX66',  # Theophyllin, Kombinationen
    'R03DA54',  # Theophyllin, Kombinationen exkl. Psycholeptika
    'R03DA74',  # Theophyllin, Kombinationen mit Psycholeptika
    'R03DB04'  # Theophyllin und Sympathomimetika
}

tiotropium = {
    'R03AL10',  # Formoterol und Tiotropiumbromid
    'R03AL06',  # Olodaterol und Tiotropiumbromid
    'R03BB04',  # Tiotropiumbromid
    'R03BB54'  # Tiotropiumbromid, Kombinationen
}

umeclidinium = {
    'R03BB07',  # Umeclidiniumbromid
    'R03AL08',  # Vilanterol, Umeclidiniumbromid und Fluticasonfuroat
    'R03AL03'  # Vilanterol und Umeclidiniumbromid
}

cromon = {
    'R03BC',  # Antiallergika, exkl. Corticosteroide
    'R03BC01',  # Cromoglicinsäure
    'R03BC03'  # Nedocromil
}

omalizumab = {'R03DX05'}

mepolizumab = {'R03DX09'}

reslizumab = {'R03DX08'}

benralizumab = {'R03DX10'}

calcium_channelblocker = {
    'C08',  # CALCIUMKANALBLOCKER
    'C08C',  # SELEKTIVE CALCIUMKANALBLOCKER MIT VORWIEGENDER GEFÄSSWIRKUNG
    'C08CA',  # Dihydropyridin-Derivate
    'C08CA01',  # Amlodipin
    'C08CA02',  # Felodipin
    'C08CA03',  # Isradipin
    'C08CA04',  # Nicardipin
    'C08CA05',  # Nifedipin
    'C08CA06',  # Nimodipin
    'C08CA07',  # Nisoldipin
    'C08CA08',  # Nitrendipin
    'C08CA09',  # Lacidipin
    'C08CA10',  # Nilvadipin
    'C08CA11',  # Manidipin
    'C08CA12',  # Barnidipin
    'C08CA13',  # Lercanidipin
    'C08CA14',  # Cilnidipin
    'C08CA15',  # Benidipin
    'C08CA16',  # Clevidipin
    'C08CA51',  # Amlodipin und Celecoxib
    'C08CA55',  # Nifedipin, Kombinationen
    'C08CX',  # Andere selektive Calciumkanalblocker mit vorwiegender Gefäßwirkung
    'C08CX01',  # Mibefradil
    'C08D',  # SELEKTIVE CALCIUMKANALBLOCKER MIT VORWIEGENDER HERZWIRKUNG
    'C08DA',  # Phenylalkylamin-Derivate
    'C08DA01',  # Verapamil
    'C08DA02',  # Gallopamil
    'C08DA51',  # Verapamil, Kombinationen
    'C08DA81',  # Verapamil in Kombination mit Chinidin
    'C08DB',  # Benzothiazepin-Derivate
    'C08DB01',  # Diltiazem
    'C08E',  # NICHTSELEKTIVE CALCIUMKANALBLOCKER
    'C08EA',  # Phenylalkylamin-Derivate
    'C08EA01',  # Fendilin
    'C08EA02',  # Bepridil
    'C08EX',  # Andere nichtselektive Calciumkanalblocker
    'C08EX01',  # Lidoflazin
    'C08EX02',  # Perhexilin
    'C08G',  # CALCIUMKANALBLOCKER UND DIURETIKA
    'C08GA',  # Calciumkanalblocker und Diuretika
    'C08GA01',  # Nifedipin und Diuretika
    'C08GA02',  # Amlodipin und Diuretika
    'C08GA23',  # Verapamil und Hydrochlorothiazid
    'C08GA53',  # Verapamil, Hydrochlorothiazid und Triamteren
    'C07FB',  # Beta-Adrenozeptorantagonisten und Calciumkanalblocker
    'C07FB02',  # Metoprolol und Felodipin
    'C07FB03',  # Atenolol und Nifedipin
    'C07FB07',  # Bisoprolol und Amlodipin
    'C07FB12',  # Nebivolol und Amlodipin
    'C07FB13',  # Metoprolol und Amlodipin
    'C07FB22',  # Metoprolol und Nifedipin
    'C07FB26',  # Acebutolol und Nifedipin
    'C09BB',  # ACE-Hemmer und Calciumkanalblocker
    'C09BB02',  # Enalapril und Lercanidipin
    'C09BB03',  # Lisinopril und Amlodipin
    'C09BB04',  # Perindopril und Amlodipin
    'C09BB05',  # Ramipril und Felodipin
    'C09BB06',  # Enalapril und Nitrendipin
    'C09BB07',  # Ramipril und Amlodipin
    'C09BB10',  # Trandolapril und Verapamil
    'C09BB12',  # Delapril und Manidipin
    'C09BX01',  # Perindopril, Amlodipin und Indapamid
    'C09BX03',  # Ramipril, Amlodipin und Hydrochlorothiazid
    'C09BX04',  # Perindopril, Bisoprolol und Amlodipin
    'C09DB',  # Angiotensin-II-Rezeptorblocker (ARB) und Calciumkanalblocker
    'C09DB01',  # Valsartan und Amlodipin
    'C09DB02',  # Olmesartanmedoxomil und Amlodipin
    'C09DB04',  # Telmisartan und Amlodipin
    'C09DB05',  # Irbesartan und Amlodipin
    'C09DB06',  # Losartan und Amlodipin
    'C09DB07',  # Candesartan und Amlodipin
    'C09DB08',  # Valsartan und Lercanidipin
    'C09DB09',  # Fimasartan und Amlodipin
    'C09DX01',  # Valsartan, Amlodipin und Hydrochlorothiazid
    'C09DX03',  # Olmesartanmedoxomil, Amlodipin und Hydrochlorothiazid
    'C09DX06',  # Candesartan, Amlodipin und Hydrochlorothiazid
    'C09DX07',  # Irbesartan, Amlodipin und Hydrochlorothiazid
    'C09XA53',  # Aliskiren und Amlodipin
    'C09XA54',  # Aliskiren, Amlodipin und Hydrochlorothiazid
    'C05AE03'  # Diltiazem
}
