import esocat
import base64

text = base64.b64decode(
	'KD08YCM5XX42WlkzMjdVdjQtUXNxcE1uJitJaiInRSVle0Fifnc9XzpdS3clbzQ0VXFwMC9RP3hOdkw6YEglYyNERDJeV1Y+Z1k7ZHRzNzZxS0pJbVprag=='
	).decode()
esocat.detect(text)