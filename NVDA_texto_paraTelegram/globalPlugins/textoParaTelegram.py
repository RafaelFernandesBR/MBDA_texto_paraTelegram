import globalPluginHandler
import ui
import urllib.request
import urllib.parse
import api
import json

chatId='885615688'
tokemBot='1820018763:AAHTTC5m_AvjaGoo8_sinIfTZ0HHRW3HK2c'

def sendTelegram(text):
		text=urllib.parse.quote(text)
		url ="https://api.telegram.org/bot"+tokemBot+"/sendMessage?chat_id="+chatId+"&text="+str(text)
		headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 tSafari/537.36'}
		res = urllib.request.Request(url)
		res.add_header('user-agent', 'M	ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36')
		content = urllib.request.urlopen(res)
		content=json.load(content)
		if(content['ok'] == True):
			return 'Texto enviado'

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def script_sendText(self, gesture):
		clipboardText = api.getClipData()
		send=sendTelegram(clipboardText)
		ui.message(str(send))

	__gestures={
"kb:NVDA+0": "sendText"	
	}