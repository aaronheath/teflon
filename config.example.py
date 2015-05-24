# Teflon Configuration (Example)

config = {
	## Debug Mode (debug)
	# True - redirections will not be performed and debug information will be in the output.
	# False - redirections will be performeed if rule matches.
	"debug": False,

	## Redirction Objects (redirections)
	# src - Regular expression to match against the URL.
	# dest - Where to redirect the browser to.
	"redirections": [
		{
			"src": ".+/google.*",
			"dest": "https://google.com/"
		},
		{
			"src": ".+",
			"dest": "https://aaronheath.com/"
		}
	]		
}