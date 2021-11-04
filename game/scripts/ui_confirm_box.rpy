screen confirm(message, yes_action, no_action, yes_label=_("Да"), no_label=_("Нет")):
    modal True
    zorder 200
    style_prefix "confirm"
    add "ui_images/overlay/confirm.png"
    frame:
        vbox:
            label _(message) style "confirm_prompt"
            hbox:
                textbutton yes_label action yes_action
                textbutton no_label action no_action
    key "game_menu" action no_action

style confirm_vbox:
    xalign 0.5
    yalign 0.5
    spacing 40

style confirm_hbox:
    xalign 0.5
    spacing 150

style confirm_frame:
    xsize 1418
    ysize 322
    background Frame("ui_images/frame.png", Borders(54, 39, 29, 25))
    xalign 0.5
    yalign 0.5

style confirm_prompt_text is ui_text:
    color "#000000"

style confirm_button:
    xsize 400
    ysize 85
    xalign 0.5
    background "ui_images/button/confirm_button_idle.png"
    hover_background "ui_images/button/confirm_button_hover.png"

style confirm_button_text is ui_text:
    xalign 0.5
    yalign 0.5
    hover_color "#ffffff"
    color "#000000"

init python:
    class ConfirmWithButtons(Action, DictEquality):
        def __init__(self, prompt, yes, no=None, confirm_selected=False, yes_label=_("Да"), no_label=_("Нет")):
            self._prompt = prompt
            self._yes_action = yes
            self._no_action = no
            self._confirm_selected = confirm_selected
            self._yes_label = yes_label
            self._no_label = no_label
        
        def get_sensitive(self):
            if self._yes_action is None:
                return False
            return renpy.is_sensitive(self._yes_action)
        
        def get_selected(self):
            return renpy.is_selected(self._yes_action)
        
        def get_tooltip(self):
            return renpy.display.behavior.get_tooltip(self._yes_action)
        
        def __call__(self):
            if self.get_selected() and not self._confirm_selected:
                return renpy.run(self._yes_action)
            screen = "confirm"
            yes_actions = [Hide(screen, config.exit_yesno_transition)]
            no_actions = [Hide(screen, config.exit_yesno_transition)]
            if self._yes_action is not None:
                yes_actions.append(self._yes_action)
            if self._no_action is not None:
                no_actions.append(self._no_action)
            if config.enter_yesno_transition:
                renpy.transition(config.enter_yesno_transition)
            renpy.show_screen(
                screen,
                message=self._prompt,
                yes_action=yes_actions,
                no_action=no_actions,
                yes_label=self._yes_label,
                no_label=self._no_label
            )
            renpy.restart_interaction()
            return
