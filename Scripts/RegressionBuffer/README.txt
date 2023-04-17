Program name: RegressionBuffer.py

#-------------------------------------------------------------------------------#|
#PROPER FORMAT FOR IMPORTING A FILE(from within 'Application' folder somewhere) #|
############################################################################### #|
        self.AppHomeFolder = Folder                                             #|
        self.currentDirectory = ''                                              #|
        sys.path.append(self.AppHomeFolder)                                     #|
        self.currentDirectory = self.AppHomeFolder + '/Regression_Sandbox'      #|
        sys.path.append(self.currentDirectory)                                  #|
        from Regression_Sandbox import RawSound, ..other regression stuff       #|
#-------------------------------------------------------------------------------#|


import MatPlotLib

class RegressionBuffer():

	#consider using a constants pattern like this:
	self.history_mode = 'timed', or 'permanent', or 'last5buffer', or 'last10buffer'

	def __int__(self)
		#set up the plot, using grapd3d_8.0.py to get the
		# nice setup with the array there and everything.


		''' 
		dont forget to notice that I have the plot set so that the axis 
		go out to 5... perhaps it 
		woouldve been smarter of me to design it keeping the
		axis limits at 1.0, but at least having 5 gives us a set of whole numbers that we 
		can use to graph the target location during the calibration program, and then there 
		is more whole number grid points, since thats what we would end up making it into for 
		ourselves anyway, should the target distances by fractions
		'''


	def goLive():
		'''
		set up the buffer that will receive RawSound objects that
		do NOT have abc or xyz parameters yet...
		
		sounds like ethan is working on the regression software and linking that with the application..
		either way, we just want this function for the RegressionBuffer class to set up a buffer that will
		wait on the minimally initialized sounds, coming from the program that connects to the arduino.
		when the buffer is not empty, add the sound to the the plot.

		heres where you would put the logic for:

		if self.history_mode == 'timed':
			for sound in graphed_sound_points:
				if (sound has been plotted for over 10 seconds):
					delete sound
		elif self.history_mode == 'permanent'
			for sounf in graphed_sound_points:
				graph no matter what, if its in the list
			if the user chooses clear sound buffer:
				clear the buffer


		etc...
		etc.. 
		
		'''

	'''
	other methods im sure will come in handy, especially with linking the programs together

		I think this is a pretty clear image of what we are shooting for here. Let me know with any questions 
		-Ben
	'''
