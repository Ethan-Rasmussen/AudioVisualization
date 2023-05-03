USE:

SoundFileGen.py   		-   create sound log files in data1.df and data2.df

Train_With_New_Sound_File.py 	- Opens data2.df and will try and update the current model 					with the data it finds here, or else it will generate a new 				model with the data from daat1.df, and then it will read the 				data2.df and continue from there


Read_and_Regress.py		-This file is the true test of the model to be applied to a 				new chunk of data,  and then it scores itself on accuracy. The 				error output is quite useful for debugging the generator.


** as you can see though, this code is working flawlessly at predicting the abc parameters well within any error margin we have heard of, even when I try and sabatoge the data with seevere noise, it figures it out, even with a training set as small as like 20.