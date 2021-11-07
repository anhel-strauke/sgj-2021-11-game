init:

    default map_info = ("", "")

    define hm = CharacterAt(hero)



    python:
        def map_marker(n):
            return "ui_images/map/map_m" + str(n) + ".png"
        
        def map_route(s):
            return "ui_images/map/map_r" + s + ".png"
    
    image map_bg = "ui_images/map/map_bg.png"
    image map_l_hand = "ui_images/map/map_l_hand.png"
    image map_r_hand = "ui_images/map/map_r_hand.png"

    define map_routes = {
        "1-2": {
            "from": 1,
            "to": 2,
            "p": ["1_2"]
        },
        "2-3": {
            "from": 2,
            "to": 3,
            "p": ["2_3_1", "2_3_2", "2_3_3"]
        },
        "3-4": {
            "from": 3,
            "to": 4,
            "p": ["3_4"]
        },
        "4-5": {
            "from": 4,
            "to": 5,
            "p": ["4_5_1", "4_5_2", "4_5_3"]
        },
        "5-6": {
            "from": 5,
            "to": 6,
            "p": ["5_6_1", "5_6_2"]
        },
        "6-7": {
            "from": 6,
            "to": 7,
            "p": ["6_7_1", "6_7_2", "6_7_3"]
        },
        "6-7-acc": {
            "from": 6,
            "to": 7,
            "p": ["6_7_1", "6_7_2", ("6_7_acc", "map_event_6_7"), "6_7_3"]
        },
        "7-8": {
            "from": 7,
            "to": 4,
            "p": ["7_8"]
        },
        "8-9": {
            "from": 4,
            "to": 9,
            "p": ["8_9_1", "8_9_2"]
        },
        "8-9-acc": {
            "from": 4,
            "to": 9,
            "p": ["8_9_1", ("8_9_acc", "map_event_8_9"), "8_9_2"]
        },
        "9-10": {
            "from": 9,
            "to": 10,
            "p": ["9_10_1", "9_10_2", "9_10_3"]
        },
        "10-11": {
            "from": 10,
            "to": 11,
            "p": ["10_11_1", "10_11_2"]
        },
        "11-12": {
            "from": 11,
            "to": 1,
            "p": ["11_12_1", "11_12_2"]
        }
    }

#     define map_points = {
#         1: {
#             "name": _("Квартира Мэллори"),
#             "pos": (629, 728)
#         },
#         2: {
#             "name": _("Аптека Амелинды"),
#             "pos": (799, 818)
#         },
#         3: {
#             "name": _("Эббот Роуд 15"),
#             "pos": (629, 351)
#         },
#         4: {
#             "name": _("Таксофон на Эббот"),
#             "pos": (736, 351)
#         },
#         5: {
#             "name": _("Броад Стрит 54"),
#             "pos": (416, 836)
#         },
#         6: {
#             "name": _("Городская площадь"),
#             "pos": (818, 580)
#         },
#         7: {
#             "name": _("Частный сектор \"Серенити 22\""),
#             "pos": (340, 325)
#         },
#         9: {
#             "name": _("Набережная Бьеншан 8"),
#             "pos": (1294, 885)
#         },
#         10: {
#             "name": _("Район Пахифеи 13384"),
#             "pos": (1469, 187)
#         },
#         11: {
#             "name": _("Мост через реку Спирит"),
#             "pos": (871, 459)
#         }
#     }
#     define map_routes = {
#         "1-2": {
#             "from": 1,
#             "to": 2,
#             "p": [(627, 743), (675, 752), (799, 836)]
#         },
#         "2-3": {
#             "from": 2,
#             "to": 3,
#             "p": [(1574, 1655), (1337, 1506), (1161, 1469), None, (1181, 1286), (1198, 1100), None, (1149, 1091), (1055, 708), (1268, 728)]
#         },
#         "3-4": {
#             "from": 3,
#             "to": 4,
#             "p": [(1251, 721), (1500, 724)]
#         },
#         "4-5": {
#             "from": 4,
#             "to": 5,
#             "p": [(1480, 741), (839, 688), (911, 1053), (850, 1046), None, (859, 1086), (838, 1269), None, (851, 1285), (824, 1420], (991, 1443), (942, 1714), (818, 1706)
#         },
#         "5-6": {
#             "from": 5,
#             "to": 6,
#             "p": [(816, 1703), (1110, 1737), (1189, 1315), (1335, 1334), (1370, 1132), (1606, 1174)]
#         },
#         "6-7": {
#             "from": 6,
#             "to": 7,
#             "p": [(1604, 1177), (1147, 1090), (1055, 706), (655, 674)]
#         },
#         "6-7-accident": {
#             "from": 6,
#             "to": 7,
#             "p": [(1604, 1177), (1147, 1090), (1055, 706), "map_accident_67", (1055, 706), (655, 674)]
#         },
#         "7-8": {
#             "from": 7,
#             "to": 4,
#             "p": [(654, 674), (1500, 724)]
#         },
#         "8-9": {
#             "from": 4,
#             "to": 9,
#             "p": [(1466, 742), (1627, 748), (1665, 873), (1672, 1025), (1662, 1126), (1689, 1180), ()]
#         }
#     }

