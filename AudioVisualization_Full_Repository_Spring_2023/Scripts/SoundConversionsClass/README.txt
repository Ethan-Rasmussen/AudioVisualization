
We really need to have this done by Teusday Night (Apr 18)  if Possible
Please notify the rest of the group if you complete this, and it would be cool if you let them know you are working on it.

#---------------------------------------------------------------------------------#|
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   #|
THIS FOLDER NEEDS TO END UP CONTAINING A CLASS THAT CAN CONVERT                   #|
BOTH WAYS BETWEEN THE (X,Y,Z) and (A,B,C) PARAMETERS FOR THE RAWSOUND CLASS       #|
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   #|
                                                                                  #|
                                                                                  #|
#-------------------------------------------#|                                    #|
program file name: SoundConversionsClass.py #|                                    #|
#-------------------------------------------#|                                    #|
                                                                                  #|
functionality:                                                                    #|
This program needs to have a class, potentially static but doesnt really matter,  #|
we can just declare one of these objects at the start of whatever program we use  #|
it in... that has the following features:                                         #|
#---------------------------------------------------------------------------------#|

//---------------------//|******
Conversion equation:  //|******
                      //|******
ax + by + cz + 0d = 0 //|******
                      //|******
ax + by + cz = 0      //|******
                      //|******
//---------------------//|******

static? class SoundConversionsClass:

a = 0.0
b = 0.0
c = 0.0
x = 0.0
y = 0.0
z = 0.0

def __init__(self x?, y?, z?, a?, b?, c?):   #pass 'None'  for empty stuff
{
	-assign whatever parameters you were passed,
	to the memebr variables
	
	-check if you got all three of either x,y,z, or a,b,c, 
	-else 	
		[raise an error or something, try and and make it clean, 
		so that we can catch that error with the actual software.]

	-if you got all 6, try and confirm whether the numbers are reasonable for a conversion

}


//------------------------------------------------------------------------------------------------------------
@classmethod
def xyz_to_abc(x=0.0, y=0.0, z=0.0):
{
	- literally any input is valid as long as it is a number,... BUT
	this is one of the areas where we need to avoid divide by zero errors and things like that.
The general conversion should always produce decent results, but obviously the line between the
orgin and a point on the z axis could create problems so you might want to watch out for those
kinds of things.

One solution could be to create a function :
				[  isWithin_M_of_anAxis(self x?, y?, z?, a?, b?, c?){return bool}   ] ... that
you can call right away when you enter the __init__ to help you be sure that things arent going to get weird
}
//------------------------------------------------------------------------------------------------------------

@class method
def abc_to_xyz(a=0.0, b=0.0, c=0.0){} ... so on and so forth
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
based on that, you want another version to go abc_to_xyz, or you can place logic in the previous function to get it all done in one. Obviously, theres many ways you could do this, but we just want to be able to trust this class to get us the other kind of parameter any time we ask for it as ling as we have one of the 2 kinds readily available. Using the new format for importing files, we should be able to bring in this class and have it work. So check examples like how it is set up in the 'FreshestCopyofApplication' folder... even thought those have a problem with the linking, you can see that is does not have to do with not being able to find the files it is looking for.

//------------------------------------------------------------------------------------------------------------
@classmethod
def getNewGraphPoint(RawSound raw_sound):
	#figure out the (x, y, z) point given a regressed raw_sound object off of the buffer
