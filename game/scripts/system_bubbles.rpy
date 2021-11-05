init -1:
    define bubbles = {
        "1057x364_bl": {
            "image": "ui_images/bubble/bubble_1057x364_bl.png",
            "anchor": (0.0, 1.0),
            "text_pos": (47, 23),
            "text_size": (972, 219),
            "style_prefix": "bubble1057"
        },
        "cat": {
            "image": "ui_images/bubble/cat_bubble.png",
            "anchor": (1.0, 1.0),
            "text_pos": (35, 27),
            "text_size": (382, 112),
            "style_prefix": "bubble_cat"
        }
    }

init -1 python:
    def CharacterAt(kind, position, bubble, **kwargs):
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

screen say_bubble(who, what, bubble="1057x364_bl", position=(1920 / 2, 1080 / 2)):
    $ b = bubbles[bubble]
    fixed:
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
                        text who id "who"
                    text what id "what"

style bubble1057_who is bubble_name_text
style bubble1057_what is bubble_text
style bubble1057_vbox:
    spacing 20
style bubble_cat_who is bubble_name_text
style bubble_cat_what is bubble_text:
    size 54
    xalign 0.5
    yalign 0.5
style bubble_cat_vbox:
    xfill True
    yfill True