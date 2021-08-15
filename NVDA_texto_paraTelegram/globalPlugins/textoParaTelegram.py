import globalPluginHandler
import ui
import urllib.request
import urllib.parse
import api
import json
import wx
import gui
from gui import nvdaControls
import config

def sendTelegram(text):
		text=urllib.parse.quote(text)
		chatId=config.conf["textoParaTelegram"]["chatId"]
		tokemBot=config.conf["textoParaTelegram"]["tokemBot"]
		url ="https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(tokemBot, chatId, text)
		headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 tSafari/537.36'}
		res = urllib.request.Request(url)
		res.add_header('user-agent', 'M	ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36')
		content = urllib.request.urlopen(res)
		content=json.load(content)
		if(content['ok'] == True):
			return 'Texto enviado'

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		confspec = {
			'chatId': 'integer(default=0)',
			'tokemBot': 'string(default=Insira seu tokem aqui:)'
		}
		config.conf.spec['textoParaTelegram'] = confspec
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(TextoParaTelegramSettingsPanel)

	def terminate(self):
		super(GlobalPlugin, self).terminate()
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(TextoParaTelegramSettingsPanel)

	def script_sendText(self, gesture):
		clipboardText = api.getClipData()
		send=sendTelegram(clipboardText)
		ui.message(str(send))

	__gestures={
		"kb:NVDA+0": "sendText"	
	}

class TextoParaTelegramSettingsPanel(gui.SettingsPanel):
	title = 'Texto Para Telegram'

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		self._chatIdLabel = sHelper.addLabeledControl("Informe o &chat ID do usuário que vai receber a mensagem:", wx.TextCtrl)
		self._tokemLabel = sHelper.addLabeledControl("Informe o &tokem do seu bot:", wx.TextCtrl)
		self._setValues()

	def _setValues(self):
		self._chatIdLabel.SetValue(str(config.conf['textoParaTelegram']['chatId']))
		self._tokemLabel.SetValue(config.conf['textoParaTelegram']['tokemBot'])

	def onSave(self):
		config.conf['textoParaTelegram']['chatId'] = self._chatIdLabel.GetValue()
		config.conf['textoParaTelegram']['tokemBot'] = self._tokemLabel.GetValue()