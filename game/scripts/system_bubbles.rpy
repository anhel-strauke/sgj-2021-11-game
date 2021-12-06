init -1:
    transform trans_flip_horizontal:
        xzoom -1
    transform trans_flip_vertical:
        yzoom -1
    transform trans_flip_both:
        xzoom -1 yzoom -1

    define bubbles = {
        "": {
            "image": "ui_images/bubble/bubble_big.png",
            "anchor": (0.5, 1.0),
            "text_pos": (46, 42),
            "text_size": (1267, 188),
            "style_prefix": "default_bubble"
        },
        "left_big": {
            "image": "ui_images/bubble/bubble_left_big.png",
            "anchor": (0.0, 0.75),
            "text_pos": (119, 39),
            "text_size": (1005, 192),
            "uppercase_who": True,
            "style_prefix": "bubble_right_tall"
        },
        # "right_small": {
        #     "image": "ui_images/bubble/small_bubble_right.png",
        #     "anchor": (1.0, 120),
        #     "text_pos": (25, 25),
        #     "text_size": (438, 136),
        #     "style_prefix": "bubble_right_small"
        # },
        "left_tall": {
            "image": "ui_images/bubble/bubble_left.png",
            "anchor": (1.0, 120),
            "text_pos": (90, 25),
            "text_size": (438, 136),
            "style_prefix": "bubble_left_tall"
        },
        "left_very_tall": {
            "image": Frame("ui_images/bubble/bubble_left.png", 0, 158, 0, 34),
            "anchor": (0, 120),
            "text_pos": (90, 25),
            "xsize": 550,
            "min_height": 243,
            "padding": (84, 25, 18, 46),
            "style_prefix": "bubble_right_tall"
        },
        "cat": {
            "image": "ui_images/bubble/cat_bubble.png",
            "anchor": (1.0, 120),
            "text_pos": (25, 25),
            "text_size": (438, 136),
            "style_prefix": "bubble_cat"
        },
        "right_tall": {
            "image": "ui_images/bubble/bubble_right.png",
            "anchor": (550, 120),
            "text_pos": (25, 25),
            "text_size": (461, 136),
            "style_prefix": "bubble_right_tall"
        },
        "right_very_tall": {
            "image": Frame("ui_images/bubble/bubble_right.png", 0, 158, 0, 34),
            "anchor": (550, 120),
            "text_pos": (25, 25),
            "xsize": 550,
            "min_height": 243,
            "padding": (25, 25, 84, 46),
            "style_prefix": "bubble_right_tall"
        },
        "top_left_big": {
            "image": "ui_images/bubble/bubble_top_left_big.png",
            "anchor": (0.1, 0.0),
            "text_pos": (39, 90),
            "text_size": (1266, 191),
            "style_prefix": "bubble_top_left"
        },
        "top_right_big_real": {
            "image": "ui_images/bubble/bubble_top_right_big.png",
            "anchor": (0.9, 0.0),
            "text_pos": (39, 90),
            "text_size": (1266, 191),
            "style_prefix": "bubble_top_left"
        },
        "top_right_big": {
            "image": At("ui_images/bubble/bubble_top_right_big.png",trans_flip_vertical),
            "anchor": (0.9, 0.0),
            "text_pos": (47, 50),
            "text_size": (1266, 191),
            "style_prefix": "bubble_top_right"
        },
        "top_right": {
            "image": Frame("ui_images/bubble/bubble_top_right.png", 0, 82, 0, 163),
            "anchor": (428, 1.0),
            "text_pos": (34, 21),
            "xsize": 561,
            "min_height": 82 + 163,
            "padding": (34, 21, 561-533, 312-229),
            "style_prefix": "bubble_right_tall"
        },
        "top_left": {
            "image": At(Frame("ui_images/bubble/bubble_top_right.png", 0, 82, 0, 163), trans_flip_horizontal),
            "anchor": (133, 1.0),
            "text_pos": (28, 21),
            "xsize": 561,
            "min_height": 82 + 163,
            "padding": (28, 21, 561-527, 312-229),
            "style_prefix": "bubble_right_tall"
        },
        "top_left_th": {
            "image": "ui_images/bubble/bubble_thoughts_top_left.png",
            "anchor": (0.1, 0.0),
            "text_pos": (45, 25),
            "text_size": (1095, 195),
            "style_prefix": "bubble_th"
        },
        "top_right_th": {
            "image": At("ui_images/bubble/bubble_thoughts_top_left.png", trans_flip_horizontal),
            "anchor": (0.9, 1.0),
            "text_pos": (45, 35),
            "text_size": (1095, 195),
            "style_prefix": "bubble_th"
        },
        "top_left_small_th": {
            "image": Frame("ui_images/bubble/bubble_thoughts_top_left_small.png", 0, 108, 0, 158),
            "anchor": (30, 1.0),
            "text_pos": (44, 32),
            "xsize": 662,
            "min_height": 108 + 158 + 10,
            "padding": (44, 32, 662 - 624, 340 - 234),
            "style_prefix": "bubble_right_tall"
        },
    }

