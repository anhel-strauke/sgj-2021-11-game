init:

    default map_info = ("", "")

    define hm = CharacterAt(hero)
    define driver = CharacterAt(hero, name=_("Водитель"))

    define map_points = {
        1: {
            "name": _("Квартира Мэллори"),
            "pos": (629, 728)
        },
        2: {
            "name": _("Аптека Амелинды"),
            "pos": (799, 818)
        },
        3: {
            "name": _("Эббот Роуд 15"),
            "pos": (629, 351)
        },
        4: {
            "name": _("Таксофон на Эббот"),
            "pos": (736, 351)
        },
        5: {
            "name": _("Броад Стрит 54"),
            "pos": (416, 836)
        },
        6: {
            "name": _("Городская площадь"),
            "pos": (818, 580)
        },
        7: {
            "name": _("Частный сектор \"Серенити 22\""),
            "pos": (340, 325)
        },
        9: {
            "name": _("Набережная Бьеншан 8"),
            "pos": (1294, 885)
        },
        10: {
            "name": _("Район Пахифеи 13384"),
            "pos": (1469, 187)
        },
        11: {
            "name": _("Мост через реку Спирит"),
            "pos": (871, 459)
        }
    }

    define map_routes = {
        "1-2": {
            "from": 1,
            "to": 2,
            "p": [(627, 743), (675, 750), (804, 830)]
        },
        "2-3": {
            "from": 2,
            "to": 3,
            "p": [
                (794, 833), (668, 754), None, (664, 748), (581, 735), (596, 656), None, (589, 651), (599, 548), 
                None, (573, 547), (527, 354), (630, 363)
            ]
        },
        "3-4": {
            "from": 3,
            "to": 4,
            "p": [(617, 360), (755, 373)]
        },
        "4-5": {
            "from": 4,
            "to": 5,
            "p": [
                (755, 373), (418, 343), (455, 527), (429, 523), (421, 634), None, (425, 641), (413, 710), (493, 721), 
                (470, 859), (409, 853)
            ]
        },
        "5-6": {
            "from": 5,
            "to": 6,
            "p": [(408, 854), (554, 869), (595, 658), (669, 669), (685, 567), (798, 586)]
        },
        "6-7": {
            "from": 6,
            "to": 7,
            "p": [(804, 588), (575, 548), (528, 353), (329, 337)]
        },
        "6-7-acc": {
            "from": 6,
            "to": 7,
            "p": [(804, 588), (575, 548), (528, 353), "map_event_6_7", (528, 353), (329, 337)]
        },
        "7-8": {
            "from": 7,
            "to": 4,
            "p": [(338, 338), (737, 370)]
        },
        "8-9": {
            "from": 4,
            "to": 9,
            "p": [
                (734, 370), (812, 377), (832, 435), (837, 492), (833, 565), (843, 588), (824, 607), (827, 629),
                (886, 662), (919, 631), (1291, 901)
            ]
        },
        "8-9-acc": {
            "from": 4,
            "to": 9,
            "p": [
                (734, 370), (812, 377), (832, 435), (837, 492), (833, 565), (843, 588), (824, 607), (827, 629), 
                (886, 662), (919, 631), "map_event_8_9", (919, 631), (1291, 901)
            ]
        },
        "9-10": {
            "from": 9,
            "to": 10,
            "p": [
                (1296, 906), (927, 634), None, (917, 628), (907, 598), None, (912, 585), (930, 547), (965, 514), None, 
                (973, 511), (1027, 491), (1087, 488),
                (1101, 347), (1471, 203)
            ]
        },
        "10-11": {
            "from": 10,
            "to": 11,
            "p": [(1471, 203), (945, 405), (989, 502), (952, 519), (924, 450), (885, 470)]
        },
        "11-12": {
            "from": 11,
            "to": 1,
            "p": [
                (861, 466), (836, 486), (833, 563), (843, 587), (816, 614), (799, 652), (762, 682), (716, 677), None,
                (710, 687), (666, 751), (618, 741)
            ]
        }
    }

    image map_bg:
        "ui_images/map/map_bg.png"
        anchor (0, 0)
        pos (51, 0)
    
    image map_road_left = "ui_images/map/map_road_left.png"
    image map_road_right = "ui_images/map/map_road_right.png"

    image map_road = Composite(
        (1920, 2160 * 2), 
        (0, 0), "map_road_left", 
        (0, 2160), "map_road_left", 
        (1816, 0), "map_road_right", 
        (1816, 2160), "map_road_right"
    )
    

    image map_l_hand = "ui_images/map/map_l_hand.png"
    image map_r_hand = "ui_images/map/map_r_hand.png"

    image map_marker_image:
        "ui_images/map/map_marker.png"
        xanchor 91 yanchor 119
    
    image map_segment_image:
        "ui_images/map/map_tick.png"
        anchor (20, 5)
    
    image map_event_image:
        "ui_images/map/map_event.png"
        anchor (42, 36)

    define map_segment_length = 50
    define map_segment_initial_shift = 20
    define map_segment_delay = 0.3

