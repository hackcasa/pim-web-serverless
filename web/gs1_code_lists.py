
class Allergen():
    CONTAINMENT_LEVEL = {
        "CONTAINS": "Innehåller",
        "MAY_CONTAIN": "Kan innehålla",
        "FREE_FROM": "Fri från"
    }

    TYPE = {
        "AC": "Kräftdjur",
        "AE": "Ägg",
        "AF": "Fisk",
        "AM": "Mjölk",
        "AN": "Nötter (eng: tree nuts)",
        "AP": "Jordnötter",
        "AS": "Sesamfrön",
        "AU": "Svaveldioxid eller sulfit",
        "AW": "Spannmål som innehåller gluten",
        "AY": "Sojabönor",
        "BC": "Selleri",
        "BM": "Senap",
        "GB": "Korn",
        "GK": "Kamut",
        "GO": "Havre",
        "GS": "Spelt",
        "ML": "Laktos",
        "NL": "Lupin",
        "NR": "Råg",
        "SA": "Mandel",
        "SC": "Cashewnöt",
        "SH": "Hasselnöt",
        "SM": "Makadamianöt",
        "SP": "Pekannöt",
        "SQ": "Queenslandsnöt",
        "SR": "Paranöt",
        "ST": "Pistaschmandel",
        "SW": "Valnöt",
        "UM": "Blötdjur",
        "UW": "Vete"
    }

    @staticmethod
    def valid_keys(allergen):
        return (allergen['type_code'] in Allergen.TYPE and
                allergen[
                    'containment_level_code'] in Allergen.CONTAINMENT_LEVEL)

    @staticmethod
    def get_text(allergen):
        if Allergen.valid_keys(allergen):
            return (Allergen.CONTAINMENT_LEVEL[
                allergen['containment_level_code']
            ] +
                " " +
                Allergen.TYPE[
                allergen['type_code']
            ])
        else:
            return (allergen['containment_level_code'] +
                    " " +
                    allergen['type_code'])


class FishingZone:
    AREA = (
        (0, "Not Set"),
        (18, "Norra ishavet"),
        (21, "Nordvästatlanten"),
        (27, "Nordostatlanten"),
        (31, "Västra mellersta Atlanten"),
        (34, "Östra mellersta Atlanten"),
        (37, "Medelhavet och Svarta havet"),
        (41, "Sydvästra Atlanten"),
        (47, "Sydöstra Atlanten"),
        (48, "Atlanten, Antarktis"),
        (51, "Västindiska Oceanen"),
        (57, "Östindiska Oceanen"),
        (58, "Södra indiska oceanen, Antarktis"),
        (61, "Nordvästra stillahavet"),
        (67, "Nordöstra stillahavet"),
        (71, "Västra mellersta stillahavet"),
        (77, "Östra mellersta stillahavet"),
        (81, "Sydvästra stillahavet"),
        (87, "Sydöstra stillahavet"),
        (88, "Stillahavet, Antarktis")
    )


