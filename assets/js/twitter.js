function appendScript(src) {
	var el = new Element('script', {'type': 'text/javascript', 'src': src});
	el.inject($(document.body));
}
window.addEvent('domready', function () {
	appendScript('http://twitter.com/javascripts/blogger.js');
	appendScript('http://twitter.com/statuses/user_timeline/' +
			'7cerebros.json?callback=twitterCallback2&count=3');
});
