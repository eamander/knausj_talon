shackle:
    edit.line_start()
    edit.extend_line_end()
	
splat:
    edit.extend_word_left()
    edit.delete()
	
splat left:
    edit.extend_word_left()
    edit.delete()

splat right:
    edit.extend_word_right()
    edit.delete()
	
depo:
	edit.paste()