class Origin:
    COUNTRY = (
        (0, "Not Set"),
        (1, "Global marknad"),
        (4, "Afghanistan"),
        (8, "Albanien"),
        (10, "Antarktis"),
        (12, "Algeriet"),
        (16, "Amerikanska Samoa"),
        (20, "Andorra"),
        (24, "Angola"),
        (28, "Antigua och Barbuda"),
        (31, "Azerbajdzjan"),
        (32, "Argentina"),
        (36, "Australien"),
        (40, "Österrike"),
        (44, "Bahamas"),
        (48, "Bahrain"),
        (50, "Bangladesh"),
        (51, "Armenien"),
        (52, "Barbados"),
        (56, "Belgien"),
        (60, "Bermuda"),
        (64, "Bhutan"),
        (68, "Bolivia"),
        (70, "Bosnien och Hercegovina"),
        (72, "Botswana"),
        (74, "Bouvetön"),
        (76, "Brasilien"),
        (84, "Belize"),
        (86, "Brittiska territoriet i Indiska Oceanen"),
        (90, "Salomonöarna"),
        (92, "Brittiska Jungfruöarna"),
        (96, "Brunei"),
        (97, "Europeiska unionen"),
        (100, "Bulgarien"),
        (104, "Burma"),
        (108, "Burundi"),
        (112, "Vitryssland"),
        (116, "Kambodja"),
        (120, "Kamerun"),
        (124, "Kanada"),
        (132, "Kap Verde"),
        (136, "Caymanöarna"),
        (140, "Centralafrikanska republiken"),
        (144, "Sri Lanka"),
        (148, "Tchad"),
        (152, "Chile"),
        (156, "Kina"),
        (158, "Taiwan"),
        (162, "Julön"),
        (166, "Kokosöarna"),
        (170, "Colombia"),
        (174, "Komorerna"),
        (175, "Mayotte"),
        (178, "Kongo-Brazzaville"),
        (184, "Cooköarna"),
        (180, "Kongo-Kinshasa"),
        (188, "Costa Rica"),
        (191, "Kroatien"),
        (192, "Kuba"),
        (196, "Cypern"),
        (203, "Tjeckien"),
        (204, "Benin"),
        (208, "Danmark"),
        (231, "Etiopien"),
        (212, "Dominica"),
        (214, "Dominikanska republiken"),
        (218, "Ecuador"),
        (222, "El Salvador"),
        (226, "Ekvatorialguinea"),
        (232, "Eritrea"),
        (233, "Estland"),
        (234, "Färöarna"),
        (238, "Falklandsöarna"),
        (239, "Sydgeorgien och Sydsandwichöarna"),
        (242, "Fiji"),
        (246, "Finland"),
        (249, "France métropolitaine (Frankrike, europeiska delen)"),
        (248, "Åland"),
        (250, "Frankrike"),
        (254, "Franska Guyana"),
        (258, "Franska Polynesien"),
        (260, "Franska södra territorierna"),
        (262, "Djibouti"),
        (266, "Gabon"),
        (268, "Georgien"),
        (270, "Gambia"),
        (275, "Palestinskt territorium, ockuperat"),
        (276, "Tyskland"),
        (288, "Ghana"),
        (292, "Gibraltar"),
        (296, "Kiribati"),
        (300, "Grekland"),
        (304, "Grönland"),
        (308, "Grenada"),
        (312, "Guadeloupe"),
        (316, "Guam"),
        (320, "Guatemala"),
        (324, "Guinea"),
        (328, "Guyana"),
        (332, "Haiti"),
        (334, "Heard- och McDonaldsöarna"),
        (336, "Vatikanstaten"),
        (340, "Honduras"),
        (344, "Hongkong"),
        (348, "Ungern"),
        (352, "Island"),
        (356, "Indien"),
        (360, "Indonesien"),
        (364, "Iran"),
        (368, "Irak"),
        (372, "Irland"),
        (376, "Israel"),
        (380, "Italien"),
        (384, "Elfenbenskusten"),
        (388, "Jamaica"),
        (392, "Japan"),
        (398, "Kazakstan"),
        (400, "Jordanien"),
        (404, "Kenya"),
        (408, "Nordkorea"),
        (410, "Sydkorea"),
        (414, "Kuwait"),
        (417, "Kirgizistan"),
        (418, "Laos"),
        (422, "Libanon"),
        (426, "Lesotho"),
        (428, "Lettland"),
        (430, "Liberia"),
        (434, "Libyen"),
        (438, "Liechtenstein"),
        (440, "Litauen"),
        (442, "Luxemburg"),
        (446, "Macau"),
        (450, "Madagaskar"),
        (454, "Malawi"),
        (458, "Malaysia"),
        (462, "Maldiverna"),
        (466, "Mali"),
        (470, "Malta"),
        (474, "Martinique"),
        (478, "Mauretanien"),
        (480, "Mauritius"),
        (484, "Mexiko"),
        (492, "Monaco"),
        (496, "Mongoliet"),
        (498, "Moldavien"),
        (499, "Montenegro"),
        (500, "Montserrat"),
        (504, "Marocko"),
        (508, "Moçambique"),
        (512, "Oman"),
        (516, "Namibia"),
        (520, "Nauru"),
        (524, "Nepal"),
        (528, "Nederländerna"),
        (530, "Nederländska Antillerna"),
        (533, "Aruba"),
        (540, "Nya Kaledonien"),
        (548, "Vanuatu"),
        (554, "Nya Zeeland"),
        (558, "Nicaragua"),
        (562, "Niger"),
        (566, "Nigeria"),
        (570, "Niue"),
        (574, "Norfolkön"),
        (578, "Norge"),
        (580, "Nordmarianerna"),
        (581, "USA:s yttre öar"),
        (583, "Mikronesiska federationen"),
        (584, "Marshallöarna"),
        (585, "Palau"),
        (586, "Pakistan"),
        (591, "Panama"),
        (598, "Papua Nya Guinea"),
        (600, "Paraguay"),
        (604, "Peru"),
        (608, "Filippinerna"),
        (612, "Pitcairnöarna"),
        (616, "Polen"),
        (620, "Portugal"),
        (624, "Guinea Bissau"),
        (626, "Östtimor"),
        (630, "Puerto Rico"),
        (634, "Qatar"),
        (638, "Réunion"),
        (642, "Rumänien"),
        (643, "Ryssland"),
        (646, "Rwanda"),
        (652, "Saint Barthélemy"),
        (654, "Sankta Helena"),
        (659, "Saint Kitts och Nevis"),
        (660, "Anguilla"),
        (662, "Saint Lucia"),
        (663, "Saint Martin, Frankrike"),
        (666, "Saint-Pierre och Miquelon"),
        (670, "Saint Vincent och Grenadinerna"),
        (674, "San Marino"),
        (678, "São Tomé och Príncipe"),
        (682, "Saudiarabien"),
        (686, "Senegal"),
        (688, "Serbien"),
        (690, "Seychellerna"),
        (694, "Sierra Leone"),
        (702, "Singapore"),
        (703, "Slovakien"),
        (704, "Vietnam"),
        (705, "Slovenien"),
        (706, "Somalia"),
        (710, "Sydafrika"),
        (716, "Zimbabwe"),
        (724, "Spanien"),
        (732, "Västsahara"),
        (736, "Sudan"),
        (740, "Surinam"),
        (744, "Svalbard och Jan Mayen"),
        (748, "Swaziland"),
        (752, "Sverige"),
        (756, "Schweiz"),
        (760, "Syrien"),
        (762, "Tadzjikistan"),
        (764, "Thailand"),
        (768, "Togo"),
        (772, "Tokelauöarna"),
        (776, "Tonga"),
        (780, "Trinidad och Tobago"),
        (784, "Förenade Arabemiraten"),
        (788, "Tunisien"),
        (792, "Turkiet"),
        (795, "Turkmenistan"),
        (796, "Turks- och Caicosöarna"),
        (798, "Tuvalu"),
        (800, "Uganda"),
        (804, "Ukraina"),
        (807, "Makedonien"),
        (818, "Egypten"),
        (826, "Storbritannien"),
        (831, "Guernsey"),
        (832, "Jersey"),
        (833, "Isle of Man"),
        (834, "Tanzania"),
        (840, "USA"),
        (850, "Amerikanska Jungfruöarna"),
        (854, "Burkina Faso"),
        (858, "Uruguay"),
        (860, "Uzbekistan"),
        (862, "Venezuela"),
        (876, "Wallis- och Futunaöarna"),
        (882, "Samoa"),
        (887, "Jemen"),
        (894, "Zambia"),
    )


