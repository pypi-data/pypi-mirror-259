"""
IM control via TCP/IP
Python API to control the IM via TcpIp

This file defines the IM object, which represents a TcpIp connection to the IM control software.
The connection is established upon creation of the IM object.

Requirements :
- an IM must be attached to the PC running the code
- the IM must be powered-on, and the IM control software opened
- this script must be either installed via pip, or put in the python sys.PATH so that it can be imported 

from acquifer.tcpip import TcpIp

myIM = TcpIp() # create the connection
myIM.openLid() # example
"""
from __future__ import annotations # needed to avoid having type hint as string
from typing import TYPE_CHECKING   
import socket, time, os
from . import utils # if we need to use utils

if TYPE_CHECKING:
	from . import WellPosition # needed to avoid circular imports : acquifer.py __init__ importing tcpip, and tcpip importing the init in return

def isPositiveInteger(value):
	"""Return false if the input is not a strictly positive >0 integer."""
	
	if not isinstance(value, int) or value < 1 :
		return False
	
	return True

def isNumber(value):
	"""Test if an input is a number ie int or float."""
	return isinstance(value, (int, float))

def checkIntensity(intensity):
	"""Throw a ValueError if the intensity is not an integer in range 0-100."""
	
	if not isinstance(intensity, int):
		raise ValueError("Intensity must be an integer value.")

	if intensity < 0 or intensity > 100 :
		raise ValueError("Intensity must be in range [0-100].")

def checkExposure(exposure):
	"""Throw a ValueError if the exposure is not a strictly positive integer value."""
	if not isinstance(exposure, int) or exposure <= 0 :
		raise ValueError("Exposure must be a strictly positive integer value.")

def checkLightSource(lightSource):
	
	msg = "Light lightSource should be either 'brightfield'/'BF' or a 6-character long string of 0 and 1 for fluorescent light sources ex : '010000'."
	
	if not isinstance(lightSource, str) : 
		raise TypeError(msg)
	
	if lightSource == "000000":
		raise ValueError("At least one fluorescent light lightSource should be selected.")
	
	if not lightSource.lower() in ("bf", "brightfield"): # then it should be a fluo light lightSource
		
		# Check that it`s 6 character long
		if len(lightSource) != 6:
			raise ValueError(msg)
		
		# Check that it`s a succession of 0/1
		for char in lightSource:
			if not (char == "0" or char =="1"):
				raise ValueError(msg)

def checkChannelParameters(channelNumber, detectionFilter, intensity, exposure, lightConstantOn):
	"""
	Utility function to check the validity of parameters for the setBrightfield and setFluoChannel functions.
	Raise a ValueError if there is an issue with any of the parameters.
	"""
	if not isPositiveInteger(channelNumber):
		raise ValueError("Channel number must be a strictly positive integer.")
	
	if not detectionFilter in (1,2,3,4) : 
		raise ValueError("Filter index must be one of 1,2,3,4.")
	
	if not isinstance(lightConstantOn, bool):
		raise TypeError("lightConstantOn must be a boolean value (True/False).")
		
	checkIntensity(intensity)
	checkExposure(exposure)

def checkZstackParameters(zStackCenter, nSlices, zStepSize):
	"""
	Check the validity of parameters for command involving z-stack (acquire/AF).
	Raise a ValueError if there is an issue with any of the parameters.
	"""
	if not isPositiveInteger(nSlices):
		raise ValueError("Number of slice must be a strictly positive integer.")
	
	if not isNumber(zStackCenter) or zStackCenter < 0 :
		raise ValueError("zStackCenter must be a positive number.")
	
	if not isNumber(zStepSize) or zStepSize < 0 :
		raise ValueError("zStepSize must be a positive number.")


