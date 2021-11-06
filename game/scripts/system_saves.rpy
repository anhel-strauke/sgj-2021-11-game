init offset = -1
init:
    default save_game_info = ""

init python:
    import datetime as dt

    autosave_file_name = u"current"
    save_file_name_prefix = u"save_"
    pause_save_file_name = "pause"

    autosave_indicator_screen = None


    def ss_list_save_slots():
        saves = []
        for (file_name, info, screenshot, utime) in renpy.list_saved_games(save_file_name_prefix):
            if len(file_name) > len(save_file_name_prefix):
                save_index = file_name[len(save_file_name_prefix):]
                if save_index.isdigit():
                    save_index = int(save_index)
                    saves.append((save_index, info, screenshot, utime))
        saves.sort(key=lambda slot: slot[3], reverse=True)
        return saves

    def ss_has_saves():
        return len(ss_list_save_slots()) > 0
    
    def ss_has_continue():
        return renpy.can_load(autosave_file_name)
    
    def ss_set_info(*args):
        global save_game_info
        save_game_info = "|".join(args)

    def ss_savepoint():
        global save_game_info
        if not renpy.in_rollback():
            renpy.take_screenshot()
            renpy.save(autosave_file_name, extra_info=save_game_info)
            if autosave_indicator_screen is not None:
                renpy.show_screen(autosave_indicator_screen)
    
    def ss_game_end():
        renpy.unlink_save(autosave_file_name)

    def _make_save_file_name(save_index):
        return (save_file_name_prefix + u"%d") % save_index
    
    def ss_new_save_index(existing_slots=None):
        # existing_slots should be a result of list_save_slots()
        if existing_slots is None:
            existing_slots = ss_list_save_slots()
        max_index = 0
        for slot in existing_slots:
            slot_index = slot[0]
            if max_index < slot_index:
                max_index = slot_index
        return max_index + 1

    def ss_save_game(save_to_index=None):
        global save_game_info
        if save_to_index is not None:
            new_save_filename = _make_save_file_name(save_to_index)
        else:
            new_save_filename = _make_save_file_name(ss_new_save_index())
        if ss_has_continue():
            renpy.copy_save(autosave_file_name, new_save_filename)
        else:
            renpy.take_screenshot()
            #print "Saving \"" + save_game_info + "\""
            renpy.save(new_save_filename, extra_info=save_game_info)

    def ss_continue_game():
        renpy.load(autosave_file_name)
    
    def ss_load_game(save_index):
        save_file_name = _make_save_file_name(save_index)
        if renpy.can_load(save_file_name):
            renpy.copy_save(save_file_name, autosave_file_name)
            renpy.load(save_file_name)

    def _format_minutes_ru(num):
        last_digit = num % 10
        if 10 <= num <= 20 or last_digit in (0, 5, 6, 7, 8, 9):
            return "%d минут" % num
        if last_digit == 1:
            return "%d минуту" % num
        return "%d минуты" % num
    
    def ss_format_save_time(utime):
        datetime = dt.datetime.fromtimestamp(utime)
        curr = dt.datetime.now()
        delta = curr - datetime
        if delta.days == 0:
            if delta.seconds < 60:
                return _("Меньше минуты назад")
            if delta.seconds < 3600:
                return _("%s назад") % _format_minutes_ru(int(delta.seconds / 60))
        return datetime.strftime("%d.%m.%Y, %H:%M")
    
    def ss_save_pause():
        renpy.save(pause_save_file_name)
    
    def ss_load_pause():
        if renpy.can_load(pause_save_file_name):
            renpy.load(pause_save_file_name)

    def location(name):
        ss_set_info(name)
        ss_savepoint()

    class ContinueGame(Action, DictEquality):
        def get_sensitive(self):
            return ss_has_continue()
        
        def __call__(self):
            ss_continue_game()
    

    class LoadFromSlot(Action, DictEquality):
        def __init__(self, slot_index):
            self._slot_index = slot_index
        
        def get_sensitive(self):
            return renpy.can_load(_make_save_file_name(self._slot_index))
        
        def __call__(self):
            if not self.get_sensitive():
                return
            ss_load_game(self._slot_index)


    class SaveToSlot(Action, DictEquality):
        def __init__(self, slot_index):
            self._slot_index = slot_index
        
        def get_sensitive(self):
            return True
        
        def __call__(self):
            ss_save_game(self._slot_index)
    

    class DeleteSaveSlot(Action, DictEquality):
        def __init__(self, slot_index):
            self._slot_index = slot_index
        
        def get_sensitive(self):
            return renpy.can_load(_make_save_file_name(self._slot_index))
        
        def __call__(self):
            if not self.get_sensitive():
                return
            filename = _make_save_file_name(self._slot_index)
            renpy.unlink_save(filename)

    def SaveSlotAction(do_save, slot_index):
        if do_save:
            return [SaveToSlot(slot_index), Return()]
        return LoadFromSlot(slot_index)