class T3780:
    UNIT_CODES = {
        "1N": "Count",
        "1S": "Milligram per Kilogram (mg/kg)",
        "23": "Grams Per Cubic Centimetre",
        "28": "Kilogram per square metre",
        "2L": "Cubic Foot Per Minute",
        "2M": "Centimetre Per Second",
        "2N": "Decibel",
        "2P": "Kilobyte",
        "2Q": "Kilo Becquerel",
        "2X": "Metre Per Minute",
        "4G": "Microlitre",
        "4H": "Micrometre",
        "4L": "Megabyte",
        "4N": "Megabecquerel",
        "58": "Net kilogram",
        "59": "Part per million",
        "5B": "Batch",
        "64": "Pound per square inch - Gauge",
        "80": "Pound per square inch - Absolute",
        "A11": "Angstrom",
        "A24": "Candela per Square Metre",
        "A43": "Deadweight Tonnage",
        "A71": "Femtometre",
        "A86": "Gigahertz",
        "AD": "Byte",
        "AMH": "Ampere Hour",
        "AMP": "Ampere",
        "ANN": "Year",
        "APZ": "Troy ounce or apothecary ounce",
        "AS": "Assortment",
        "ATM": "Standard Atmosphere",
        "ATT": "Technical Atmosphere",
        "AWG": "Gauge",
        "AXU": "Anti XA Unit",
        "B10": "Bit per second",
        "B37": "Kilogram Force",
        "B47": "Kilonewton",
        "B60": "Lumens per Square Meter",
        "B61": "Lumens Per Watt",
        "B62": "Lumen Seconds",
        "B64": "Lux Seconds",
        "BAR": "Bar (unit of pressure)",
        "BB": "Base box",
        "BFT": "Board Foot",
        "BLL": "Barrel US",
        "BP": "Hundred board foot",
        "BPM": "Beats Per Minute",
        "BQL": "Becquerel",
        "BTU": "British thermal unit",
        "BUA": "Bushel (US)",
        "BUI": "Bushel (UK)",
        "C16": "Millimetre Per Second",
        "C18": "Millimole",
        "C26": "Millisecond",
        "C34": "Mole",
        "C45": "Nanometre",
        "C47": "Nano Seconds",
        "C52": "Picometre",
        "C65": "Pascal Seconds",
        "C75": "Picowatt",
        "CEL": "Degree Celsius",
        "CFU": "Colony Forming Units",
        "CG": "Card",
        "CGM": "Centigram",
        "CLT": "Centilitre",
        "CMK": "Square centimetre",
        "CMQ": "Cubic centimetre",
        "CMT": "Centimetre",
        "CTM": "Metric Carat",
        "CWA": "Hundred pound (cwt) / hundred weight (US)",
        "CWI": "Hundred weight (UK)",
        "D03": "Kilowatt / hour",
        "D19": "Square Metre Kelvin Per Watt",
        "D29": "Terahertz",
        "D30": "Terajoule",
        "D32": "Terawatt hour",
        "D40": "Thousand Litre",
        "D43": "Atomic Mass Units (AMU)",
        "D5": "Kilogram per square centimetre",
        "D55": "Heat Transfer Coefficient",
        "D63": "Book",
        "D70": "Calorie - International Table (IT)",
        "DAY": "Days",
        "DD": "Degree (Unit of Angle)",
        "DG": "Decigram",
        "DLT": "Decilitre",
        "DMK": "Square decimetre",
        "DMQ": "Cubic decimetre",
        "DMT": "Decimetre",
        "DRA": "Dram (US)",
        "DRI": "Dram (UK)",
        "DZN": "Dozen",
        "E09": "Milliampere hour",
        "E14": "Kilocalorie",
        "E27": "Dose",
        "E32": "Litre Per Hour",
        "E34": "Gigabyte",
        "E35": "Terabyte",
        "E36": "Petabyte",
        "E37": "Pixel",
        "E39": "Dots per inch",
        "E4": "Gross kilogram",
        "E55": "Use",
        "EA": "Each",
        "ELU": "ELISA Units",
        "F27": "Gram Per Hour",
        "FAH": "Degree Fahrenheit",
        "FH": "Micromole",
        "FJ": "Sizing Factor",
        "FOT": "Foot",
        "FP": "Pound per square foot",
        "FR": "Foot Per Minute",
        "FS": "Foot Per Second",
        "FTK": "Square foot",
        "FTQ": "Cubic foot",
        "G2": "US Gallon Per Minute",
        "G21": "Cup (US)",
        "G23": "Peck",
        "G24": "Tablespoon",
        "G25": "Teaspoon",
        "G26": "Stere",
        "GBQ": "Gigabecquerel",
        "GFI": "Gram of Fissile Isotope",
        "GL": "Gram Per Litre",
        "GLI": "Gallon (UK)",
        "GLL": "Gallon (US)",
        "GM": "Gram per square metre",
        "GRM": "Gram",
        "GRN": "Grain",
        "GRO": "Gross",
        "GWH": "Gigawatt hour",
        "H49": "Centimetre Per Hour",
        "H67": "Millimetre Per Hour",
        "H79": "French gauge",
        "H81": "Millimetre Per Minute",
        "H87": "Piece",
        "HC": "Hundred count",
        "HD": "Half dozen",
        "HEP": "Histamine Equivalent Prick",
        "HGM": "Hectogram",
        "HLT": "Hectolitre",
        "HM": "Mile Per Hour (statute mile)",
        "HTZ": "Hertz",
        "HUR": "Hour",
        "INH": "Inches",
        "INK": "Square inch",
        "INQ": "Cubic inch",
        "IU": "Inch Per Second",
        "JOU": "Joule",
        "K14": "Foot Per Hour",
        "K30": "Gallon (US liquid) Per Second",
        "K43": "Horsepower",
        "K6": "Kilolitre",
        "KDW": "Kilogram drained net weight",
        "KGM": "Kilogram",
        "KHY": "Kilogram of hydrogen peroxide",
        "KHZ": "Kilohertz",
        "KIU": "Kallikrein inactivator unit.",
        "KJO": "Kilojoule",
        "KMA": "Kilogram of methylamine",
        "KMH": "Kilometre Per Hour",
        "KMT": "Kilometre",
        "KNI": "Kilogram of nitrogen",
        "KNM": "Kilonewton Per Square Metre",
        "KNT": "Knot",
        "KO": "The milliequivalence caustic potash per gram of product",
        "KPA": "Kilopascal- a thousand pascals (10 to the 3rd power)",
        "KPH": "Kilogram of potassium hydroxide (caustic potash)",
        "KPO": "Kilogram of potassium oxide",
        "KPP": "Kilogram of phosphorus pentoxide (phosphoric anhydride)",
        "KSD": "Kilogram of substance 90% dry",
        "KSH": "Kilogram of sodium hydroxide (caustic soda)",
        "KT": "Kit",
        "KUR": "Kilogram of Uranium",
        "KWH": "Kilowatt hour",
        "KWT": "Kilowatt",
        "LBR": "Pound",
        "LD": "Litre / Day",
        "LF": "Linear foot",
        "LK": "Link",
        "LM": "Linear metre",
        "LPA": "Litre of pure alcohole",
        "LR": "Layer",
        "LTN": "Ton (UK) or long ton (US)",
        "LTR": "Litre",
        "LUX": "Lux",
        "M57": "Mile Per Minute",
        "M58": "Mile Per Second",
        "M60": "Metre Per Hour",
        "M62": "Kilometre Per Second",
        "M63": "Inch Per Minute",
        "M64": "Yard Per Second",
        "M65": "Yard Per Minute",
        "M66": "Yard Per Hour",
        "MAW": "Megawatt",
        "MBR": "Millibar",
        "MC": "Microgram",
        "MEQ": "Milliequivalents",
        "MGM": "Milligram",
        "MHZ": "Megahertz",
        "MIK": "Square mile",
        "MIN": "Minute (unit of time)",
        "MIU": "Million International Unit (NIE)",
        "MLT": "Millilitre",
        "MMK": "Square millimetre",
        "MMQ": "Cubic millimetre",
        "MMT": "Millimetre",
        "MON": "Month",
        "MPN": "Most Probable Number",
        "MQH": "Cubic Metre Per Hour",
        "MTK": "Square metre",
        "MTQ": "Cubic metre",
        "MTR": "Metre",
        "MTS": "Metre Per Second",
        "MWH": "Megawatt hour (1000 kW.h)",
        "NCL": "Number of cells",
        "NEW": "Newton",
        "NIU": "Number of International Units",
        "NPR": "Number of pairs",
        "NU": "Newton Metre",
        "OHM": "Ohm",
        "ON": "Ounces per square yard",
        "ONZ": "Ounce",
        "OPM": "Oscillations Per Minute",
        "OZA": "Fluid ounce (US)",
        "OZI": "Fluid ounce (UK)",
        "P1": "Percent",
        "PAL": "Pascal",
        "PD": "Pad",
        "PFU": "Plaque Forming unit(s)",
        "PNT": "Point",
        "PR": "Pair",
        "PRS": "Potential Renal Solute Load",
        "PS": "Pound-force per square inch",
        "PTD": "Dry Pint (US)",
        "PTI": "Pint (UK)",
        "PTL": "Liquid pint (US)",
        "PTN": "Portion:",
        "Q30": "pH (potential of Hydrogen)",
        "Q32": "Femtolitre",
        "Q33": "Picolitre",
        "Q34": "Nanolitre",
        "QB": "Page - hardcopy",
        "QTD": "Quart (US dry)",
        "QTL": "Liquid quart (US)",
        "R9": "Thousand cubic metre",
        "RPM": "Revolutions Per Minute",
        "S4": "Square Metre / Second",
        "SEC": "Second (unit of time)",
        "SET": "Set",
        "SMI": "Mile (statute mile)",
        "SQE": "SQ-E",
        "STN": "Ton (US) or short ton (UK)",
        "SX": "Shipment",
        "T3": "Thousand piece",
        "TNE": "Tonne",
        "TPI": "Teeth Per Inch",
        "U2": "Tablet",
        "UA": "Torr",
        "VLT": "Volt",
        "WEE": "Week",
        "WHR": "Watt hour",
        "WTT": "Watt",
        "XRE": "Retinol Equivalent (RE)",
        "XRO": "Roll",
        "XST": "Sheet",
        "X_CCA": "Cold Cramp Amp",
        "X_CFG": "Colony Forming Units per gram (CFU/g)",
        "X_CFP": "Colony Forming Units per Pound (CFU/lb)",
        "X_CHD": "Centisimal Hahnemannian Dilution (CH)",
        "X_DBA": "Decibar",
        "X_DWT": "Penny Weight",
        "X_HIN": "Hundredths of an Inch",
        "X_IUK": "International Units per Kilogram (IU/kg)",
        "X_KVN": "Korsakovian (K)",
        "X_MLM": "Millesimai (LM)",
        "X_MPG": "Miles Per Gallon",
        "X_MTC": "Mother tincture (Dry material)",
        "X_NGM": "Nanogram",
        "X_PPC": "Pixel per centimetre",
        "X_PPI": "Pixel per inch",
        "X_RAE": "Retinol Activity Equivalents",
        "X_SIN": "Thirty Seconds of an Inch",
        "X_SPS": "Sample per second",
        "X_UIN": "Ten Thousandths of an Inch",
        "YDK": "Square Yard",
        "YRD": "Yard",
    }
