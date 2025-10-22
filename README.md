# Banknote Verifier – Echt vs Vals Geld Herkenning

## Groepsleden
- Emiel Mangelschots
- Bjarni Heselmans

---

## Projectdoel
Dit project heeft als doel een systeem te ontwikkelen dat met een webcam of camera via microcontroller kan bepalen of een bankbiljet echt of vals is.
In tegenstelling tot machine learning of deep learning benaderingen, maken wij uitsluitend gebruik van klassieke image processing-technieken zoals:

- Kleurconversies (RGB → HSV)
- Histogram equalization en gamma-correctie
- Low-pass filtering (ruisonderdrukking)
- Edge detection (Canny / Sobel)
- Frequentiedomeinanalyse (FFT)
- Textuuranalyse via Gabor- en Laplacian-filters

Echte biljetten vertonen specifieke microstructuren, patronen en fijne textuurdetails die vervalsingen missen. Door deze kenmerken te analyseren en te kwantificeren kunnen we het biljet classificeren als "waarschijnlijk echt" of "waarschijnlijk vals".

---

## Overzicht van de methode

### 1. Beeldverwerving
- Input via webcam of camera op microcontroller (bijv. Raspberry Pi).
- Bankbiljetten worden op een egale achtergrond gelegd onder constante belichting.
- Beelden worden vastgelegd in RGB-formaat (8-bit per kanaal).

### 2. Voorbewerking
Doel: stabiliseren van de belichting, verbeteren van contrast, en ruisonderdrukking.

| Stap | Methode | Reden / Verwachte effect |
|------|----------|--------------------------|
| Kleurconversie | RGB → HSV | Scheidt helderheid (Value) van kleurtint (Hue) zodat analyse robuuster is voor belichting. |
| Histogram equalization / Gamma-correctie | CLAHE (Contrast Limited Adaptive Histogram Equalization) | Verbetert contrast, maakt randen beter zichtbaar, en compenseert ongelijke belichting. |
| Low-pass filtering | Gaussian blur (σ = 1–2) | Vermindert hoge-frequentieruis, voorkomt foutieve randdetectie. |

---

### 3. Edge & textuuranalyse
Na de voorbewerking worden rand- en textuurkenmerken geëxtraheerd.

| Stap | Methode | Doel |
|------|----------|------|
| Edge detection | Canny of Sobel | Opsporen van randen en microprintpatronen op het biljet. |
| Edge density berekening | Gemiddeld aantal edge-pixels per oppervlakte | Echte biljetten hebben hogere en complexere randdichtheid. |
| Laplacian of High-pass filtering | Versterken van hoge frequenties | Maakt fijne structuren en textuurverschillen duidelijker. |
| Gabor-filters | Oriëntatie- en frequentiegevoelige textuuranalyse | Herkent druklijnen en textuurpatronen die op echte biljetten voorkomen. |

---

### 4. Frequentiedomeinanalyse (FFT)
Een 2D Fast Fourier Transform (FFT) wordt toegepast op de grijswaardenversie van het biljet.
Door de energieverdeling in de frequentiedomeinrepresentatie te meten, kunnen we zien of het biljet regelmatige hoge-frequentiecomponenten bevat (kenmerkend voor offsetdruk).

- Echte biljetten: duidelijke ringstructuren / pieken in hoge frequenties.
- Valse biljetten (geprint): energie geconcentreerd in lage frequenties (vlakke patronen).

Metrieken:
- Ratio van hoge-frequentie-energie tot totale energie (HF_ratio)
- Aantal significante pieken in frequentiedomein (peak_count)

---

### 5. Classificatie (Echt / Vals)
Op basis van de gemeten kenmerken wordt een eenvoudige regelgebaseerde beslissing genomen:

```
if (edge_density > threshold1) and (HF_ratio > threshold2):
    label = "Echt"
else:
    label = "Vals"
```

Drempelwaarden worden experimenteel bepaald door een reeks echte en valse biljetten te analyseren.

---

## Verwachte resultaten & evaluatie
We zullen tijdens het project meetbare waarden verzamelen om de prestaties te beoordelen:

| Metriek | Beschrijving | Doelwaarde |
|----------|---------------|------------|
| Edge density verschil | Gemiddeld verschil tussen echte en valse biljetten | > 20% |
| HF-ratio verschil | Verschil in hoge-frequentie energie | > 15% |
| Classificatienauwkeurigheid | Correcte voorspellingen op testset | ≥ 80% |

We zullen ook voorbeelden tonen van foutieve classificaties om beperkingen te bespreken.

---

## Overwogen alternatieven
| Stap | Alternatief | Waarom (nog) niet gekozen |
|------|--------------|----------------------------|
| Edge detection | Laplacian of Scharr filter | Geprobeerd indien Canny te gevoelig is voor ruis. |
| Frequentieanalyse | Wavelet-transformatie | Interessant alternatief; mogelijk in latere fase. |
| Classificatie | SVM of Random Forest | Te complex voor eerste prototype, maar kan later toegevoegd worden. |
| Belichtingscorrectie | Retinex / homomorphic filtering | Wordt onderzocht als geavanceerde verbetering. |

---

## Tools & afhankelijkheden
- Python 3.12+
- OpenCV – beeldbewerking en filtering
- NumPy / SciPy – wiskundige berekeningen en FFT
- Matplotlib – visualisatie van resultaten
- (Optioneel): Raspberry Pi + camera-module

---

## Installatie & gebruik (wordt verder aangevuld)
```
# 1. Clone de repository
git clone https://github.com/<jullie-gebruikersnaam>/banknote-verifier.git

# 2. Installeer vereiste pakketten
pip install -r requirements.md

# 3. Start de applicatie
python main.py
```

---

## Toekomstige uitbreidingen
- Automatische herkenning van biljetwaarde (€5, €10, €20, …)
- Real-time detectie via live camerastream
- Analyse onder verschillende lichtcondities
- Implementatie van een eenvoudige machine learning-classifier (indien toegestaan)

---

## Bronnen
- Slides Image Processing – Dr. Ing. Koen Gilissen
- OpenCV Documentation
- Gonzalez & Woods, Digital Image Processing, 4th Edition

---

Opmerking: Deze README is een levend document.
Tijdens de ontwikkeling worden resultaten, grafieken, codevoorbeelden en prestatiemaatstaven toegevoegd.

## Contributators
- **Emiel Mangelschots** – _Student_ – [GitHub](https://github.com/empel06)  
- **Bjarni Heselmans** – _Student_ – [GitHub](https://github.com/BjarniHeselmans) 