init -1 python:
    import math

    class LineSegment(object):
        def __init__(self, ax, ay, bx=None, by=None):
            try:
                if len(ax) == 2 and len(ay) == 2:
                    bx, by = ay
                    ax, ay = ax
                else:
                    raise ValueError("points should have 2 coords")
            except TypeError:
                pass
            assert ax != bx or ay != by
            self._ax = float(ax)
            self._ay = float(ay)
            self._bx = float(bx)
            self._by = float(by)
            self.length = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
            self._vx = float(bx - ax)
            self._vy = float(by - ay)
            self.angle = math.degrees(math.acos((ax - bx) / self.length))
            if by > ay:
                self.angle = -self.angle
        
        def __len__(self):
            return self.length
        
        def interpolate(self, t):
            x = self._ax + self._vx * t
            y = self._ay + self._vy * t
            return (x, y)
        
        def interp_p(self, l):
            t = float(l) / self.length
            return self.interpolate(t)
    
    def map_build_segment(p_from, p_to, init_delay):
        sg = LineSegment(p_from, p_to)
        n_segments = int(round(len(sg) / float(map_segment_length)))
        n_segments = max(n_segments, 1)
        line_pos = map_segment_initial_shift if len(sg) > map_segment_length else len(sg) / 2.0
        seg_delay = init_delay
        segments_appear = []
        segments_fix = []
        cw_angle = sg.angle
        print("Line from (%f, %f) to (%f, %f), length %f, n_segments %d" % (p_from[0], p_from[1], p_to[0], p_to[1], sg.length, n_segments))
        for i in xrange(n_segments):
            seg_pos = sg.interp_p(line_pos)
            seg_pos = (int(seg_pos[0]), int(seg_pos[1]))
            segment_appear_img = At("map_segment_image", trans_map_segment_appear(seg_pos, cw_angle, seg_delay))
            segment_fix_img = At("map_segment_image", trans_map_segment_fix(seg_pos, cw_angle))
            print("Segment %d: delay %f, line_pos %f, cw_angle %f, pos (%f, %f)" % (i, seg_delay, line_pos, cw_angle, seg_pos[0], seg_pos[1]))
            line_pos += map_segment_length
            seg_delay += map_segment_delay
            segments_appear.append(segment_appear_img)
            segments_fix.append(segment_fix_img)
        return (segments_appear, segments_fix, seg_delay)

    def map_make_stages(route_id):
        global map_points, map_routes
        from_marker = None
        to_marker = None
        route_stages = []
        
        try:
            route = map_routes[route_id]
            from_marker_desc = map_points[route["from"]]
            to_marker_desc = map_points[route["to"]]
            route_points = route["p"]
            stage_segments_appear = []
            stage_segments_fix = []

            route_point_from = None
            seg_delay = 0.0
            for point in route_points:
                if type(point) is str:
                    route_stages.append({
                        "appear": stage_segments_appear,
                        "fix": stage_segments_fix,
                        "event_pos": route_point_from,
                        "event_label": point
                    })
                    stage_segments_appear = []
                    stage_segments_fix = []
                    seg_delay = 0
                    continue
                if point is None:
                    route_point_from = None
                    continue
                if route_point_from is None:
                    route_point_from = point
                    continue
                if route_point_from == point:
                    continue
                curr_segments_appear, curr_segments_fix, seg_delay = map_build_segment(route_point_from, point, seg_delay)
                stage_segments_appear += curr_segments_appear
                stage_segments_fix += curr_segments_fix
                route_point_from = point
            if stage_segments_appear:
                route_stages.append({
                    "appear": stage_segments_appear,
                    "fix": stage_segments_fix,
                    "event_pos": None,
                    "event_label": None
                })
            
            return (from_marker_desc, to_marker_desc, route_stages)

        except KeyError as e:
            print(str(e))
            return (None, None, [])
    
    def map_show_stage(stage, stage_fix, stage_index):
        assert len(stage) == len(stage_fix)
        for (i, img) in enumerate(stage):
            tag_name = "map_segment_%d_%d" % (stage_index, i)
            renpy.show(tag_name, what=img, tag=tag_name, behind=["map_from_marker", "map_to_marker"])
        delay_t = len(stage) * map_segment_delay
        renpy.pause(delay_t + 0.5)
        for (i, img) in enumerate(stage_fix):
            tag_name = "map_segment_%d_%d" % (stage_index, i)
            renpy.show(tag_name, what=img, tag=tag_name, behind=["map_from_marker", "map_to_marker"])

