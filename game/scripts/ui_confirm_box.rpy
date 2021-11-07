screen confirm(message, yes_action, no_action):
    modal True
    zorder 900
    style_prefix "confirm"
    add "ui_images/overlay/confirm.png"
    frame:
        fixed:
            label _(message) style "confirm_prompt"
            hbox:
                button action yes_action:
                    background "ui_images/button/[prefix_]confirm_yes.png"
                button action no_action:
                    background "ui_images/button/[prefix_]confirm_no.png"
    key "game_menu" action no_action

style confirm_vbox:
    xalign 0.5
    yalign 0.5
    spacing 40

style confirm_hbox:
    xalign 0.5
    yalign 1.0
    spacing 63
    xoffset 19
    yoffset -89

style confirm_frame:
    xsize 1040
    ysize 572
    background "ui_images/yes_no_bg.png"
    xalign 0.5
    yalign 0.5
    xoffset -35

style confirm_prompt:
    xysize (759, 199)
    pos (168, 162)

style confirm_prompt_text is ui_text:
    color "#fcd28e"
    align (0.5, 0.5)
    text_align 0.5

style confirm_button:
    xsize 219
    ysize 101

# init python:
#     class ConfirmWithButtons(Action, DictEquality):
#         def __init__(self, prompt, yes, no=None, confirm_selected=False, yes_label=_("Да"), no_label=_("Нет")):
#             self._prompt = prompt
#             self._yes_action = yes
#             self._no_action = no
#             self._confirm_selected = confirm_selected
#             self._yes_label = yes_label
#             self._no_label = no_label
        
#         def get_sensitive(self):
#             if self._yes_action is None:
#                 return False
#             return renpy.is_sensitive(self._yes_action)
        
#         def get_selected(self):
#             return renpy.is_selected(self._yes_action)
        
#         def get_tooltip(self):
#             return renpy.display.behavior.get_tooltip(self._yes_action)
        
#         def __call__(self):
#             if self.get_selected() and not self._confirm_selected:
#                 return renpy.run(self._yes_action)
#             screen = "confirm"
#             yes_actions = [Hide(screen, config.exit_yesno_transition)]
#             no_actions = [Hide(screen, config.exit_yesno_transition)]
#             if self._yes_action is not None:
#                 yes_actions.append(self._yes_action)
#             if self._no_action is not None:
#                 no_actions.append(self._no_action)
#             if config.enter_yesno_transition:
#                 renpy.transition(config.enter_yesno_transition)
#             renpy.show_screen(
#                 screen,
#                 message=self._prompt,
#                 yes_action=yes_actions,
#                 no_action=no_actions,
#                 yes_label=self._yes_label,
#                 no_label=self._no_label
#             )
#             renpy.restart_interaction()
#             return
