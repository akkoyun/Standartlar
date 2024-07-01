# Ölçüm Tipi Tablosu

Veri paketi içerisinde gelen tüm ölçümler (listede belirtilen) **measurement** tablosu içerisine kaydedilecektir. 

## Ölçüm Segmentleri

| Segment     | Segment ID |
|-------------|------------|
| Device      | 1          |
| Power       | 2          |
| Environment | 3          |
| Water       | 4          |
| Energy      | 5          |
| Battery     | 6          |

## Ölçüm Tipleri

| Type ID | Type Name                   | Variable         | Unit  | Segment     |
|---------|-----------------------------|------------------|-------|-------------|
|         | Air Temperature             | AT               | C     | Environment |
|         | Air Humidity                | AH               | %     | Environment |
|         | Air Pressure                | AP               | mBar  | Environment |
|         | UV Index                    | UV               | -     | Environment |
|         | Soil Temperature 0          | ST0              | C     | Environment |
|         | Soil Temperature 1          | ST1              | C     | Environment |
|         | Soil Temperature 2          | ST2              | C     | Environment |
|         | Soil Temperature 3          | ST3              | C     | Environment |
|         | Soil Temperature 4          | ST4              | C     | Environment |
|         | Soil Temperature 5          | ST5              | C     | Environment |
|         | Soil Temperature 6          | ST6              | C     | Environment |
|         | Soil Temperature 7          | ST7              | C     | Environment |
|         | Soil Temperature 8          | ST8              | C     | Environment |
|         | Soil Temperature 9          | ST9              | C     | Environment |
|         | Rain                        | R                | -     | Environment |
|         | Wind Direction              | WD               | D     | Environment |
|         | Wind Speed                  | WS               | m/sn  | Environment |
|         | Water Pressure IN           | PIN              | Bar   | Water       |
|         | Water Pressure OUT          | POUT             | Bar   | Water       |
|         | Phase R Instant Voltage     | VR               | Volt  | Energy      |
|         | Phase S Instant Voltage     | VS               | Volt  | Energy      |
|         | Phase T Instant Voltage     | VT               | Volt  | Energy      |
|         | Phase R RMS Voltage         | VR_RMS           | Volt  | Energy      |
|         | Phase S RMS Voltage         | VS_RMS           | Volt  | Energy      |
|         | Phase T RMS Voltage         | VT_RMS           | Volt  | Energy      |
|         | Average RMS Voltage         | VA_RMS           | Volt  | Energy      |
|         | Phase R Fundamental Voltage | VR_FUND          | Volt  | Energy      |
|         | Phase S Fundamental Voltage | VS_FUND          | Volt  | Energy      |
|         | Phase T Fundamental Voltage | VT_FUND          | Volt  | Energy      |
|         | Phase R Harmonic-2 Voltage  | VR_HARM_2        | Volt  | Energy      |
|         | Phase S Harmonic-2 Voltage  | VS_HARM_2        | Volt  | Energy      |
|         | Phase T Harmonic-2 Voltage  | VT_HARM_2        | Volt  | Energy      |
|         | Average Harmonic-2 Voltage  | VA_HARM_2        | Volt  | Energy      |
|         | Phase R Harmonic-3 Voltage  | VR_HARM_3        | Volt  | Energy      |
|         | Phase S Harmonic-3 Voltage  | VS_HARM_3        | Volt  | Energy      |
|         | Phase T Harmonic-3 Voltage  | VT_HARM_3        | Volt  | Energy      |
|         | Average Harmonic-3 Voltage  | VA_HARM_3        | Volt  | Energy      |
|         | Phase R Harmonic-4 Voltage  | VR_HARM_4        | Volt  | Energy      |
|         | Phase S Harmonic-4 Voltage  | VS_HARM_4        | Volt  | Energy      |
|         | Phase T Harmonic-4 Voltage  | VT_HARM_4        | Volt  | Energy      |
|         | Average Harmonic-4 Voltage  | VA_HARM_4        | Volt  | Energy      |
|         | Phase R Harmonic-5 Voltage  | VR_HARM_5        | Volt  | Energy      |
|         | Phase S Harmonic-5 Voltage  | VS_HARM_5        | Volt  | Energy      |
|         | Phase T Harmonic-5 Voltage  | VT_HARM_5        | Volt  | Energy      |
|         | Average Harmonic-5 Voltage  | VA_HARM_5        | Volt  | Energy      |
|         | Phase R Harmonic-6 Voltage  | VR_HARM_6        | Volt  | Energy      |
|         | Phase S Harmonic-6 Voltage  | VS_HARM_6        | Volt  | Energy      |
|         | Phase T Harmonic-6 Voltage  | VT_HARM_6        | Volt  | Energy      |
|         | Average Harmonic-6 Voltage  | VA_HARM_6        | Volt  | Energy      |
|         | Phase R Harmonic-7 Voltage  | VR_HARM_7        | Volt  | Energy      |
|         | Phase S Harmonic-7 Voltage  | VS_HARM_7        | Volt  | Energy      |
|         | Phase T Harmonic-7 Voltage  | VT_HARM_7        | Volt  | Energy      |
|         | Average Harmonic-7 Voltage  | VA_HARM_7        | Volt  | Energy      |
|         | Phase R Harmonic-8 Voltage  | VR_HARM_8        | Volt  | Energy      |
|         | Phase S Harmonic-8 Voltage  | VS_HARM_8        | Volt  | Energy      |
|         | Phase T Harmonic-8 Voltage  | VT_HARM_8        | Volt  | Energy      |
|         | Average Harmonic-8 Voltage  | VA_HARM_8        | Volt  | Energy      |
|         | Phase R Harmonic-9 Voltage  | VR_HARM_9        | Volt  | Energy      |
|         | Phase S Harmonic-9 Voltage  | VS_HARM_9        | Volt  | Energy      |
|         | Phase T Harmonic-9 Voltage  | VT_HARM_9        | Volt  | Energy      |
|         | Average Harmonic-9 Voltage  | VA_HARM_9        | Volt  | Energy      |
|         | Phase R Harmonic-10 Voltage | VR_HARM_10       | Volt  | Energy      |
|         | Phase S Harmonic-10 Voltage | VS_HARM_10       | Volt  | Energy      |
|         | Phase T Harmonic-10 Voltage | VT_HARM_10       | Volt  | Energy      |
|         | Average Harmonic-10 Voltage | VA_HARM_10       | Volt  | Energy      |
|         | Phase R Harmonic-11 Voltage | VR_HARM_11       | Volt  | Energy      |
|         | Phase S Harmonic-11 Voltage | VS_HARM_11       | Volt  | Energy      |
|         | Phase T Harmonic-11 Voltage | VT_HARM_11       | Volt  | Energy      |
|         | Average Harmonic-11 Voltage | VA_HARM_11       | Volt  | Energy      |
|         | Phase R Harmonic-12 Voltage | VR_HARM_12       | Volt  | Energy      |
|         | Phase S Harmonic-12 Voltage | VS_HARM_12       | Volt  | Energy      |
|         | Phase T Harmonic-12 Voltage | VT_HARM_12       | Volt  | Energy      |
|         | Average Harmonic-12 Voltage | VA_HARM_12       | Volt  | Energy      |
|         | Phase R Harmonic-13 Voltage | VR_HARM_13       | Volt  | Energy      |
|         | Phase S Harmonic-13 Voltage | VS_HARM_13       | Volt  | Energy      |
|         | Phase T Harmonic-13 Voltage | VT_HARM_13       | Volt  | Energy      |
|         | Average Harmonic-13 Voltage | VA_HARM_13       | Volt  | Energy      |
|         | Phase R Harmonic-14 Voltage | VR_HARM_14       | Volt  | Energy      |
|         | Phase S Harmonic-14 Voltage | VS_HARM_14       | Volt  | Energy      |
|         | Phase T Harmonic-14 Voltage | VT_HARM_14       | Volt  | Energy      |
|         | Average Harmonic-14 Voltage | VA_HARM_14       | Volt  | Energy      |
|         | Phase R Harmonic-15 Voltage | VR_HARM_15       | Volt  | Energy      |
|         | Phase S Harmonic-15 Voltage | VS_HARM_15       | Volt  | Energy      |
|         | Phase T Harmonic-15 Voltage | VT_HARM_15       | Volt  | Energy      |
|         | Average Harmonic-15 Voltage | VA_HARM_15       | Volt  | Energy      |
|         | Phase R Harmonic-16 Voltage | VR_HARM_16       | Volt  | Energy      |
|         | Phase S Harmonic-16 Voltage | VS_HARM_16       | Volt  | Energy      |
|         | Phase T Harmonic-16 Voltage | VT_HARM_16       | Volt  | Energy      |
|         | Average Harmonic-16 Voltage | VA_HARM_16       | Volt  | Energy      |
|         | Phase R Harmonic-17 Voltage | VR_HARM_17       | Volt  | Energy      |
|         | Phase S Harmonic-17 Voltage | VS_HARM_17       | Volt  | Energy      |
|         | Phase T Harmonic-17 Voltage | VT_HARM_17       | Volt  | Energy      |
|         | Average Harmonic-17 Voltage | VA_HARM_17       | Volt  | Energy      |
|         | Phase R Harmonic-18 Voltage | VR_HARM_18       | Volt  | Energy      |
|         | Phase S Harmonic-18 Voltage | VS_HARM_18       | Volt  | Energy      |
|         | Phase T Harmonic-18 Voltage | VT_HARM_18       | Volt  | Energy      |
|         | Average Harmonic-18 Voltage | VA_HARM_18       | Volt  | Energy      |
|         | Phase R Harmonic-19 Voltage | VR_HARM_19       | Volt  | Energy      |
|         | Phase S Harmonic-19 Voltage | VS_HARM_19       | Volt  | Energy      |
|         | Phase T Harmonic-19 Voltage | VT_HARM_19       | Volt  | Energy      |
|         | Average Harmonic-19 Voltage | VA_HARM_19       | Volt  | Energy      |
|         | Phase R Harmonic-20 Voltage | VR_HARM_20       | Volt  | Energy      |
|         | Phase S Harmonic-20 Voltage | VS_HARM_20       | Volt  | Energy      |
|         | Phase T Harmonic-20 Voltage | VT_HARM_20       | Volt  | Energy      |
|         | Average Harmonic-20 Voltage | VA_HARM_20       | Volt  | Energy      |
|         | Phase R Current             | IR_RMS           | Amper | Energy      |
|         | Phase S Current             | IS_RMS           | Amper | Energy      |
|         | Phase T Current             | IT_RMS           | Amper | Energy      |
|         | Average Current             | IA_RMS           | Amper | Energy      |
|         | Phase R Fundamental Current | IR_FUND          | Amper | Energy      |
|         | Phase S Fundamental Current | IS_FUND          | Amper | Energy      |
|         | Phase T Fundamental Current | IT_FUND          | Amper | Energy      |
|         | Phase R Harmonic-2 Current  | IR_HARM_2        | Amper | Energy      |
|         | Phase S Harmonic-2 Current  | IS_HARM_2        | Amper | Energy      |
|         | Phase T Harmonic-2 Current  | IT_HARM_2        | Amper | Energy      |
|         | Average Harmonic-2 Current  | IA_HARM_2        | Amper | Energy      |
|         | Phase R Harmonic-3 Current  | IR_HARM_3        | Amper | Energy      |
|         | Phase S Harmonic-3 Current  | IS_HARM_3        | Amper | Energy      |
|         | Phase T Harmonic-3 Current  | IT_HARM_3        | Amper | Energy      |
|         | Average Harmonic-3 Current  | IA_HARM_3        | Amper | Energy      |
|         | Phase R Harmonic-4 Current  | IR_HARM_4        | Amper | Energy      |
|         | Phase S Harmonic-4 Current  | IS_HARM_4        | Amper | Energy      |
|         | Phase T Harmonic-4 Current  | IT_HARM_4        | Amper | Energy      |
|         | Average Harmonic-4 Current  | IA_HARM_4        | Amper | Energy      |
|         | Phase R Harmonic-5 Current  | IR_HARM_5        | Amper | Energy      |
|         | Phase S Harmonic-5 Current  | IS_HARM_5        | Amper | Energy      |
|         | Phase T Harmonic-5 Current  | IT_HARM_5        | Amper | Energy      |
|         | Average Harmonic-5 Current  | IA_HARM_5        | Amper | Energy      |
|         | Phase R Harmonic-6 Current  | IR_HARM_6        | Amper | Energy      |
|         | Phase S Harmonic-6 Current  | IS_HARM_6        | Amper | Energy      |
|         | Phase T Harmonic-6 Current  | IT_HARM_6        | Amper | Energy      |
|         | Average Harmonic-6 Current  | IA_HARM_6        | Amper | Energy      |
|         | Phase R Harmonic-7 Current  | IR_HARM_7        | Amper | Energy      |
|         | Phase S Harmonic-7 Current  | IS_HARM_7        | Amper | Energy      |
|         | Phase T Harmonic-7 Current  | IT_HARM_7        | Amper | Energy      |
|         | Average Harmonic-7 Current  | IA_HARM_7        | Amper | Energy      |
|         | Phase R Harmonic-8 Current  | IR_HARM_8        | Amper | Energy      |
|         | Phase S Harmonic-8 Current  | IS_HARM_8        | Amper | Energy      |
|         | Phase T Harmonic-8 Current  | IT_HARM_8        | Amper | Energy      |
|         | Average Harmonic-8 Current  | IA_HARM_8        | Amper | Energy      |
|         | Phase R Harmonic-9 Current  | IR_HARM_9        | Amper | Energy      |
|         | Phase S Harmonic-9 Current  | IS_HARM_9        | Amper | Energy      |
|         | Phase T Harmonic-9 Current  | IT_HARM_9        | Amper | Energy      |
|         | Average Harmonic-9 Current  | IA_HARM_9        | Amper | Energy      |
|         | Phase R Harmonic-10 Current | IR_HARM_10       | Amper | Energy      |
|         | Phase S Harmonic-10 Current | IS_HARM_10       | Amper | Energy      |
|         | Phase T Harmonic-10 Current | IT_HARM_10       | Amper | Energy      |
|         | Average Harmonic-10 Current | IA_HARM_10       | Amper | Energy      |
|         | Phase R Harmonic-11 Current | IR_HARM_11       | Amper | Energy      |
|         | Phase S Harmonic-11 Current | IS_HARM_11       | Amper | Energy      |
|         | Phase T Harmonic-11 Current | IT_HARM_11       | Amper | Energy      |
|         | Average Harmonic-11 Current | IA_HARM_11       | Amper | Energy      |
|         | Phase R Harmonic-12 Current | IR_HARM_12       | Amper | Energy      |
|         | Phase S Harmonic-12 Current | IS_HARM_12       | Amper | Energy      |
|         | Phase T Harmonic-12 Current | IT_HARM_12       | Amper | Energy      |
|         | Average Harmonic-12 Current | IA_HARM_12       | Amper | Energy      |
|         | Phase R Harmonic-13 Current | IR_HARM_13       | Amper | Energy      |
|         | Phase S Harmonic-13 Current | IS_HARM_13       | Amper | Energy      |
|         | Phase T Harmonic-13 Current | IT_HARM_13       | Amper | Energy      |
|         | Average Harmonic-13 Current | IA_HARM_13       | Amper | Energy      |
|         | Phase R Harmonic-14 Current | IR_HARM_14       | Amper | Energy      |
|         | Phase S Harmonic-14 Current | IS_HARM_14       | Amper | Energy      |
|         | Phase T Harmonic-14 Current | IT_HARM_14       | Amper | Energy      |
|         | Average Harmonic-14 Current | IA_HARM_14       | Amper | Energy      |
|         | Phase R Harmonic-15 Current | IR_HARM_15       | Amper | Energy      |
|         | Phase S Harmonic-15 Current | IS_HARM_15       | Amper | Energy      |
|         | Phase T Harmonic-15 Current | IT_HARM_15       | Amper | Energy      |
|         | Average Harmonic-15 Current | IA_HARM_15       | Amper | Energy      |
|         | Phase R Harmonic-16 Current | IR_HARM_16       | Amper | Energy      |
|         | Phase S Harmonic-16 Current | IS_HARM_16       | Amper | Energy      |
|         | Phase T Harmonic-16 Current | IT_HARM_16       | Amper | Energy      |
|         | Average Harmonic-16 Current | IA_HARM_16       | Amper | Energy      |
|         | Phase R Harmonic-17 Current | IR_HARM_17       | Amper | Energy      |
|         | Phase S Harmonic-17 Current | IS_HARM_17       | Amper | Energy      |
|         | Phase T Harmonic-17 Current | IT_HARM_17       | Amper | Energy      |
|         | Average Harmonic-17 Current | IA_HARM_17       | Amper | Energy      |
|         | Phase R Harmonic-18 Current | IR_HARM_18       | Amper | Energy      |
|         | Phase S Harmonic-18 Current | IS_HARM_18       | Amper | Energy      |
|         | Phase T Harmonic-18 Current | IT_HARM_18       | Amper | Energy      |
|         | Average Harmonic-18 Current | IA_HARM_18       | Amper | Energy      |
|         | Phase R Harmonic-19 Current | IR_HARM_19       | Amper | Energy      |
|         | Phase S Harmonic-19 Current | IS_HARM_19       | Amper | Energy      |
|         | Phase T Harmonic-19 Current | IT_HARM_19       | Amper | Energy      |
|         | Average Harmonic-19 Current | IA_HARM_19       | Amper | Energy      |
|         | Phase R Harmonic-20 Current | IR_HARM_20       | Amper | Energy      |
|         | Phase S Harmonic-20 Current | IS_HARM_20       | Amper | Energy      |
|         | Phase T Harmonic-20 Current | IT_HARM_20       | Amper | Energy      |
|         | Average Harmonic-20 Current | IA_HARM_20       | Amper | Energy      |
|         | Phase R Fund. ReActive Pwr. | QFUNDR           | -     | Energy      |
|         | Phase S Fund. ReActive Pwr. | QFUNDS           | -     | Energy      |
|         | Phase T Fund. ReActive Pwr. | QFUNDT           | -     | Energy      |
|         | Phase R Harm. ReActive Pwr. | QHARMR           | -     | Energy      |
|         | Phase S Harm. ReActive Pwr. | QHARMS           | -     | Energy      |
|         | Phase T Harm. ReActive Pwr. | QHARMT           | -     | Energy      |
|         | Phase R Active Power        | PR               | -     | Energy      |
|         | Phase S Active Power        | PS               | -     | Energy      |
|         | Phase T Active Power        | PT               | -     | Energy      |
|         | Average Active Power        | PA               | -     | Energy      |
|         | Phase R ReActive Power      | QR               | -     | Energy      |
|         | Phase S ReActive Power      | QS               | -     | Energy      |
|         | Phase T ReActive Power      | QT               | -     | Energy      |
|         | Average ReActive Power      | QA               | -     | Energy      |
|         | Phase R Apparent Power      | SR               | -     | Energy      |
|         | Phase S Apparent Power      | SS               | -     | Energy      |
|         | Phase T Apparent Power      | ST               | -     | Energy      |
|         | Average Apparent Power      | SA               | -     | Energy      |
|         | Phase R Fundamental Power   | PFUNDR           | -     | Energy      |
|         | Phase S Fundamental Power   | PFUNDS           | -     | Energy      |
|         | Phase T Fundamental Power   | PFUNDT           | -     | Energy      |
|         | Phase R Harmonic Power      | PHARMR           | -     | Energy      |
|         | Phase S Harmonic Power      | PHARMS           | -     | Energy      |
|         | Phase T Harmonic Power      | PHARMT           | -     | Energy      |
|         | Phase R PowerFactor         | PFR              | -     | Energy      |
|         | Phase S PowerFactor         | PFS              | -     | Energy      |
|         | Phase T PowerFactor         | PFT              | -     | Energy      |
|         | Average PowerFactor         | PFA              | -     | Energy      |
|         | Line Frequency              | FREQ             | Hz    | Energy      |
|         | Phase R Recieved P Energy   | WHR_POS          | -     | Energy      |
|         | Phase R Delivered P Energy  | WHR_NEG          | -     | Energy      |
|         | Phase S Recieved P Energy   | WHS_POS          | -     | Energy      |
|         | Phase S Delivered P Energy  | WHS_NEG          | -     | Energy      |
|         | Phase T Recieved P Energy   | WHT_POS          | -     | Energy      |
|         | Phase T Delivered P Energy  | WHT_NEG          | -     | Energy      |
|         | Phase R Recieved Q Energy   | VARHR_POS        | -     | Energy      |
|         | Phase R Delivered Q Energy  | VARHR_NEG        | -     | Energy      |
|         | Phase S Recieved Q Energy   | VARHS_POS        | -     | Energy      |
|         | Phase S Delivered Q Energy  | VARHS_NEG        | -     | Energy      |
|         | Phase T Recieved Q Energy   | VARHT_POS        | -     | Energy      |
|         | Phase T Delivered Q Energy  | VARHT_NEG        | -     | Energy      |