transform trans_map_marker_appear(position):
    pos position
    alpha 1.0
    block:
        0.4
        alpha 0.0
        0.4
        alpha 1.0
        repeat 4
        

transform trans_map_marker_fix(position):
    pos position
    alpha 1.0

transform trans_map_segment_appear(position, rot_angle, appear_delay):
    anchor (0.5, 0.5)
    pos position
    rotate rot_angle
    rotate_pad False
    alpha 0.0
    appear_delay
    linear 0.1 alpha 1.0

transform trans_map_segment_fix(position, rot_angle, apppear_delay=0):
    anchor (0.5, 0.5)
    pos position
    rotate rot_angle
    rotate_pad False
    alpha 1.0

transform trans_map_road_show:
    anchor (0, 0)
    pos (0, -2160)

transform trans_map_road_move:
    anchor (0, 0)
    linear 0.5 ypos 0
    ypos -2160
    repeat

transform trans_map_road_stop:
    anchor (0, 0)

label map:
    $ route, next_label = map_info

    scene black
    show map_road at trans_map_road_show
    show map_bg
    show map_l_hand:
        pos (136, 665)
    show map_r_hand:
        pos (1627, 628)
    with fade

    $ (marker_from, marker_to, route_stages) = map_make_stages(route)

    show map_marker_image at trans_map_marker_appear(marker_from["pos"]) as map_from_marker
    pause 2.4
    show map_marker_image at trans_map_marker_fix(marker_from["pos"]) as map_from_marker
    pause 0.5
    show map_marker_image at trans_map_marker_appear(marker_to["pos"]) as map_to_marker
    pause 2.4
    show map_marker_image at trans_map_marker_fix(marker_to["pos"]) as map_to_marker
    pause 0.5

    show map_l_hand:
        linear 0.5 pos (136, 1080)
    show map_r_hand:
        linear 0.5 pos (1627, 1080)

    pause 0.5
    hide map_r_hand
    hide map_l_hand
    with None

    pause 1.0

    $ stage_index = 0
    while stage_index < len(route_stages):
        show map_road at trans_map_road_move
        $ route_stage = route_stages[stage_index]
        $ map_show_stage(route_stage["appear"], route_stage["fix"], stage_index)

        if route_stage["event_label"]:
            show map_road at trans_map_road_stop
            show map_event_image at trans_map_marker_appear(route_stage["event_pos"])
            with hpunch
            pause 2.4
            show map_event_image at trans_map_marker_fix(route_stage["event_pos"])
            pause 0.5
            call expression route_stage["event_label"] from _map_event_label
            hide map_event_image
            pause 0.5
        $ stage_index += 1
    
    show map_road at trans_map_road_stop
    show map_marker_image at trans_map_marker_appear(marker_to["pos"]) as map_to_marker
    pause 2.8
    show map_marker_image at trans_map_marker_fix(marker_to["pos"]) as map_to_marker
    pause 1.5
    scene black
    with dissolve

    jump expression next_label
    
label map_event_6_7:
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