# init -1 python:
#     import math

#     class LineSegment(object):
#         def __init__(self, ax, ay, bx=None, by=None):
#             try:
#                 if len(ax) == 2 and len(ay) == 2:
#                     bx, by = ay
#                     ax, ay = ax
#                 else:
#                     raise ValueError("points should have 2 coords")
#             except TypeError:
#                 pass
#             assert ax != bx or ay != by
#             self._ax = float(ax)
#             self._ay = float(ay)
#             self._bx = float(bx)
#             self._by = float(by)
#             self.length = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
#             self._vx = float(bx - ax)
#             self._vy = float(by - ay)
#             self.angle = math.degrees(math.acos((bx - ax) / self.length))
        
#         def __len__(self):
#             return self.length
        
#         def interpolate(t):
#             x = self._ax + self._vx * t
#             y = self._ay + self._vy * t
#             return (x, y)
        
#         def interp_p(l):
#             t = float(l) / self.length
#             return self.interpolate(t)

transform trans_map_marker_appear:
    align (0, 0)
    alpha 1.0
    0.4
    alpha 0.0
    0.4
    alpha 1.0
    0.4
    alpha 0.0
    0.4
    alpha 1.0

label map:
    $ route, next_label = map_info

    scene map_bg
    show map_l_hand:
        pos (136, 665)
    show map_r_hand:
        pos (1627, 628)
    with fade

    $ r = map_routes[route]
    $ marker_from = Image(map_marker(r["from"]))
    $ marker_to = Image(map_marker(r["to"]))
    show expression marker_from at trans_map_marker_appear
    pause 1.2
    show expression marker_from:
        align (0, 0) alpha 1
    pause 0.5
    show expression marker_to at trans_map_marker_appear
    pause 1.2
    show expression marker_to:
        align (0, 0) alpha 1
    pause 0.5

    show map_l_hand:
        linear 0.5 pos (136, 1080)
    show map_r_hand:
        linear 0.5 pos (1627, 1080)

    pause 0.5
    hide map_r_hand
    hide map_l_hand

    pause 1.0

    $ route_index = 0
    while route_index < len(r["p"]):
        $ route_part = r["p"][route_index]
        if type(route_part) is tuple:
            $ part_id, label_to_call = route_part
            show expression map_route(part_id) at trans_map_marker_appear
            with hpunch
            pause 1.2
            show expression map_route(part_id):
                align (0, 0) alpha 1.0
            call expression label_to_call from _call_expression
        else:
            show expression map_route(route_part):
                align (0, 0)
            with None
            pause 1.0
        $ route_index += 1
    
    show expression marker_to at trans_map_marker_appear
    pause 1.2
    show expression marker_to:
        align (0, 0) alpha 1
    pause 0.5

    pause 1.0

    jump expression next_label
    
label map_event_6_7:
    define driver = CharacterAt(hero, name=_("Водитель"))

    driver "Сильно ушиблись?"

    hm "Я в порядке, не волнуйтесь."
    hm "Если бы не сгруппировалась, было бы гораздо хуже…"

    driver "Ваш парокат?"

    hm "Он… Кажется, не заводится."

    driver "Я вижу, двигатель сильно поврежден."
    driver "Давайте я помогу вам закинуть его в багажник. Довезу вас до ближайшего паромонтажа."

    hm "Я благодарю вас. Надеюсь, я не сильно опоздаю к следующей доставке."

    pause 1.0

    hm "Почему всё не может быть идеально?"
    $ Myo_value = 0
    $ money_value = 0

    pause 1.0

    return

label map_event_8_9:
    driver "Сильно ушиблись?"

    hm "Я в порядке, не волнуйтесь."
    hm "Если бы не сгруппировалась, было бы гораздо хуже…"

    driver "Ваш парокат?"

    hm "С виду нормально. Пара царапин, не более."

    driver "Что это торчит из вашей сумки? Похоже на какую-то траву, или плюш?"

    hm "Это же…"
    hm "О, нет! Это кукла, которую я должна сейчас доставить ребенку…"
    hm "Наверное, она вывалилась из сумки во время падения и зацепилась за что-то…"

    driver "Ясно. Ну, удачи вам с этим, леди."
    driver "Мне нужно ехать, а то у меня в машине женщина скоро родит."
    $ Myo_value = 0
    $ doll_broken = True

    pause 1.0

    return