#Author-Luke Beno
#Description-Tools for creating SteamVR tracked objects in Fusion360.
'''
/*******************************************************************
    Copyright (C) 2017 Triad Semiconductor
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions
    are met:

    1. Redistributions of source code must retain the above copyright
       notice, this list of conditions and the following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright
       notice, this list of conditions and the following disclaimer in the
       documentation and/or other materials provided with the distribution.
    3. Neither the name of the the copyright holder nor the names of its contributors
       may be used to endorse or promote products derived from this software
       without specific prior written permission.
    4. Use of this source code or binary forms in commercial products shall require explicit
       written consent of Triad Semiconductor

    THIS SOFTWARE IS PROVIDED BY THE THE COPYRIGHT HOLDERS AND CONTRIBUTORS ``AS IS'' AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED.  IN NO EVENT SHALL THE INSTITUTE OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
    OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
    HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
    LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
    OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
    SUCH DAMAGE.

    Originally written by Luke Beno
    Please post support questions to @lgbeno on Twitter.

*******************************************************************/
'''

import adsk.core, adsk.fusion,traceback

from .Fusion360CommandBase import Fusion360CommandBase

import tempfile
import json
import os
import webbrowser

class Fusion360_SteamVR_Json(Fusion360CommandBase):
    # Runs when user selects your command from Fusion UI, Build UI here
    def onCreate(self, command, inputs):
        product = self.app.activeProduct
        json_obj = {"channelMap":[],"modelNormals":[],"modelPoints":[]}
        obj_array = {}
        for a in product.activeComponent.constructionAxes:
            index = int(str(a.name).replace('Axis',''))
            obj_array[index] = {"ChannelNum":index-1,"modelNormals":[a.geometry.direction.x,a.geometry.direction.y,a.geometry.direction.z],"modelPoints":[0,0,0]}
        for p in product.activeComponent.constructionPoints:
            index = int(str(p.name).replace('Point',''))
            obj_array[index]['modelPoints'] = [p.geometry.x/100,p.geometry.y/100,p.geometry.z/100]
        for s in obj_array:
            json_obj["channelMap"].append(obj_array[s]["ChannelNum"])
            json_obj["modelNormals"].append(obj_array[s]["modelNormals"])
            json_obj["modelPoints"].append(obj_array[s]["modelPoints"])
        
        # Create a temporary directory.
        tempDir = tempfile.mkdtemp()
        resultFilename = tempDir + '//'+product.activeComponent.name
        resultFilename = resultFilename + '.json'

        json_file_handle =  open(resultFilename, 'w')
        json_file_handle.write(json.dumps(json_obj,indent=2, sort_keys=True))
        webbrowser.open(resultFilename)
        #sensorBodySelection = inputs.addSelectionInput('sensorBodySelection', 'Sensor Object', 'Select the bodies where Sensors may be placed')
        #obstacleSelection = inputs.addSelectionInput('obstacleSelection', 'Obstacles', 'Select the bodies that could occlude Sensors')
        #self.json_path =  inputs.addTextBoxCommandInput('json_path', 'JSON Path: ', 'C:/example.json', 1, False)
        
    # Runs when when any input in the command dialog is changed
    def onInputChanged(self, command, inputs, changedInput):
        pass
        
    # Runs when the user presses ok button
    def onExecute(self, command, inputs):
        pass

commands = []
command_defs = []

# Define parameters for command
cmd = {
        'commandName': 'Generate SteamVR JSON (Triad Semiconductor)',
        'commandDescription': 'Dev Tool for making SteamVR Tracked Object JSON Files \nWritten by Luke Beno \n(c) Triad Semiconductor',
        'commandResources': './Resources/Fusion360_SteamVR_Json',
        'cmdId': 'Fusion360_SteamVR_Json_CmdId',
        'workspace': 'FusionSolidEnvironment',
        'toolbarPanelID': 'SolidScriptsAddinsPanel',
        'class' : Fusion360_SteamVR_Json
}
command_defs.append(cmd)

debug = False
for cmd_def in command_defs:
    # Creates the commands for use in the Fusion 360 UI
    command = cmd_def['class'](cmd_def, debug)
    commands.append(command)

def run(context):
    for command in commands:
        command.onRun()

def stop(context):
    for command in commands:
        command.onStop()
