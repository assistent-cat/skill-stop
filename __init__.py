# Copyright 2016 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from adapt.intent import IntentBuilder
from mycroft.messagebus.message import Message, dig_for_message
from mycroft import MycroftSkill, intent_handler


class StopSkill(MycroftSkill):
    def __init__(self):
        super().__init__(name="StopSkill")

    @intent_handler(IntentBuilder("").require("Stop"))
    def handle_stop(self, event):
        # Framework catches this, invokes stop() method on all skills
        message = dig_for_message()
        m = message.forward('mycroft.stop') if message \
            else Message('mycroft.stop')
        self.bus.emit(m)

    ######################################################################
    # Typically the enclosure will handle all of the following
    # NOTE: system.update is generated by skill-version-checker
    ######################################################################

    @intent_handler("reboot.intent")
    def handle_reboot(self, event):
        if self.ask_yesno("confirm.reboot") == "yes":
            self.bus.emit(Message("system.reboot"))

    @intent_handler("shutdown.intent")
    def handle_shutdown(self, event):
        if self.ask_yesno("confirm.shutdown") == "yes":
            self.bus.emit(Message("system.shutdown"))

    @intent_handler('wifi.setup.intent')
    def handle_wifi_setup(self, event):
        self.bus.emit(Message("system.wifi.setup"))

    @intent_handler('ssh.enable.intent')
    def handle_ssh_enable(self, event):
        self.bus.emit(Message("system.ssh.enable"))

    @intent_handler('ssh.disable.intent')
    def handle_ssh_disable(self, event):
        self.bus.emit(Message("system.ssh.disable"))

def create_skill():
    return StopSkill()