class TcpIp(object):
	"""Object representing an active TcpIp connection to the Imaging Machine Control Software for remote control."""

	def __init__(self, port=6200):
		"""Initialize a TCP/IP socket for the exchange of commands."""
		
		self._socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM) # IPv6 on latest IM 
		try:
			self._socket.connect(("localhost", port))
		
		except socket.error:
			msg = ("Cannot connect to IM GUI.\nMake sure an IM is available, powered-on and the IM program is running.\n" +
			"Also make sure that the option 'Block remote connection' of the admin panel is deactivated, and that the port numbers match (here set to {}).".format(port))
			raise socket.error(msg)
		
		self._isConnected = True # only False once socket is closed
		print("Connected to IM on port {}, in {} mode.".format(port, self.getMode()))

	def closeConnection(self):
		"""
		Close the socket connection, making it available to other resources.
		After closing the socket, no commands can be sent anymore via this IM instance. 
		This should be called at the end of external scripts.
		It also switches back to 'live' mode in case the machine is in script mode, and switch off all channels.
		"""
		print("Closing connection with the IM - going to LIVE mode, resetting camera and switching off all light-sources.")
		self.setMode("live")
		self.resetCamera()
		self.setBrightFieldOff()
		self.setFluoChannelOff()
		self._socket.close()
		self._isConnected = False
		print("Closed connection : no more commands can be sent via this IM object.")

	def sendCommand(self, stringCommand):
		"""
		Send a string command to the IM and wait 50ms for processing of the command.
		The command is converted to a bytearray before sending.
		""" 
		if not self._isConnected:
			raise socket.error("Connection to IM was closed. Create a new IM object to establish a new connection.")
		
		self._socket.sendall(bytearray(stringCommand, "ascii"))
		time.sleep(0.05) # wait 50ms, before sending another command (which is usually whats done next, e.g. with _getFeedback

	def checkLidClosed(self):
		"""Throw an exception if the lid is opened.""" 
		if self.isLidOpened():
			raise Exception("Lid is opened !")

	def _getFeedback(self, nbytes=256):
		"""
		Tries to read at max nbytes back from IM and convert to a string.
		This should be called after "get" commands.
		Calling this function will block execution (ie the function wont return), until at least one byte is available for reading.
		"""
		return self._socket.recv(nbytes).decode("ascii")

	def _waitForFinished(self):
		"""
		This function calls getFeedback with the correct size corresponding to "finished". 
		It will pause code execution until this amount of bytes can be read.
		"""
		feedback = self._getFeedback()
		if feedback != "finished":
			self.setMode("live")      # come back to live in case it was in script
			raise Exception(feedback) # this also interrupts execution

	def _getValueAsType(self, command, cast):
		"""Send a command, get the feedback and cast it to the type provided by the cast function ex: int."""
		self.sendCommand(command)
		return cast(self._getFeedback())

	def _getIntegerValue(self, command):
		"""Send a command and parse the feedback to an integer value."""
		return self._getValueAsType(command, int)

	def _getFloatValue(self, command):
		"""Send a command and parse the feedback to a float value."""
		return self._getValueAsType(command, float)

	def _getBooleanValue(self, command):
		"""Send a command and parse the feedback to a boolean value (0/1)."""
		return self._getValueAsType(command, int) # dont use bool, bool of a non-empty string is always true, even bool("0")

	def openLid(self):
		self.sendCommand("OpenLid()")
		self._waitForFinished()

	def closeLid(self):
		self.sendCommand("CloseLid()")
		self._waitForFinished()

	def isLidClosed(self):
		"""Check if the lid is closed."""
		return self._getBooleanValue("LidClosed()")

	def isLidOpened(self):
		"""Check if lid is opened."""
		return self._getBooleanValue("LidOpened()")

	def getMode(self):
		"""Return current acquisition mode either "live" or "script"."""
		return "live" if self._getBooleanValue("LiveModeActive()") else "script"

	def isScriptRunning(self):
		"""
		Check if a script is running i.e when LiveMode is not active.
		If a script is running, tcpip commands should not be sent (except to ask for the machine state).
		"""
		return not self._getBooleanValue("LiveModeActive()")

	def isLiveModeActive(self):
		"""
		Check if live mode is active, i.e no script is running and tcpip commands can be sent.
		"""
		return self._getBooleanValue("LiveModeActive()")

	def isTemperatureRegulated(self):
		return self._getBooleanValue("GetTemperatureRegulation()")
	
	def getTemperatureAmbient(self):
		"""Return ambient temperature in Celsius degrees."""
		return self._getFloatValue("GetAmbientTemperature(TemperatureUnit.Celsius)")
	
	def getTemperatureSample(self):
		"""Return the sample temperature in Celsius degrees."""
		return self._getFloatValue("GetSampleTemperature(TemperatureUnit.Celsius)")

	def getTemperatureTarget(self):
		"""Return the target temperature in celsius degrees."""
		return self._getFloatValue("GetTargetTemperature(TemperatureUnit.Celsius)")

	def setTemperatureRegulation(self, state):
		"""
		Activate (state=True) or deactivate (state=False) temperature regulation.
		"""
		if state :
			self.sendCommand("SetTemperatureRegulation(1)")
		
		else :
			self.sendCommand("SetTemperatureRegulation(0)")
		
		self._waitForFinished()
		
	def setTemperatureTarget(self, temp):
		"""
		Set the target temperature to a given value in degree celsius (with 0.1 precision).
		Note : This does NOT switch on temperature regulation !
		Call setTemperatureRegulation(True) to activate the regulation.
		"""
		if (temp < 18 or temp > 34):
			raise ValueError("Target temperature must be in range [18;34].")
		
		self.sendCommand( "SetTargetTemperature({:.1f}, TemperatureUnit.Celsius)".format(temp) )
		self._waitForFinished()
		
	def getNumberOfColumns(self):
		"""Return the number of plate columns."""
		return self._getIntegerValue("GetCountWellsX()")

	def getNumberOfRows(self):
		"""Return the number of plate rows."""
		return self._getIntegerValue("GetCountWellsY()")

	def getObjectiveIndex(self):
		"""Return the currently selected objective-index (1 to 4)."""
		return self._getIntegerValue("GetObjective()")

	def getPositionX(self):
		"""Return the current objective x-axis position in mm."""
		return self._getFloatValue("GetXPosition()")

	def getPositionY(self):
		"""Return the current objective y-axis position in mm."""
		return self._getFloatValue("GetYPosition()")

	def getPositionZ(self):
		"""Return the current objective z-axis position in µm."""
		return round(self._getFloatValue("GetZPosition()"), 1) # keep 0.1 precision only, although returned with 3-digit position (but alternating)

	def log(self, message):
		"""Log a message to display in the imgui log."""
		self.sendCommand("Log({})".format(message))
		self._waitForFinished()

	def _moveXY(self, x, y, mode="absolute"):
		"""
		Move XY-position to an absolute X,Y position (mode=absolute), 
		or increment the position by a given step (mode=relative).
		This function blocks until the position is reached.
		"""
		self.checkLidClosed()
		
		if mode == "absolute":
			goToMode = "GotoMode.Abs"
		
		elif mode == "relative":
			goToMode = "GotoMode.Rel"
		
		else :
			raise ValueError("mode is 'absolute' or 'relative'.")
		
		cmd = "GotoXY({:.3f}, {:.3f}, {})".format(x, y, goToMode)
		self.sendCommand(cmd)
		print(cmd)
		
		# Feedback
		if self._getFeedback() == "out of range":
			raise ValueError("X,Y position out of range.")

	def moveXYto(self, x, y):
		"""
		Move to position x,y in mm, with 0.001 decimal precision.
		This commands blocks code execution until the position is reached.
		"""
		if (x<0 or y<0):
			raise ValueError("x,y positions must be positive.")
		
		self._moveXY(x,y)
	
	def moveXYtoWellPosition(self, wellPosition:WellPosition):
		"""
		Move the objective to pre-defined well position, and update well/subposition metadata.
		"""
		
		"""
		# Check if wellPosition is a WellInfo object
		# could work but requires importing the dll here too
		if isinstance(wellPosition, WellPosition):
			x,y = wellPosition.x, wellPosition.y
		
		elif isinstance(wellPosition, WellInfo):
			x,y 
		"""
		self.moveXYto(wellPosition.x, wellPosition.y)
		self.setMetadataWellId(wellPosition.wellID)
		self.setMetadataSubposition(wellPosition.subposition)
	
	def moveXYby(self, xStep, yStep):
		"""Increment/Decrement the x, y position by a given step in mm, with 0.001 decimal precision."""
		self._moveXY(xStep, yStep, mode = "relative")

	def _moveZ(self, z, mode="absolute"):
		"""
		Move the Z-position to an absolute axis position (mode=absolute, default),
		or increment/decrement the Z-position (mode=relative).
		"""
		self.checkLidClosed()
		
		if mode == "absolute":
			goToMode = "GotoMode.Abs"
		
		elif mode == "relative":
			goToMode = "GotoMode.Rel"
		
		else :
			raise ValueError("mode is 'absolute' or 'relative'.")
		
		cmd = "GotoZ({:.1f}, {})".format(z, goToMode)
		self.sendCommand(cmd)
		print(cmd)
		self._waitForFinished()

	def moveZto(self, z):
		"""
		Move to Z-position in µm with 0.1 precision.
		This commands blocks code execution until the position is reached.
		"""
		if z<0:
			raise ValueError("Z-position must be a positive value.")
		self._moveZ(z)

	def moveZby(self, zStep):
		"""Increment/Decrement the Z-axis position by a given step size."""
		self._moveZ(zStep, mode = "relative")

	def moveXYZto(self, x, y, z):
		"""
		Move to x,y position (mm, 0.001 precision) and z-position in µm (0.1 precision).
		This commands blocks code execution until the position is reached.
		"""
		cmd = "GotoXYZ({:.3f},{:.3f},{:.1f})".format(x,y,z)
		self.sendCommand(cmd)
		print(cmd)
		self._waitForFinished()

	def runScript(self, scriptPath):
		"""
		Start a .imsf or .cs script to run an acquisition.
		This command can be called only if no script is currently running.
		The command blocks further commands execution until the script has finished running.
		The script that was started can only be stopped in the IM software, in the 'Run' tab.
		
		Returns
		=======
		The directory where the images were last saved.
		"""
		self.checkLidClosed()
		
		scriptPath = scriptPath.lower() # script centered with PV are typically upper-case sos till work here
		
		if not (scriptPath.endswith(".imsf") or scriptPath.endswith(".cs")):
			raise ValueError("Script must be a .imsf or .cs file.")
		
		if not os.path.exists(scriptPath):
			raise ValueError("Script file not existing : {}".format(scriptPath))
		
		cmd = "RunScript({})".format(scriptPath)
		self.sendCommand(cmd)
		print(cmd)
		print("Note : Running script cannot be stopped by tcpip, only via the IM software, in the 'Run' tab.")
		
		# Return the directory where the images were saved
		return self._getFeedback()

	def stopScript(self):
		"""Stop any script currently running."""
		self.sendCommand("StopScript()")
		self._waitForFinished()

	def setCamera(self, x, y, width, height, binning=None):
		"""
		Set acquisition parameters of the camera (binning and/or sensor region for the acquisition).
		The provided parameters will be used for the next "acquire" commands (sent via the gui or tcpip).
		Exposure time are defined for each channel using the setBrightfield or setFluo commands.

		Parameters
		----------
		x : int
			Horizontal coordinate of the top left corner of the rectangular region of interest, in the coordinate system of the camera sensor (when no binning).
		
		y : int
			Vertical coordinate of the top left corner of the rectangular region of interest, in the coordinate system of the camera sensor (when no binning).
		
		width : int
			Width of the rectangular region of interest, in the coordinate system of the camera sensor (when no binning).
		
		height : int
			Height of the rectangular region of interest, in the coordinate system of the camera sensor (when no binning).
		
		binning : int, optional
			Binning factor for width/height. One of 1,2,4 The default is None, ie it wont change the current binning setting.
		"""
		self.checkLidClosed()
		
		if binning and binning not in (1,2,4):
			raise ValueError("Binning should be 1,2 or 4.")
		
		# Check that the values are integer in range 0,2048
		for value in (x,y,width,height) : 
		
			if not isinstance(value, int) or value < 0 or value > 2048 :
				raise ValueError("x,y,width,height must be integer values in range [0;2048].")
		
		# Check that x+width, y+height < 2048
		if (x + width) > 2048 :
			raise ValueError("x + width exceeds the maximal value of 2048 for the camera sensor area.")
		
		if (y + height) > 2048 :
			raise ValueError("y + height exceeds the maximal value of 2048 for the camera sensor area.")
		
		if binning : 
			cmd = "SetCamera({},{},{},{},{})".format(binning, x, y, width, height)
		else:
			cmd = "SetCamera({},{},{},{})".format(x, y, width, height)
		
		self.sendCommand(cmd)
		self._waitForFinished()
		print("Updated camera settings.")

	def setCameraBinning(self, binning):
		"""Set the binning factor for the camera. Also resets the camera sensor region to the full frame 2048x2048."""
		self.sendCommand("SetBinning({})".format(binning))
		self._waitForFinished()


	def resetCamera(self):
		"""Reset camera to full-size field of view (2048x2048 pixels) and no binning."""
		self.setCamera(0,0,2048,2048)
	
	def setObjective(self, index):
		"""
		Set the objective based on the index (1 to 4).
		If the objective given as argument is the current objective, the command has no effect.
		Objective indexes are sorted with increasing magnification (ex : 1:2X, 4:20X).
		"""
		if index == self.getObjectiveIndex():
			return # already the selected objective : avoid the objective from moving up/down again
		
		if index not in (1,2,3,4):
			raise ValueError("Objective index must be one of 1,2,3,4.") 
		
		self.checkLidClosed()

		cmd =  "SetObjective({})".format(index)
		self.sendCommand(cmd)
		self._waitForFinished()
		print(cmd)

	def setDefaultProjectFolder(self, folder):
		r"""
		Set the default project folder, used when no path is specified for the acquire command. 
		Use double-backslash \\, single forward slash or raw strings with single backslash \ ex: r"a\b" as delimiter between path elements.
		Images will be saved in subfolders of this default project folder, in unique subfolders named with a timestamp, followed by the PlateId.
		i.e DefaultProjectFolder > timestamp_PlateId
		"""
		if not isinstance(folder ,str):
			raise TypeError("Folder must be a string.")
		
		cmd = "SetDefaultProjectFolder(\"{}\")".format(folder)
		#self.cmd = cmd # this was just to inspect the sent command without having a print version but really the string object
		self.sendCommand(cmd)
		self._waitForFinished()
		print(cmd)

	def setPlateId(self, plateId):
		"""
		Set the plateId, used when no path is specified for the acquire command. 
		Images will be saved in subfolders of the default project folder, in unique subfolders named with a timestamp, followed by the PlateId.
		i.e DefaultProjectFolder > timestamp_PlateId
		See setDefaultProjectFolder.
		"""
		cmd = "SetPlateId(\"{}\")".format(plateId)
		self.sendCommand(cmd)
		self._waitForFinished()
		print(cmd)

	def _setImageFilenameAttribute(self, attribute, value):
		"""
		Update one of the filename attribute among :
			- WE : well number
			- PO : subposition
			- LO : timepoint/loop iteration
			- CO : channel number (COlor).
			- Coordinate : the well id (ex: "A001" )
		"""
		listAttribute = ("WE", "PO", "LO", "CO", "Coordinate") # Coordinate is the wellID
		if not (attribute in listAttribute ):
			raise ValueError("attribute must be one of " + listAttribute)
		
		if attribute == "WE" and ( not isinstance(value, int) or value < 1 ):
			raise ValueError("Well number must be a strictly positive integer.""")
		
		if (attribute == "PO" and 
			( not isinstance(value, int) or value < 1 or value > 99 ) ):
			raise ValueError("Subpositions must be in range [1;99].")
			# The PO tag should only have 2 digit t have a fixed filename length.
		
		if (attribute == "LO" and 
			(not isinstance(value, int) or value < 1 or value > 999) ):
			raise ValueError("Timepoints must be in range [1;999].")
		
		if attribute == "CO" and (value < 0 or value > 9) :
			raise ValueError("Channel index ('CO') must be in range [1,9].")
		
		cmd = "SetImageFileNameAttribute(ImageFileNameAttribute.{}, {})".format(attribute, value)
		#print(cmd)
		self.sendCommand(cmd)
		self._waitForFinished()

	def setMetadata(self, wellId, wellNumber, subposition=1, timepoint=1):
		"""Update multiple metadata at once, used to name image files for the next acquisition(s)."""
		self.setMetadataWellId(wellId)
		self.setMetadataWellNumber(wellNumber)
		self.setMetadataSubposition(subposition)
		self.setMetadataTimepoint(timepoint)

	def setMetadataWellNumber(self, number):
		"""Update well number used to name image files for the next acquisitions (WE tag)."""
		self._setImageFilenameAttribute("WE", number)
		print("Set metadata well number - WE:" + str(number))

	def setMetadataWellId(self, wellID, leadingChar = "-"):
		"""
		Update the well ID (ex: "A001"), used to name the image files for the next acquisitions.
		The well ID must start with a letter.
		
		Parameters
		----------
		leadingChar, string
		Character added before the well id, at the beginning of the filename.
		By default this is a slash (-) for compatibility with acquifer software suite, but it could be replaced by another character.
		"""
		
		if not isinstance(wellID, str):
			raise TypeError("WellID must be a string ex: 'A001'.")
		
		if len(wellID) != 4 : 
			raise ValueError("WellId should be a 4-character long string to assure compatibility with the acquifer software suite. Ex : 'A001'")
		
		if not wellID[0].isalpha():
			raise ValueError("WellID must start with a letter, example of well ID 'A001'.")
		
		self._setImageFilenameAttribute("Coordinate", leadingChar + wellID)
		print("Set metadata wellID:" + wellID)

	def setMetadataSubposition(self, subposition):
		"""Update the well subposition index (within a given well), used to name the image files for the next acquisitions (PO tag)."""
		self._setImageFilenameAttribute("PO", subposition)
		print("Set metadata subposition - PO:" + str(subposition))

	def setMetadataTimepoint(self, timepoint):
		"""Update the timepoint (or loop iteration) index, used to name the image files for the next acquisitions (LO tag)."""
		self._setImageFilenameAttribute("LO", timepoint) # LO for LOOP
		print("Set metadata timepoint - LO:" + str(timepoint))

	def setBrightField(self, channelNumber, detectionFilter, intensity, exposure, lightConstantOn=False):
		"""
		Activate the brightfield light lightSource.
		In live mode, the resulting "channel" is directly switched on, and must be switched off using the setBrightFieldOff command.
		In script mode, the "channel" is switched on with the next acquire commands, synchronously with the camera.

		Parameters
		----------
		channelNumber : int (>0)
			this value is used for the image file name (tag CO).
		
		detectionFilter : int (between 1 and 4)
			positional index of the detection filter (1 to 4), depending on the filter, the overall image intensity varies.
		
		intensity : int between 0 and 100
			intensity for the brightfield light-source.
		
		exposure : int
			exposure time in ms, used by the camera when imaging/previewing this channel.
			In live mode, a value of 0 will freeze the preview image.
		
		lightConstantOn : bool
			if true, the light is constantly on (only during the acquisition in script mode)
			if false, the light lightSource is synchronized with the camera exposure, and thus is blinking.
		"""
		self.checkLidClosed()
		checkChannelParameters(channelNumber, detectionFilter, intensity, exposure, lightConstantOn)
		
		lightConstantOn = "true" if lightConstantOn else "false" # just making sure to use a lower case for true : python boolean is True
		offsetAF = 0 # if one wants to apply an offset, directly do it in the acquire command
		
		self.sendCommand("SetBrightField({}, {}, {}, {}, {}, {})".format(channelNumber, detectionFilter, intensity, exposure, offsetAF, lightConstantOn) )
		print("Switched-on brightfield light-source - filter:{} - {}% - {}ms".format(detectionFilter, intensity, exposure))
		self._waitForFinished()
		
	def setBrightFieldOff(self):
		"""
		Switch the brightfield channel off in live mode, by setting intensity and exposure time to 0.
		This also freezes the image preview (exposure=0).
		In script mode this has no utility : on/off switching is synchronized with the camera acquisition.
		This function thus first check if live mode is active.
		"""
		self.checkLidClosed()
		
		if self.getMode() == "live":
			self.sendCommand("SetBrightField(1, 1, 0, 0, 0, false)") # any channel, filter should do, as long as intensity is 0
			print("Switched-off brightfield light-source.")
			self._waitForFinished()
		
	def setFluoChannel(self, channelNumber, lightSource, detectionFilter, intensity, exposure, lightConstantOn=False):
		"""
		Activate one or multiple LED light sources for fluorescence imaging.
		In live mode, the resulting "channel" is directly switched on, and must be switched off using the setFluoChannelOff command.
		In script mode, the "channel" is switched on with the next acquire commands, synchronously with the camera.

		Parameters
		----------
		channelNumber : int (>0)
			this value is used for the image file name (tag CO).
		
		lightSource : string
			this should be a 6-character string of 0 and 1, corresponding to the LED light lightSource to activate. Ex : "010000" will activate the 2nd light lightSource, while 010001 will activate both the second and last light sources..
		
		detectionFilter : int (between 1 and 4)
			positional index of the detection filter (1 to 4), depending on the filter, the overall image intensity varies.
		
		intensity : int between 0 and 100
			intensity for the LED fluorescent light lightSource(s).
			With multiple light sources, this is the power used for each of them.
		
		exposure : int
			exposure time in ms, used by the camera when imaging/previewing this channel.
			In live mode, a value of 0 will freeze the preview image.
		
		lightConstantOn : bool
			if true, the light is constantly on (only during the acquisition in script mode)
			if false, the light lightSource is synchronized with the camera exposure, and thus is blinking.
		"""
		self.checkLidClosed()
		checkLightSource(lightSource)
		checkChannelParameters(channelNumber, detectionFilter, intensity, exposure, lightConstantOn)
		
		lightConstantOn = "true" if lightConstantOn else "false" # just making sure to use a lower case for true : python boolean is True
		offsetAF = 0 # if one wants to apply an offset, directly do it in the acquire command
		
		cmd = "SetFluoChannel({}, \"{}\", {}, {}, {}, {}, {})".format(channelNumber, lightSource, detectionFilter, intensity, exposure, offsetAF, lightConstantOn)
		#print(cmd)
		self.sendCommand(cmd)
		print("Switched-on fluorescent light source - filter:{} - {}% - {}ms".format(detectionFilter, intensity, exposure))
		self._waitForFinished()

	def setFluoChannelOff(self):
		"""
		Switch off all the LED light sources (fluorescence) by setting the intensities to 0%.
		This also freezes the image preview (exposure=0).
		This is effective in live mode only, in script mode on/off switching occurs automatically with the acquire commands.
		This function thus first check if live mode is active.
		"""
		self.checkLidClosed()
		
		if self.getMode() == "live":
			self.sendCommand("SetFluoChannel(1, \"111111\", 1, 0, 0, 0, false)")
			print("Switch-off fluorescent light sources.")
			self._waitForFinished()

	def setLightSource(self, channelNumber, lightSource, detectionFilter, intensity, exposure, lightConstantOn = False):
		"""
		Switch-on light source, brightfield or fluorescent one(s).
		
		Parameters
		----------
		channelNumber : int (>0)
			this value is used for the image file name (tag CO).
		
		lightSource : string
			light-source used for the acquisition.
			
			For brightfield, it should be 'brightfield' or 'bf' (not case-sensitive)
			
			For fluorescent light sources, this should be a 6-character string of 0 and 1, corresponding to the LED light lightSource to activate. 
			Ex : "010000" will activate the 2nd light lightSource, while 010001 will activate both the second and last light sources.
		
		detectionFilter : int (between 1 and 4)
			positional index of the detection filter (1 to 4), depending on the filter, the overall image intensity varies.
		
		intensity : int between 0 and 100
			relative intensity for the light-source(s).
			If multiple fluorescent light sources are activated, this is the intensity used for each of them.
		
		exposure : int
			exposure time in ms, used by the camera when imaging/previewing this channel.
			In live mode, a value of 0 will freeze the preview image.
		
		lightConstantOn : bool
			if true, the light is constantly on (only during the acquisition in script mode)
			if false (default), the light lightSource is synchronized with the camera exposure, and thus is blinking.
		"""
		if lightSource.lower() in ("brightfield", "bf") :
			self.setBrightField(channelNumber, detectionFilter, intensity, exposure,  lightConstantOn)
		
		else:
			self.setFluoChannel(channelNumber, lightSource, detectionFilter, intensity, exposure, lightConstantOn)

	def setLightSourceOff(self, lightSource):
		"""Switch-off the light-source."""
		checkLightSource(lightSource)
		
		if lightSource.lower() in ("bf","brightfield"):
			self.setBrightFieldOff()
		
		else:
			self.setFluoChannelOff()
	
	def acquire(self, channelNumber,
					  objective,
					  lightSource, 
					  detectionFilter, 
					  intensity, 
					  exposure, 
					  zStackCenter,
					  nSlices, 
					  zStepSize, 
					  lightConstantOn=False, 
					  saveDirectory=""):
		"""
		Acquire a Z-stack composed of nSlices, distributed evenly around a Z-center position, using current objective and camera settings.
		
		Images are named according to the IM filenaming convention, and saved in saveDirectory, or in the default project folder if none is mentioned.
		Use setDefaultProject folder and setPlateID to define this directory and template for the created subdirectory name. 
		Use setMetadata to update image-metadata used for filenaming before calling acquire.
		
		In live mode, this function first switch to script mode (needed for acquire commands) and switch back to live mode after acquisition.
		First call setMode("script") to stay in script mode, and avoid switching back and forth for successive acquire commands.
		
		Note : different camera settings can be used between autofocus and acquisition, use setCamera before the respective commands.
		
		Parameters
		----------
		objective : int
			Objective index used for acquisition, one of 1,2,3,4.
			The indexes are almost always ordered by increasing objective magnification. 
		
		channelNumber : int (>0)
			this value is used for the image file name (tag CO).
		
		lightSource : string
			light-source used for the acquisition.
			
			For brightfield, it should be 'brightfield' or 'bf' (not case-sensitive)
			
			For fluorescent light sources, this should be a 6-character string of 0 and 1, corresponding to the LED light lightSource to activate. 
			Ex : "010000" will activate the 2nd light lightSource, while 010001 will activate both the second and last light sources.
		
		detectionFilter : int (between 1 and 4)
			positional index of the detection filter (1 to 4), depending on the filter, the overall image intensity varies.
		
		intensity : int between 0 and 100
			relative intensity for the light-source(s).
			If multiple fluorescent light sources are activated, this is the intensity used for each of them.
		
		exposure : int
			exposure time in ms.
		
		zStackCenter : float
			center position of the Z-stack in µm, with 0.1 precision.
			One typically uses the value returned by the autofocus (+/- some offset eventually).
		
		nSlices : int
			Number of slice composing the stack	
			
			For odd number of slices, the center slice is acquired at Z-position zStackCenter and (nSlices-1)/2 are acquired above and below this center slice.
			
			For even number of slices, nSlices/2 slices are acquired above and below the center position. No images is acquired for the center position.
		
		zStepSize : float
			distance between slices in µm with 0.1 precision
		
		lightConstantOn : bool
			if true, the light is constantly on (only during the acquisition in script mode)
			if false, the light lightSource is synchronized with the camera exposure, and thus is blinking.
		
		saveDirectory : string, default=""
			Custom directory where the images should be saved. 
			
			Use double-backslash \\, single forward slash or raw strings with single backslash \ ex: r"a\b" as delimiter between path elements.
			
			If not specified the images are saved within the default project directory, in a subdirectory named with a unique timestamp and the default plateID.
			Use setDefaultProjectFolder and setPlateId to define the default values for these fields.
		
		Return
		------
		The path to the directory where the images were saved
		"""
		# This implementation of acquire always switch to script mode(if not the case already) 
		# and systematically set the channel before each acquire command
		# This is to prevent issue of not having set the channel while being in script mode
		self.checkLidClosed()
		
		# check parameters type and value
		checkLightSource(lightSource)
		checkChannelParameters(channelNumber, detectionFilter, intensity, exposure, lightConstantOn)
		checkZstackParameters(zStackCenter, nSlices, zStepSize)
		
		if saveDirectory:
			cmd = "Acquire({}, {:.1f}, {:.1f}, {})".format(nSlices, zStepSize, zStackCenter, saveDirectory)
		else:
			cmd = "Acquire({}, {:.1f}, {:.1f})".format(nSlices, zStepSize, zStackCenter)
		
		print(cmd) # Should appear as top-level command before subcommands are called within Acquire
		
		mode0 = self.getMode() # if we want to go back to live mode
		self.setMode("script") # for acquire to work, needs to be in script mode
		
		# Set objective and light source AFTER switching to script mode
		# switching to script mode reset objective and light source otherwise
		self.setObjective(objective)
		self.setLightSource(channelNumber, lightSource, detectionFilter, intensity, exposure, lightConstantOn)
		
		self.sendCommand(cmd)  # send the acquire command
		outDirectory = self._getFeedback()
		
		self._waitForFinished()
		
		# Go back to live mode if originally in live mode
		if mode0 == "live":
			self.setMode("live") 
		
		return outDirectory

	def _setSettingMode(self, state):
		"""
		Switch to setting mode true/false, needed by software AF in live mode.
		Does not do anything is script mode.
		"""
		if self.getMode() == "script":
			return
		
		cmd = "SettingModeOn()" if state else "SettingModeOff()"
		self.sendCommand(cmd)
		self._waitForFinished()

	def setMode(self, mode):
		"""
		Set the acquisition mode to either "live" or "script".
		This function first checks the current mode before changing it if needed.
		
		In live mode, interaction with the GUI are possible.
		In script mode, interaction with the GUI are not possible. It is used for acquisition with the camera.
		For successive camera acquisitions, switching to script mode is recommended to avoid switching back and forth between script and live mode. 
		Switching to script mode also resets the current objective to the one at index 1, as well as the light source setting.
		"""
		if not isinstance(mode, str):
			raise TypeError("Mode should be either 'script' or 'live'.")
		
		mode = mode.lower() # make it case-insensitive
		
		# Check current mode, this prevent error message from IM when switching to current mode
		if mode == self.getMode(): # actually returns only live/script not setting
			return
		
		if mode == "script":
			self.sendCommand("SetScriptMode(1)")
			print("Switch to 'script' mode.\nNOTE : interaction with the GUI are suspended until 'live' mode is reactivated.")
		
		elif mode == "live":
			self.sendCommand("SetScriptMode(0)")
			print("Switch to 'live' mode.")
		
		else:
			raise ValueError("Mode can be either 'script' or 'live'.")
		
		self._waitForFinished()

	def runSoftwareAutoFocus(self, 
							  objective,
							  lightSource, 
							  detectionFilter, 
							  intensity, 
							  exposure, 
							  zStackCenter,
							  nSlices, 
							  zStepSize, 
							  lightConstantOn=False):
		"""
		Run a software autofocus with a custom channel and current objective and camera settings.
		Return the Z-position of the most focused slice, within a stack centred on a given Z-position, with nSlices each separated by zStepSize.
		This function works with both 'live' and 'script' modes.
		NOTE : Different camera settings can be used between the autofocus and the acquisition, use setCamera before each command respectively.
		
		Parameters
		----------
		objective : int
			Objective index used for autofocus, one of 1,2,3,4.
			The indexes are almost always ordered by increasing objective magnification. 
		
		lightSource : string
			light-source used for the autofocus.
			
			For brightfield, it should be 'brightfield' or 'bf' (not case-sensitive)
			
			For fluorescent light sources, this should be a 6-character string of 0 and 1, corresponding to the LED light lightSource to activate. 
			Ex : "010000" will activate the 2nd light lightSource, while 010001 will activate both the second and last light sources.
		
		detectionFilter : int (between 1 and 4)
			positional index of the detection filter (1 to 4), depending on the filter, the overall image intensity varies.
		
		intensity : int between 0 and 100
			relative intensity for the light-source(s).
			If multiple fluorescent light sources are activated, this is the intensity used for each of them.
		
		exposure : int
			exposure time in ms
		
		zStackCenter : float
			center position of the Z-stack in µm, with 0.1 precision.
		
		nSlices : int
			Number of slice composing the stack.
			
			For odd number of slices, the center slice is acquired at Z-position zStackCenter and (nSlices-1)/2 are acquired above and below this center slice.
			
			For even number of slices, nSlices/2 slices are acquired above and below the center position. No images is acquired for the center position.
		
		zStepSize : float
			distance between slices in µm with 0.1 precision
		
		lightConstantOn : bool
			if true, the light is constantly on (only during the acquisition in script mode)
			if false, the light lightSource is synchronized with the camera exposure, and thus is blinking.
		
		Returns
		-------
		zFocus : float
			The position of the most focused slice within the stack, in µm with 0.1 precision.
		"""
		self.checkLidClosed()
		
		# check parameters type and value
		checkLightSource(lightSource)
		channelNumber = 1 # not important for the autofocus, no filename is saved
		checkChannelParameters(channelNumber, detectionFilter, intensity, exposure, lightConstantOn)
		checkZstackParameters(zStackCenter, nSlices, zStepSize )
		
		self.setObjective(objective)

		mode = self.getMode()
		
		if mode == "live":
			self._setSettingMode(True) # in live mode, setting must be on
		
		# Switch-on light
		self.setLightSource(channelNumber, lightSource, detectionFilter, intensity, exposure, lightConstantOn)
		
		# Send autofocus command and read feedback
		cmd = "SoftwareAutofocus({:.1f}, {}, {:.1f})".format(zStackCenter, nSlices, zStepSize)
		print(cmd)
		zFocus = self._getFloatValue(cmd)
		print("Z-focus = {} µm".format(zFocus))
		
		# In live mode, switch-off light and exit setting mode
		if mode == "live":
			self.setLightSourceOff(lightSource)
			self._setSettingMode(False)
		
		return zFocus

	def runHardwareAutoFocus(self, objective, detectionFilter, zStart) :
		"""
		Run a hardware autofocus and return the Z-position found.
		The hardware autofocus uses a dedicated laser for focusing.
		
		Parameters
		----------
		objective : int
			Objective index used for autofocus, one of 1,2,3,4.
			The indexes are almost always ordered by increasing objective magnification. 
		
		detectionFilter : int
			Positional index of the detection filter used for the autofocus.
		
		zStart : float
			Starting position for the autofocus search.
		
		Returns
		-------
		float
			The Z-position found by the autofocus.
		"""
		self.checkLidClosed()
		
		if not objective in (1,2,3,4):
			raise ValueError("Objective index should be one of 1,2,3,4.")
		
		if not detectionFilter in (1,2,3,4) : 
			raise ValueError("Filter index must be one of 1,2,3,4.")
		
		if not isNumber(zStart) or zStart < 0:
			raise ValueError("zStart must be a positive number.")
		"""
		if not isNumber(offset) or offset < 0:
			raise ValueError("Offset must be a positive number.")
		"""
		offset = 0 # offset to returned zValue can be added manually in the code
		cmd = "HardwareAutofocus({:.1f}, {:.1f}, {}, {})".format(zStart, offset, objective, detectionFilter)
		return self._getFloatValue(cmd)


def testRunScript(im):
	im.runScript("C:\\Users\\Administrator\\Desktop\\Laurent\\laurent_test_tcpip.imsf")

## TEST
if __name__ in ['__builtin__', '__main__']:

	# Create an IM instance
	myIM = TcpIp()

	# Loop over functions, calling the getter/is methods first
	for function in dir(myIM):

		if not (function.startswith("get") or function.startswith("is")) :
			continue # skip non getter

		try :
			print(function , " : ", getattr(myIM, function)()) # Get the function object from the name and call it

		# Print the exception and continue the execution
		except Exception as e:
			print("Exception with ", function)
			print(e)

	
	# Error or not, close the socket
	myIM.closeSocket()
	
	"""
	cmd = "GotoXY(30, 30.003)" 
	cmd = "GotoZ(2940.4)" 
	print (myIM.sendCommand(cmd)) # should print None 
	"""