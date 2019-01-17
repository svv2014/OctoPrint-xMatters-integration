# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import requests


class XmattersIntegrationPlugin(octoprint.plugin.StartupPlugin,
								octoprint.plugin.TemplatePlugin,
								octoprint.plugin.SettingsPlugin,
								octoprint.plugin.EventHandlerPlugin):

	def on_after_startup(self):
		self._logger.info("xMatters (enabled: %s)" % self._settings.get(["enabled"]))

	def get_settings_defaults(self):
		return dict(apikey="<API key>",
					recipients="< comma separated recipients >",
					secret="<serecret>",
					integrationUrl="<Integration Url >",
					enabled=False,
					enablePrintStarted=False,
					enablePrintDone=False,
					enablePrintPaused=False,
					enablePrintResumed=False,
					enablePrintFailed=False,
					enableMovieDone=False)

	def get_template_configs(self):
		return [
			dict(type="navbar", custom_bindings=False),
			dict(type="settings", custom_bindings=False)
		]

	def send_xmatters_notification(self, title, details):
		if not self._settings.get(["enabled"]):
			return

		recipients = self._settings.get(["recipients"])
		apikey = self._settings.get(["apikey"])
		secret = self._settings.get(["secret"])
		url = self._settings.get(["integrationUrl"])

		headers = {'Content-Type': 'application/json'}
		payload = "{ \"properties\": { \"Title\": \"%s\", \"Details\": \"%s\"}, \"recipients\": [ \"%s\" ] }" % (
			title, details, recipients)

		self._logger.info(" sending notification with payload: %s" % payload)
		r = requests.post(url=url, auth=(apikey, secret), data=payload, headers=headers)

		self._logger.info(" response: %s" % r.text)

	# http:/docs.octoprint.org/en/master/events/index.html#printing
	def on_event(self, event, payload):
		title = "OctoPrint "
		
		if event == "PrintStarted" and self._settings.get(["enablePrintStarted"]):
			self._logger.info("xMatters ( event: %s)" % event)
			details = "Printing started for the file: %s%s ,<br> storage location %s" % (payload.path, payload.name, payload.origin)
			title += " Print Started %s" % payload.name
			self.send_xmatters_notification(title, details)

		if event == "PrintDone" and self._settings.get(["enablePrintDone"]):
			self._logger.info("xMatters ( event: %s)" % event)
			details = "Printing Finished for the file: %s%s ,<br> storage location %s <br> time: %s " % (payload.path, payload.name, payload.origin, payload.time)
			title += " Printing Finished %s " % payload.name
			self.send_xmatters_notification(title, details)

		if event == "PrintPaused" and self._settings.get(["enablePrintPaused"]):
			self._logger.info("xMatters ( event: %s)" % event)
			details = "Printing Paused for the file: %s%s ,<br> storage location %s, <br> position: %s" % (payload.path, payload.name, payload.origin, payload.position)
			title += " Printing Paused %s " % payload.name
			self.send_xmatters_notification(title, details)

		if event == "PrintResumed" and self._settings.get(["enablePrintResumed"]):
			self._logger.info("xMatters ( event: %s)" % event)
			details = "Printing Resumed for the file: %s%s ,<br> storage location %s" % (payload.path, payload.name, payload.origin)
			title += " Printing Resumed %s " % payload.name
			self.send_xmatters_notification(title, details)

		if event == "PrintFailed" and self._settings.get(["enablePrintFailed"]):
			self._logger.info("xMatters ( event: %s)" % event)
			details = "Printing Failed for the file: %s%s ,<br> storage location %s,<br> time: %s,<br> failure reason: %s " % (payload.path, payload.name, payload.origin, payload.time, payload.reason)
			title += " Printing Failed %s " % payload.name
			self.send_xmatters_notification(title, details)

		if event == "MovieDone" and self._settings.get(["enableMovieDone"]):
			self._logger.info("xMatters ( event: %s)" % event)
			details = "Rendering Time-laps is finished. File: %s ,<br> GCODE file: %s" % (payload.movie, payload.gcode)
			title += " Time-laps rendered %s " % payload.movie_basename
			self.send_xmatters_notification(title, details)

__plugin_name__ = "xMatters Integration"
__plugin_implementation__ = XmattersIntegrationPlugin()