init -1 python:
    def CharacterAt(kind, position=None, bubble="", **kwargs):
        if position is None:
            position = (1920 / 2, 1080 - 88)
        b = bubbles[bubble]
        if "style_prefix" in b:
            if "who_style" not in kwargs:
                kwargs["who_style"] = b["style_prefix"] + "_who"
            if "what_style" not in kwargs:
                kwargs["what_style"] = b["style_prefix"] + "_what"
        return Character(
                kind=kind,
                screen="say_bubble",
                show_bubble=bubble,
                show_position=position,
                **kwargs
            )

screen say_bubble(who, what, bubble="", position=(1920 / 2, 1080 - 28)):
    $ b = bubbles[bubble]
    $ caps_who = unicode(who).upper() if b.get("uppercase_who", True) else who
    fixed:
        if "padding" in b:
            $ min_height = b.get("min_height", 0)
            window id "window":
                background b["image"]
                pos position
                anchor b["anchor"]
                xsize b["xsize"]
                yminimum min_height
                padding b["padding"]
                vbox:
                    xfill True
                    style b["style_prefix"]+"_vbox"
                    if who:
                        text caps_who id "who"
                    text what id "what"
        else:
            window id "window":
                style_prefix "foo"
                background b["image"]
                pos position
                anchor b["anchor"]
                fixed:
                    xysize b["text_size"]
                    vbox:
                        xfill True
                        style b["style_prefix"]+"_vbox"
                        pos b["text_pos"]
                        if who:
                            text caps_who id "who"
                        text what id "what"

style default_bubble_who is bubble_name_text
style default_bubble_what is bubble_text
style default_bubble_vbox:
    spacing 16

style bubble_left_big_who is bubble_name_text:
    size +40
style bubble_left_big_what is bubble_text
style bubble_left_big_vbox:
    spacing 16

style bubble_top_right_who is bubble_name_text:
    size +40
style bubble_top_right_what is bubble_text
style bubble_top_right_vbox:
    spacing 16

style bubble_right_small_who is bubble_name_text:
    size +40
style bubble_right_small_what is bubble_text:
    size 35
    xalign 0.1
style bubble_right_small_vbox:
    spacing 16

style bubble_left_tall_who is bubble_name_text:
    size +40
style bubble_left_tall_what is bubble_text:
    size 35
    xalign 0.1
style bubble_left_tall_vbox:
    spacing 16

# style bubble_right_tall_who is bubble_name_text:
#     size +40
style bubble_right_tall_who is bubble_name_text
# style bubble_right_tall_what is bubble_text:
#     size 35
style bubble_right_tall_what is bubble_text
style bubble_right_tall_vbox:
    spacing 16

style bubble_top_left_who is bubble_name_text
style bubble_top_left_what is bubble_text
style bubble_top_left_vbox:
    spacing 16

style bubble_cat_who is bubble_name_text
style bubble_cat_what is bubble_text:
    size 54
    xalign 0.5
    yalign 0.5
style bubble_cat_vbox:
    xfill True
    yfill True

style bubble_th_who is bubble_name_text
style bubble_th_what is bubble_text
style bubble_th_vbox:
    spacing 16
