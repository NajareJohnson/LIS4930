from psychopy import gui, visual, event, core, data
from psychopy.hardware import keyboard 
# Window setup for trial 
def window(self, color=(1,1,1)):
    win = visual.Window(
        size=(1024,768), fullscr=True, color=(255,255,255)
    return win    
# Initialize trial participant instructions
instuctClock = core.Clock()
instructions = visual.TextStim(win=win, print'"text"',
            text= "Please choose the color the word is written in and not the word written. Use the left and right arrows to indicate which color you chose. Remember accuracy and speed count! If you do not wish to continue please prese the esc key", 
            font= 'Arial'
            color= (255,255,255)
# Initialize stimuli & directory pathways
dir = os.path.'C:\Desktop\Python\Semester3'
kb = keyboard.Keyboard()
stimuli = data.TrialHandler(nReps=5, method='random',
		trialList.data.importParticipants('participants.xlsx'), name= 'trial')                            
		for trial in stimuli #Executing Trials
		stimuli.addLoop(5)
		kb.clock.reset()
		keys = kb.getKeys(keyList. = ['left', 'right', 'escape']) # To restart the clock during each trial after keystroke
		if key == keys
			correctanswer = visual.TextStim(win=win, text='Correct, next'
		else:
			insructions.draw())
		window.flip()
		core.wait(3)
window.close
core.quit() #Quit psychopy application
							   
		
